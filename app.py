import json
import asyncio
from contextlib import suppress

import aiohttp
from loguru import logger


class VkApi:
    def __init__(self, access_token: str) -> None:
        self.host = 'https://api.vk.com/method/'
        self.params = {'v': 5.131}
        self.headers = {'Authorization': f"Bearer {access_token}"}

    async def join_chat(self, link: str) -> tuple[bool, str | None]:
        method = 'messages.joinChatByInviteLink'
        self.params["link"] = link
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.host + method, params=self.params) as response:
                json_response = await response.json()
                if 'error' in json_response:
                    return False, json_response["error"]["error_msg"]
                else:
                    return True, None


def load_data(filename: str) -> dict:
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


async def main() -> None:
    data = load_data('data.json')
    link = input('Введите ссылку на чат: ')
    for key, user in data.items():
        vk_api = VkApi(user["access_token"])
        result = await vk_api.join_chat(link)
        if result[0]:
            logger.success(f'Вступил в чат "{link}" - {user["url_profile"]}')
        else:
            logger.warning(f'Возникла проблема "{result[1]}" - {user["url_profile"]}')


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
