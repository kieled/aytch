<h2 align="center">:small_red_triangle: AYTCH - Async YouTube Channels Info :small_red_triangle:</h2>

![f71e489b-7db1-480f-8f5b-1954d4a70a17](https://user-images.githubusercontent.com/68655454/229964492-2a6fa0db-99da-411c-8b9a-41f959aa266a.jpg)


<p align="center">Inspired by <a href="https://github.com/FreeTubeApp/yt-channel-info">yt-channel-info</a></p>

AYTCH is a Python library for extracting information about YouTube channels. It uses web scraping techniques to retrieve data from YouTube's web pages without any API keys and limits.


## :pencil2: Installation
You can install YoutubeGrabber using pip:

```python
pip install aytch
```

## :bookmark_tabs: Usage
Here's an example of how to use YoutubeGrabber to get information about a YouTube channel:

```python
import asyncio
from aytch import get_channel_info

async def main():
    channel_url = 'https://www.youtube.com/channel/UCdX9ulb8u0oUf8pUzg9Z5Jw'
    channel_info = await get_channel_info(channel_url)
    print(channel_info)

asyncio.run(main())
```
## :link: API
```python
get_channel_info(
    channel_url: URL, 
    lang: 'en' | 'ru' = 'en'
) -> dict
```
Retrieves information about a YouTube channel.

#### Parameters:

* **channel_url (str)**: _The URL of the YouTube channel to get information about._
* **lang (str)**: _The language of the YouTube page. Can be either 'en' or 'ru'. Defaults to 'en'._

#### Returns:

A dictionary containing the following information about the channel:

* **author (str)**: _The name of the channel's author._
* **author_id (str)**: _The external ID of the channel's author._
* **author_url (str)**: _The URL of the channel's author._
* **author_thumbnail (str)**: _The URL of the channel's author's thumbnail image._
* **subscriber_count (int)**: _The number of subscribers to the channel._
* **description (str)**: _The description of the channel._
* **view_count (str)**: _The total number of views on the channel._

## :recycle: Contributing
Contributions to aytch are welcome! If you'd like to contribute, please fork the repository and make a pull request.

License
aytch is licensed under the MIT License. See LICENSE for more information.
