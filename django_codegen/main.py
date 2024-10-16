import os
from core.generator import CodeGenerator
from core.manager import CodeGenManager
from core.writer import CodeWriter
from prompts.openai_client import OpenAIClient
from prompts.prompt_builder import PromptBuilder


def main():
    # Creamos una única instancia del cliente GPT como Singleton
    gpt_client = OpenAIClient(api_key=os.environ.get("OPENAI_API_KEY"))
    manager = CodeGenManager()

    # Inicializamos el generador y el escritor
    generator = CodeGenerator(PromptBuilder(), gpt_client)
    writer = CodeWriter(r'C:\Users\PabloReinaGalvez\OneDrive - GRUPO HISPATEC INFORMATICA EMPRESARIAL\Documentos\Utilidades\django_codegen\output')

    manager.set_generator(generator)
    manager.set_writer(writer)

    # Simulamos el input del usuario para los modelos
    user_inputs = {
        'models': [
            {
                'name': 'User',
                'fields': 'username, email, password'
            },
            {
                'name': 'Post',
                'fields': 'title, content, user_id'
            }
        ]
    }

    # Generamos y escribimos el código
    manager.generate_code(user_inputs)

if __name__ == '__main__':
    main()
