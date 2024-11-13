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
        with open('data/user.py', 'r') as file:
            user_model = file.read()

        with open('data/user_serializer.py') as file:
            user_serializer = file.read()

        self.writer.write(user_model, user_serializer, '', '')
