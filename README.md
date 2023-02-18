# Массовое вступление в чат ВК

## Описание:
    input.json - Должен содержать данные аккаунтов ВК

    {
      "0": {
        "user_id": "TEST_USER_ID",
        "username": "TEST_USERNAME",
        "password": "TEST_PASSWORD",
        "url_profile": "TEST_URL_PROFILE",
        "access_token": "TEST_ACCESS_TOKEN"
      },
      "1": {
        "user_id": "TEST_USER_ID",
        "username": "TEST_USERNAME",
        "password": "TEST_PASSWORD",
        "url_profile": "TEST_URL_PROFILE",
        "access_token": "TEST_ACCESS_TOKEN"
      }
    }

## Зависимости:
    aiohttp-3.8.4 Async http client/server framework (asyncio)

## Запуск:
    python main.py