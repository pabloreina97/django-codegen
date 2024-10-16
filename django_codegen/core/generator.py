class CodeGenerator:
    """
    La clase CodeGenerator interactúa con el cliente OpenAI para generar código Django a partir de los inputs
    proporcionados por el usuario.
    """

    def __init__(self, prompts_module, gpt_client):
        self.prompts_module = prompts_module
        self.gpt_client = gpt_client

    def generate(self, user_inputs):
        # Primero generamos los modelos
        models_code = self.generate_models(user_inputs['models'])
        # Luego generamos los serializers
        serializers_code = self.generate_serializers(user_inputs['models'])  # Pasamos los mismos modelos para los serializers
        # Finalmente generamos los viewsets
        viewsets_code = self.generate_viewsets(user_inputs['models'])  # Usamos los modelos para los viewsets
        return models_code, serializers_code, viewsets_code

    def generate_models(self, models):
        prompt = self.prompts_module.get_model_prompt(models)
        return self.gpt_client.call(prompt)

    def generate_serializers(self, models):
        prompt = self.prompts_module.get_serializer_prompt(models)
        return self.gpt_client.call(prompt)

    def generate_viewsets(self, models):
        prompt = self.prompts_module.get_viewset_prompt(models)
        return self.gpt_client.call(prompt)
