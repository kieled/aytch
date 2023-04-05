from typing import Literal
import aiohttp


class YoutubeGrabberHelper:
    def __init__(self, lang: Literal["ru", "en"]):
        self.headers = {
            "X-YouTube-Client-Name": "1",
            "X-YouTube-Client-Version": "2.20201021.03.00",
            "accept-language": "ru-RU,ru;q=0.9" if lang == "ru" else "en-US,en,q=0.9",
        }

    async def make_channel_request(self, url):
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=10), headers=self.headers
        ) as s:
            try:
                async with s.get(url) as response:
                    return await response.json()
            except aiohttp.ClientError as e:
                return {"error": True, "message": e}

    async def fetch(self, channel_url):
        if "https://www.youtube.com/" not in channel_url:
            raise Exception("Incorrect youtube channel url")

        url = channel_url if "?" not in channel_url else channel_url.split("?")[0]

        url = (
            url
            + ("/" if channel_url[-1] != "/" else "")
            + "about?flow=grid&view=0&pbj=1"
        )
        return await self.perform_channel_request(url)

    async def perform_channel_request(self, url):
        channel_page_response = await self.make_channel_request(url)
        if isinstance(channel_page_response, dict) and channel_page_response.get(
            "error"
        ):
            raise Exception(channel_page_response["message"])
        return channel_page_response

    @staticmethod
    def find_tab(tabs):
        return next(
            (tab for tab in tabs if tab.get("tabRenderer", {}).get("selected")), None
        )
