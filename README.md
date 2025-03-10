# FastApi + Python, QA-Guru intro

Микросервис на Python + FastAPI

## Установка

Инструкции по установке

```bash
# Клонируйте репозиторий:
git clone https://github.com/shade1471/fast_api_intro.git
cd /fast_api_intro

# Установите зависимости:
pip install -r requirements.txt

# Запустите сервис FastApi:
uvicorn main:app --reload
```
## Запуск авто-тестов
```bash
# В новом окне терминала выполните команду:
pytest test_fast_api.py

```


## Endpoint's

```
# Получить данные по пользователю
GET /api/users/{user_id}
Возвращает данные пользователя по ID.
```

```
# Создать пользователя
POST /api/users/
Создает нового пользователя. Ожидает JSON с полями name и job.
```

```
# Обновить пользователя
PUT /api/users/{user_id}
Обновляет данные существующего пользователя. Ожидает JSON с полями name и job.
```

```
# Удалить пользователя
DELETE /api/users/{user_id}
Удаляет пользователя по ID.
```
## Предустановленные данные

При новом запуске сервиса, существует 5 пользователей, id c 1 по 5.
