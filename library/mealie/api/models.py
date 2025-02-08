"""Модели для валидирования ответов API."""

APP_ABOUT_INFO = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "production": {"type": "boolean"},
        "version": {"type": "string"},
        "demoStatus": {"type": "boolean"},
        "allowSignup": {"type": "boolean"},
        "defaultGroupSlug": {"type": ["string", "null"]},
        "defaultHouseholdSlug": {"type": ["string", "null"]},
        "enableOidc": {"type": "boolean"},
        "oidcRedirect": {"type": "boolean"},
        "oidcProviderName": {"type": "string"},
        "enableOpenai": {"type": "boolean"},
        "enableOpenaiImageServices": {"type": "boolean"},
    },
    "required": [
        "production",
        "version",
        "demoStatus",
        "allowSignup",
        "defaultGroupSlug",
        "defaultHouseholdSlug",
        "enableOidc",
        "oidcRedirect",
        "oidcProviderName",
        "enableOpenai",
        "enableOpenaiImageServices",
    ],
}

APP_ABOUT_STARTUP_INFO = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "isFirstLogin": {"type": "boolean"},
        "isDemo": {"type": "boolean"},
    },
    "required": ["isFirstLogin", "isDemo"],
}

ALL_USERS = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "admin": {"type": "boolean", "enum": [True, False]},
                    "email": {"type": "string", "format": "email"},
                    "fullName": {"type": "string"},
                    "group": {"type": "string"},
                    "household": {"type": "string"},
                    "username": {"type": "string"},
                },
                "required": [
                    "admin",
                    "email",
                    "fullName",
                    "group",
                    "household",
                    "username",
                ],
            },
        },
        "next": {"type": ["string", "null"]},
        "previous": {"type": ["string", "null"]},
    },
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "items",
        "next",
        "previous",
    ],
}

CREATE_USER = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "admin": {"type": "boolean", "enum": [True, False]},
        "email": {"type": "string", "format": "email"},
        "fullName": {"type": "string"},
        "group": {"type": "string"},
        "household": {"type": "string"},
        "username": {"type": "string"},
    },
    "required": ["admin", "email", "fullName", "group", "household", "username"],
}
