from enum import Enum


class Schema(Enum):

    APP_ABOUT_INFO = {
        "production": "boolean",
        "version": "string",
        "demoStatus": "boolean",
        "allowSignup": "boolean",
        "defaultGroupSlug": "string",
        "defaultHouseholdSlug": "string",
        "enableOidc": "boolean",
        "oidcRedirect": "boolean",
        "oidcProviderName": "string",
        "enableOpenai": "boolean",
        "enableOpenaiImageServices": "boolean",
    }
    APP_ABOUT_STARTUP_INFO = {
        "isFirstLogin": "boolean",
        "isDemo": "boolean",
    }

    def __value__(self) -> dict[str, str]:
        return self.value
