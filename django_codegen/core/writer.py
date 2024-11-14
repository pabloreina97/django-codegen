import os


class CodeWriter:
    """
    Este componente se encarga de escribir el código generado en los archivos adecuados,
    permitiendo escribir cualquier archivo en cualquier directorio especificado.
    """

    def __init__(self, project_root):
        self.project_root = project_root

    def write(self, file_path, code):
        """
        Método genérico para escribir código en un archivo específico.

        :param file_path: Ruta relativa donde se guardará el archivo.
        :param code: Código a escribir en el archivo.
        """
        full_path = os.path.join(self.project_root, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(code)
