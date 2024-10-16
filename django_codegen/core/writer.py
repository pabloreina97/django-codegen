import os

class CodeWriter:
    """
    Este componente se encarga de escribir el código generado en los archivos adecuados.
    """
    
    def __init__(self, project_root):
        self.project_root = project_root

    def write(self, models_code, serializers_code, viewsets_code):
        self.write_to_file('models', models_code)
        self.write_to_file('serializers', serializers_code)
        self.write_to_file('views', viewsets_code)

    def write_to_file(self, directory, content):
        os.makedirs(os.path.join(self.project_root, directory), exist_ok=True)
        for file_name, code in content.items():
            file_path = os.path.join(self.project_root, directory, f"{file_name}.py")
            with open(file_path, 'w') as file:
                file.write(code)
