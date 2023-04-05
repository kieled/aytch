import re
from typing import Literal
from aytch.utils import DictSearch
from aytch.helper import YoutubeGrabberHelper


async def get_channel_info(channel_url: str, lang: Literal["ru", "en"] = "en"):
    """
    Retrieve information about a YouTube channel given its URL.

    :param channel_url: The URL of the channel.
    :type channel_url: str
    :param lang: The language of the channel's metadata. Default is 'en'.
    :type lang: Literal['ru', 'en']
    :return: A dictionary containing the following information about the channel:
        - author: The name of the channel's author.
        - author_id: The external ID of the channel's author.
        - author_url: The URL of the channel's author.
        - author_thumbnail: The URL of the channel's author's thumbnail image.
        - subscriber_count: The number of subscribers to the channel.
        - description: The description of the channel.
        - view_count: The total number of views on the channel.
    :rtype: dict
    """
    yt_helper = YoutubeGrabberHelper(lang)
    result = await yt_helper.fetch(channel_url)
    if isinstance(result, list):
        result = [i["response"] for i in result if "response" in i][0]
    page_data = DictSearch(result)

    if result.get("alerts"):
        raise Exception(page_data.get_value("alerts[0].alertRenderer.text.simpleText"))

    meta_data = page_data.get_value(next(page_data.search("channelMetadataRenderer")))
    header_data = page_data.get_value(next(page_data.search("c4TabbedHeaderRenderer")))
    if not header_data:
        header_data = next(page_data.search("topicChannelDetailsRenderer"))
        if header_data:
            header_data = page_data.get_value(header_data)

    header_tabs = result["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]
    about_tab = YoutubeGrabberHelper.find_tab(header_tabs)

    subscriber_text = page_data.get_value(
        f"{next(page_data.search('subscriberCountText'))}.simpleText"
    )

    subscriber_multiplier = re.findall(
        r"[a-zA-Zа-яА-Я]+", subscriber_text.split(" ")[0]
    )[0].lower()

    subscriber_number = float(
        re.sub(r"(?![\d,.]+).+", "", subscriber_text).replace(",", ".")
    )

    views = "0"
    if about_tab:
        for i in page_data.search("viewCountText"):
            if i:
                views = page_data.get_value(i).get("simpleText")
                views = re.sub(r"\D", "", views)

    subscriber_count = subscriber_number
    if subscriber_multiplier == ("тыс" if lang == "ru" else "k"):
        subscriber_count *= 1000
    elif subscriber_multiplier == ("млн" if lang == "ru" else "m"):
        subscriber_count *= 1000000

    return dict(
        author=meta_data["title"] if meta_data else header_data["title"]["simpleText"],
        author_id=meta_data["externalId"]
        if meta_data
        else header_data["navigationEndpoint"]["browseEndpoint"]["browseId"],
        author_url=meta_data["vanityChannelUrl"]
        if meta_data
        else header_data["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"][
            "url"
        ],
        author_thumbnail=header_data["avatar"]["thumbnails"][-1]["url"],
        subscriber_count=int(subscriber_count),
        description=meta_data.get("description") or "",
        view_count=views,
    )
