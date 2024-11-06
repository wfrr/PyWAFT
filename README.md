# Python Web Automation Testing Framework

## Описание

Исследовательский проект по разработке фреймворка для автоматизации тестирования web-приложения
[Mealie](https://github.com/mealie-recipes/mealie) на Python с использованием pytest и Selenium.

### Пример запуска теста в Firefox

`$ python -m pytest tests/mealie/ui/test_login.py --variables config/stand/mealie-test.toml --variables config/browser/firefox-120.toml`

### Примеры конфига браузера

```toml
# Firefox
[browser]
name = "firefox"
version = "100"

[[browser.prefs]]
"browser.download.manager.showWhenStarting" = false
```

```toml
# Chrome
[browser]
cli-arguments = ["--incognito", "--user-data-dir=C:\\Temp\\chrome"]
name = "chrome"
version = "119"

[[browser.prefs]]
"download.prompt_for_download" = false
"safebrowsing.enabled" = true
```

```toml
# Edge
[browser]
cli-arguments = "--incognito"
name = "firefox"
version = "100"
```

### Пример конфига тестового стенда

```toml
[stand]
env = "test"

[stand.app]
url = "http://127.0.0.4/store/"

[stand.db]
username = "user"
password = "12345"
host = "127.0.0.4"
port = "3306"
name = "store"

[stand.users]

[stand.users.customer]
customer_id = 1
email = "user@mail.com"
username = "user"
password = "123123"
url = "http://127.0.0.4/store/index.php?route=account/login"

[stand.users.admin]
username = "admin"
password = "admin"
url = "http://127.0.0.4/store/admin/"
```
