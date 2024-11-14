import os
import sys
import time
import threading
from itertools import cycle

from colorama import Fore, Style, init

from core.generator import CodeGenerator
from core.manager import CodeGenManager
from core.writer import CodeWriter
from prompts.openai_client import OpenAIClient
from prompts.prompt_builder import PromptBuilder

init(autoreset=True)


class Spinner:
    def __init__(self, message):
        self.message = message
        self.spinner = cycle(['|', '/', '-', '\\'])
        self._stop_event = threading.Event()
        self.thread = threading.Thread(target=self._spin)

    def _spin(self):
        while not self._stop_event.is_set():
            sys.stdout.write(f'\r{self.message} {next(self.spinner)}')
            sys.stdout.flush()
            time.sleep(0.1)

    def start(self):
        self.thread.start()

    def stop(self):
        self._stop_event.set()
        self.thread.join()


def main():
    # Crear instancia del cliente GPT usando la API_KEY de las variables de entorno
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(Fore.RED + "La variable de entorno OPENAI_API_KEY no está configurada.")
        sys.exit(1)

    gpt_client = OpenAIClient(api_key=api_key)
    manager = CodeGenManager()

    # Obtener la ruta del directorio actual para la salida
    output_dir = os.getcwd()

    # Inicializamos el generador y el escritor
    generator = CodeGenerator(PromptBuilder(), gpt_client)
    writer = CodeWriter(output_dir)

    manager.set_generator(generator)
    manager.set_writer(writer)

    # Almacenar los modelos creados por el usuario
    user_inputs = {'models': []}
    created_models = set()

    print(Fore.CYAN + Style.BRIGHT + "Bienvenido al generador de código Django.")
    print(Fore.CYAN + "Vamos a crear tus modelos.\n")

    while True:
        try:
            # Pedimos al usuario que introduzca el nombre del modelo
            model_name = input(f"{Fore.BLUE}Introduce el nombre del modelo (o Enter para finalizar): ").strip()
            if not model_name:
                break

            if model_name.lower() == 'user':
                manager.create_user()
                created_models.add('user')
            else:
                # Preguntamos los campos del modelo
                fields = input(
                    f"{Fore.YELLOW}Introduce los campos del modelo {model_name} separados por comas (o deja en blanco para generar automáticamente): "
                ).strip()

                # Si el usuario deja los campos en blanco, GPT generará los campos
                if not fields:
                    fields = 'gpt_auto_generate'  # Marcador especial para indicar que GPT debe generar los campos

                # Verificar si los campos incluyen otros modelos (para relaciones ForeignKey)
                fields_list = [field.strip() for field in fields.split(',')]
                for field in fields_list:
                    if field.lower() in created_models:
                        # Si el campo es un modelo existente, lo tratamos como un ForeignKey
                        fields = fields.replace(field, f"{field} (ForeignKey)")

                # Agregar el modelo a la lista de modelos del usuario
                user_inputs['models'].append({
                    'name': model_name,
                    'fields': fields
                })

                # Agregar el modelo creado a la lista de modelos existentes
                created_models.add(model_name.lower())
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            sys.exit(0)

    if user_inputs['models']:
        spinner = Spinner("Generando código...")
        spinner.start()

        try:
            manager.generate_code(user_inputs)
        except Exception as e:
            print(Fore.RED + f"\nError al generar el código: {e}")
            spinner.stop()
            sys.exit(1)

        spinner.stop()
        print(f"{Fore.GREEN}Código generado en el directorio: {output_dir}")
    else:
        print(Fore.RED + "No se ha creado ningún modelo.")


if __name__ == '__main__':
    main()
