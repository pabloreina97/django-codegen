import json
from openai import OpenAI
from utils.schemes import code_schema


class OpenAIClient:
    """
    Cliente Singleton para interactuar con la API de OpenAI usando el método correcto de `client.chat.completions.create`.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(OpenAIClient, cls).__new__(cls)
        return cls._instance

    def __init__(self, api_key, model="gpt-4o-mini"):
        if not hasattr(self, '_initialized'):
            self.client = OpenAI(api_key=api_key)
            self.model = model
            self._initialized = True

    def call(self, prompt):
        """
        Método para realizar una llamada a GPT usando `client.chat.completions.create` con el formato adecuado.
        :param prompt: El prompt que se enviará a GPT.
        :param many: Indica si se esperan varios codigos o uno solo para todas las clases.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Eres un experto en Django que genera código para un proyecto Django."},
                {"role": "user", "content": prompt}
            ],
            response_format=code_schema,
            max_tokens=1024
        )
        # Devolvemos el contenido generado por GPT
        result = json.loads(response.choices[0].message.content)

        return result.get('classes', [])
