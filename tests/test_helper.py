import pytest
from aytch.helper import YoutubeGrabberHelper


@pytest.mark.asyncio
async def test_compare_json():
    def get_channel_id(item):
        return (
            item[1]
            .get("response")
            .get("header")
            .get("c4TabbedHeaderRenderer")
            .get("channelId")
        )

    data = await YoutubeGrabberHelper("en").fetch(
        channel_url="https://www.youtube.com/channel/UCmDX0sR-FHpWM1xFcpSQ3hw"
    )
    assert get_channel_id(data) == "UCmDX0sR-FHpWM1xFcpSQ3hw"
