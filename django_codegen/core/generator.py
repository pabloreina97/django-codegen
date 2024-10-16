import openai

class CodeGenerator:
    """
    La clase [CodeGenerator] se encarga de interactuar con GPT-4 para generar el código a partir de los inputs recibidos.
    """
    
    def __init__(self, prompts_module):
        self.prompts_module = prompts_module

    def generate(self, user_inputs):
        models_code = self.generate_models(user_inputs['models'])
        serializers_code = self.generate_serializers(user_inputs['serializers'])
        viewsets_code = self.generate_viewsets(user_inputs['viewsets'])
        return models_code, serializers_code, viewsets_code

    def generate_models(self, models):
        prompt = self.prompts_module.get_model_prompt(models)
        return self.call_gpt(prompt)

    def generate_serializers(self, serializers):
        prompt = self.prompts_module.get_serializer_prompt(serializers)
        return self.call_gpt(prompt)

    def generate_viewsets(self, viewsets):
        prompt = self.prompts_module.get_viewset_prompt(viewsets)
        return self.call_gpt(prompt)

    def call_gpt(self, prompt):
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text
