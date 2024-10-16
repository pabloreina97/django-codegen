import click
from gpt_codegen.core.manager import CodeGenManager
from gpt_codegen.core.generator import CodeGenerator
from gpt_codegen.core.writer import CodeWriter
from gpt_codegen.prompts import model_prompt, serializer_prompt, viewset_prompt

@click.command()
@click.option('--project-root', prompt="Introduce el directorio raíz del proyecto",
              help="Directorio raíz donde se escribirán los archivos generados.")
def run(project_root):
    manager = CodeGenManager()
    
    # Configuramos el generador y el escritor
    generator = CodeGenerator(prompts_module={
        "models": model_prompt,
        "serializers": serializer_prompt,
        "viewsets": viewset_prompt
    })
    writer = CodeWriter(project_root)
    
    manager.set_generator(generator)
    manager.set_writer(writer)
    
    # Ejemplo de inputs recogidos (esto debería provenir de un flujo de input interactivo)
    user_inputs = {
        "models": {"User": ["id: IntegerField", "username: CharField"], "Post": ["id: IntegerField", "content: TextField"]},
        "serializers": {"UserSerializer": ["id", "username"], "PostSerializer": ["id", "content"]},
        "viewsets": {"UserViewSet": ["list", "retrieve"], "PostViewSet": ["list", "retrieve", "create"]}
    }
    
    manager.generate_code(user_inputs)

if __name__ == "__main__":
    run()
