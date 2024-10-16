class PromptBuilder:
    """
    Esta clase se encarga de construir los prompts para la generación de modelos, serializers y viewsets.
    """

    @staticmethod
    def get_model_prompt(models):
        model_str = "\n".join([f"Modelo: {model['name']} con campos {model['fields']}" for model in models])
        return (f"Genera el código Django para los siguientes modelos. \n{model_str}\n. Si en los campos pone '--gpt_auto_generate', entonces genera los campos automáticamente según el modelo. Haz las importaciones necesarias en cada uno de los modelos.")

    @staticmethod
    def get_serializer_prompt(models):
        model_str = "\n".join([f"Modelo: {model['name']} con campos {model['fields']}" for model in models])
        return f"Genera el código Django para los serializers de los siguientes modelos: \n{model_str}.\n No pongas '__all__' en los campos, sino escríbelos explícitamente. Haz las importaciones necesarias en cada uno de los serializadores."

    @staticmethod
    def get_viewset_prompt(models):
        model_names = [model['name'] for model in models]
        return f"Genera el código Django para los ModelViewsets de los siguientes modelos: {', '.join(model_names)}. Haz las importaciones necesarias en cada una de las vistas."

    @staticmethod
    def get_urls_prompt(models):
        model_names = [model['name'] for model in models]
        return f"Genera el código Django para registrar URLs de las viewsets de los siguientes modelos: {', '.join(model_names)}. Hazlo con rest framework routers."