import os


class CodeGenManager:
    """
    Manager que orquesta el flujo completo, desde la interacción con el usuario hasta la escritura de archivos.
    """

    def __init__(self):
        self.generator = None
        self.writer = None

    def set_generator(self, generator):
        self.generator = generator

    def set_writer(self, writer):
        self.writer = writer

    def generate_code(self, user_inputs):
        if not self.generator or not self.writer:
            raise Exception("Generator and Writer must be set before generating code.")

        # Lista de tipos de clase a generar
        class_types = ['model', 'serializer', 'viewset', 'urls']
        generated_codes = []

        for class_type in class_types:
            codes = self.generator.generate(user_inputs, class_type)
            for item in codes:
                # Definir la ruta de archivo según el tipo
                if class_type == 'urls':
                    file_path = f"{class_type}.py"
                else:
                    directory = f"{class_type}s"
                    file_name = f"{item.get('model')}_{class_type}.py"
                    file_path = os.path.join(directory, file_name)

                generated_codes.append({'path': file_path, 'code': item.get('code')})

        # Escribir todos los archivos generados
        for code_item in generated_codes:
            self.writer.write(code_item['path'], code_item['code'])

    def create_user(self):
        root_dir = os.path.dirname(os.path.dirname(__file__))
        user_model_path = os.path.join(root_dir, 'data', 'user.py.txt')
        user_serializer_path = os.path.join(root_dir, 'data', 'user_serializer.py.txt')

        with open(user_model_path, 'r') as file:
            user_model = file.read()

        with open(user_serializer_path, 'r') as file:
            user_serializer = file.read()

        self.writer.write('models.py', user_model)
        self.writer.write('serializers.py', user_serializer)
