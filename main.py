import json
import asyncio
from contextlib import suppress

import aiohttp


class VK:
    """
    Класс для взаимодействия с ВК
    """

    def __init__(self, token: str) -> None:
        """
        Метод инициализации класса

        :param token: Токен аккаунта ВК
        """
        self.headers = {'Authorization': f'Bearer {token}'}

    async def join_chat(self, link: str) -> tuple[bool, str]:
        """
        Метод для вступления в чат ВК по ссылке

        :return: tuple[bool, str]
        """
        params = dict(
            link=link,
            v=5.131
        )
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(f'https://api.vk.com/method/messages.joinChatByInviteLink',
                                   params=params) as response:
                json_response = await response.json()
                if 'error' in json_response:
                    return False, json_response["error"]["error_msg"]
                else:
                    return True, json_response['response']


def file_input() -> dict:
    """
    Функция читает и возвращает словарь с данными аккаунтов

    :return: dict
    """
    with open('./input.json', 'r') as file:
        return json.load(file)


async def main() -> None:
    """
    Главная функция запуска

    :return: None
    """
    link = input('Введите пригласительную ссылку в чат: ')
    input_data = file_input()  # Получаем словарь с данными аккаунтов
    for key in input_data.keys():  # Перебираем словарь по его ключам
        account = input_data[key]
        vk = VK(token=account["access_token"])  # Инициализируем класс
        status, response = await vk.join_chat(link)  # Вступаем в чат
        if status:  # Если вступление в чат удалось
            print(f'Вступил в чат - {account["url_profile"]}')
        else:  # Если вступление в чат не удалось
            print(f'Возникла ошибка - {account["url_profile"]}: {response}')


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):  # Игнорирование ошибок при остановке
        asyncio.run(main())  # Запуск асинхронной функции из синхронного контекста
