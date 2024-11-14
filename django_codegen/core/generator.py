class CodeGenerator:
    """
    La clase CodeGenerator interactúa con el cliente OpenAI para generar código Django
    a partir de los inputs proporcionados por el usuario.
    """

    def __init__(self, prompts_module, gpt_client):
        self.prompts_module = prompts_module
        self.gpt_client = gpt_client

    def generate(self, user_inputs, class_type):
        """
        Genera código para el tipo de clase especificado.

        :param user_inputs: Datos proporcionados por el usuario.
        :param class_type: Tipo de clase a generar (e.g., 'model', 'serializer').
        :return: Código generado.
        """
        prompt_method = getattr(self.prompts_module, f'get_{class_type}_prompt', None)
        if not prompt_method:
            raise ValueError(f"No se encontró un prompt para el tipo '{class_type}'.")

        prompt = prompt_method(user_inputs['models'])
        return self.gpt_client.call(prompt)
