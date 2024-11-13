from prompts.prompt_builder import PromptBuilder
from prompts.openai_client import OpenAIClient
from core.writer import CodeWriter
from core.manager import CodeGenManager
from core.generator import CodeGenerator
import sys
import os
import time
import itertools
import threading
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)


def spinner():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\rGenerando código... {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + Fore.GREEN + Style.BRIGHT + '\nGeneración completada!    \n')


def main():
    global done

    # Crear instancia del cliente GPT usando la API_KEY de las variables de entorno
    gpt_client = OpenAIClient(api_key=os.environ.get("OPENAI_API_KEY"))
    manager = CodeGenManager()

    # Obtener la ruta del directorio actual para la salida
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, 'output')

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
        # Pedimos al usuario que introduzca el nombre del modelo
        model_name = input(f"{Fore.BLUE}Introduce el nombre del modelo (o Enter para finalizar): ").strip()
        if model_name.lower() == '':
            break

        if model_name.lower() == 'user':
            manager.create_user()

        # Preguntamos los campos del modelo
        fields = input(f"{Fore.YELLOW}Introduce los campos del modelo {model_name} separados por comas (o deja en blanco para generar automáticamente): ").strip()

        # Si el usuario deja los campos en blanco, GPT generará los campos
        if not fields:
            fields = 'gpt_auto_generate'  # Marcador especial para indicar que GPT debe generar los campos

        # Verificar si los campos incluyen otros modelos (para relaciones ForeignKey)
        fields_list = fields.split(', ') if fields != '--gpt_auto_generate' else []
        for field in fields_list:
            if field in created_models:
                # Si el campo es un modelo existente, lo tratamos como un ForeignKey
                fields = fields.replace(field, f"{field} (ForeignKey)")

        # Agregar el modelo a la lista de modelos del usuario
        user_inputs['models'].append({
            'name': model_name,
            'fields': fields
        })

        # Agregar el modelo creado a la lista de modelos existentes
        created_models.add(model_name.lower())

    if user_inputs['models']:
        # Si se han introducido modelos, generamos y escribimos el código
        done = False
        t = threading.Thread(target=spinner)
        t.start()

        manager.generate_code(user_inputs)

        done = True
        t.join()

        print(f"{Fore.GREEN}Código generado en el directorio: {output_dir}")
    else:
        print(Fore.RED + "No se ha creado ningún modelo.")


if __name__ == '__main__':
    main()
