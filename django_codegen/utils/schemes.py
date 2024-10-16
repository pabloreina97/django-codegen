format_schema_many = {
    "type": "json_schema",
    "json_schema": {
        "name": "model_schema_list",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "classes": {
                    "type": "array",
                    "description": "Lista de objetos que representan diferentes clases.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "model": {
                                "type": "string",
                                "description": "El nombre del modelo en minúsculas.",
                            },
                            "class": {
                                "type": "string",
                                "description": "El tipo de clase generada (model, serializer, view, url...)",
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

format_schema_one = {
    "type": "json_schema",
    "json_schema": {
        "name": "model_schema",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "class": {
                    "type": "string",
                    "description": "El tipo de clase generada (model, serializer, view, url...)",
                },
                "code": {
                    "type": "string",
                    "description": "El código generado.",
                },
            },
            "required": ["class", "code"],
            "additionalProperties": False,
        },
    },
}
