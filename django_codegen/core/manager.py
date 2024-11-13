import os


class CodeGenManager:
    """
    Este archivo contendrá un Manager que se encargará de orquestar el flujo completo, desde la interacción con el
    usuario hasta la escritura de archivos. Aplicamos el patrón Singleton para evitar que haya múltiples instancias
    de este Manager.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CodeGenManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.generator = None
            self.writer = None

    def set_generator(self, generator):
        self.generator = generator

    def set_writer(self, writer):
        self.writer = writer

    def generate_code(self, user_inputs):
        if not self.generator or not self.writer:
            raise Exception("Generator and Writer must be set before generating code.")

        models_code, serializers_code, viewsets_code, urls_code = self.generator.generate(user_inputs)
        self.writer.write(models_code, serializers_code, viewsets_code, urls_code)

    def create_user(self):
        root_dir = os.path.dirname(os.path.dirname(__file__))
        user_model_path = os.path.join(root_dir, 'data', 'user.py.txt')
        user_serializer_path = os.path.join(root_dir, 'data', 'user_serializer.py.txt')

        with open(user_model_path, 'r') as file:
            user_model = file.read()

        with open(user_serializer_path, 'r') as file:
            user_serializer = file.read()

        self.writer.raw_write('models.py', user_model)
        self.writer.raw_write('serializers.py', user_serializer)
