import os

class CodeWriter:
    """
    Este componente se encarga de escribir el código generado en los archivos adecuados,
    separando cada modelo, serializer y viewset en archivos individuales.
    """
    
    def __init__(self, project_root):
        self.project_root = project_root

    def write(self, models_code, serializers_code, viewsets_code):
        """
        Método principal para escribir el código en las carpetas adecuadas.
        """
        self.write_to_file('models', models_code)
        self.write_to_file('serializers', serializers_code)
        self.write_to_file('viewsets', viewsets_code)

    def write_to_file(self, directory, content_list):
        """
        Escribe cada bloque de código en un archivo individual dentro de la carpeta correspondiente.

        :param directory: El subdirectorio donde se guardarán los archivos (por ejemplo, 'models', 'serializers', 'viewsets').
        :param content_list: Lista de diccionarios con la información del modelo, el tipo de clase y el código.
        """
        # Creamos el directorio si no existe
        dir_path = os.path.join(self.project_root, directory)
        os.makedirs(dir_path, exist_ok=True)

        # Escribimos cada archivo individual basado en el contenido del diccionario
        for item in content_list:
            # Cada clave en el diccionario es el nombre del archivo (sin extensión)
            file_path = os.path.join(dir_path, f"{item.get('model')}_{item.get('class')}.py")
            with open(file_path, 'w') as file:
                file.write(item.get('code'))
