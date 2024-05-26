# Python Web Automation Testing Framework

## Описание
Исследовательский проект по разработке фреймворка для автоматизации тестирования web-приложения
[OpenCart](https://github.com/opencart/opencart) на Python с использованием pytest и Selenium.

### Примеры конфига браузера


```
# Firefox
[browser]
name = "firefox"
version = "100"
```

```
# Chrome
[browser]
cli-arguments = ["--incognito", "--user-data-dir=C:\\Temp\\chrome"]
name = "chrome"
version = "119"
```

```
# Edge
[browser]
cli-arguments = "--incognito"
name = "firefox"
version = "100"
```

### Пример конфига тестового стенда

```
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
