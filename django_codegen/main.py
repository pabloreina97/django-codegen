import os
from core.generator import CodeGenerator
from core.manager import CodeGenManager
from core.writer import CodeWriter
from prompts.openai_client import OpenAIClient
from prompts.prompt_builder import PromptBuilder

def main():
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

    print("Bienvenido al generador de código Django. Vamos a crear tus modelos.")

    while True:
        # Pedimos al usuario que introduzca el nombre del modelo
        model_name = input("Introduce el nombre del modelo (o Enter para finalizar): ").strip()
        if model_name.lower() == '':
            break

        # Preguntamos los campos del modelo
        fields = input(f"Introduce los campos del modelo {model_name} separados por comas (o deja en blanco para generar automáticamente): ").strip()

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
        manager.generate_code(user_inputs)
        print(f"Código generado en el directorio: {output_dir}")
    else:
        print("No se ha creado ningún modelo.")

if __name__ == '__main__':
    main()
