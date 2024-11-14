code_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "model_schema_list",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "classes": {
                    "type": "array",
                    "description": "Lista de diccionarios con el código e información de las clases generadas.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "model": {
                                "type": "string",
                                "description": "El nombre del modelo en minúsculas. Si en un mismo código hay diferentes modelos, se pone '*' para indicar que es para todos los modelos.",
                            },
                            "class": {
                                "type": "string",
                                "description": "El tipo de clase generada (model, serializer, view, urls...)",
                            },
                            "code": {
                                "type": "string",
                                "description": "El código generado.",
                            },
                        },
                        "required": ["model", "class", "code"],
                        "additionalProperties": False,
                    },
                }
            },
            "required": ["classes"],
            "additionalProperties": False,
        },
    },
}
