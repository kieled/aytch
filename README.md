<h2 align="center">:small_red_triangle: AYTCH - Async YouTube Channels Scrapper :small_red_triangle:</h2>

![Logo](https://user-images.githubusercontent.com/68655454/229973420-c79ee91d-e73a-4358-95ff-78f501e99902.jpg)


<p align="center">
    <a href="https://pypi.python.org/pypi/aytch" alt="PyPi Package Version">
        <img src="https://img.shields.io/pypi/v/aytch.svg" /></a>
    <a href="https://pypi.python.org/pypi/aytch" alt="Supported Python versions">
        <img src="https://img.shields.io/pypi/pyversions/aytch.svg" /></a>
    <a href="https://github.com/kieled/aytch/actions/workflows/test.yaml" alt="GitFlow">
        <img src="https://github.com/kieled/aytch/actions/workflows/test.yaml/badge.svg" /></a>
    <a href="https://codecov.io/gh/kieled/aytch" alt="codecov">
        <img src="https://codecov.io/gh/kieled/aytch/branch/main/graph/badge.svg?token=3M53KOF8R1" /></a>
</p>


<p align="center">AYTCH is a Python library for extracting information about YouTube channels. It uses AIOHTTP library for best performance and concurrent fetching support. Library very lightweight (11KB) and return only extra nessesary information about any youtube channel.</p>


## :pencil2: Installation
You can install AYTCH using pip:

```python
pip install aytch
```

## :bookmark_tabs: Usage
Here's an example of how to use AYTCH to get information about a YouTube channel:

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
    channel_url: str, 
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

Example:
```python
{
    'author': 'The Slow Mo Guys',
    'author_id': 'UCUK0HBIBWgM2c4vsPhkYY4w',
    'author_url': 'https://www.youtube.com/channel/UCUK0HBIBWgM2c4vsPhkYY4w',
    'author_thumbnail': 'https://yt3.ggpht.com/ytc/AAUvwnhRnI8Lr...',
    'subscriber_count': 14500000,
    'description': 'The best slow motion on Youtube.  \n\nWe shoot all of our...',
    'view_count': '265308911'
}

```

## :recycle: Contributing
Contributions to aytch are welcome! If you'd like to contribute, please fork the repository and make a pull request.

## :warning: License
aytch is licensed under the MIT License. See LICENSE for more information.

<p align="center">Inspired by <a href="https://github.com/FreeTubeApp/yt-channel-info">yt-channel-info</a></p>
