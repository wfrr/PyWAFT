ECHOER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "client": {
            "type": "object",
            "properties": {
                "host": {"type": "string", "format": "ipv4"},
                "port": {"type": ["string", "integer"]},
            },
            "required": ["host", "port"],
        },
        "request": {
            "type": "object",
            "properties": {
                "http": {
                    "type": "object",
                    "properties": {
                        "method": {"type": "string"},
                        "path": {"type": "string"},
                        "protocol": {"type": "string"},
                    },
                    "required": ["method", "path", "protocol"],
                },
                "params": {"type": ["string", "null"]},
                "query_param": {
                    "type": "object",
                    "additionalProperties": {"type": "string"},
                },
                "headers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": {"type": "string"},
                    },
                },
                "body": {
                    "type": ["array", "string"],
                    "items": [
                        {
                            "type": "array",
                            "items": [{"type": "string"}, {"type": "string"}],
                        }
                    ],
                },
            },
            "required": ["http", "params", "query_param", "headers", "body"],
        },
        "op_result": {"type": ["string", "null"]},
    },
    "required": ["client", "request", "op_result"],
}
