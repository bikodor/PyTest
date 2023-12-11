POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"}   #, "enum": ["х"]; х == то,
        # что точно должно присутствовать в json
    },
    "required": ["id"]
}

# {'id': 1, 'title': 'Post 1'}