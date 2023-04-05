import aytch
import pytest


@pytest.mark.asyncio
async def test_author_channel():
    data = await aytch.get_channel_info(
        channel_url="https://www.youtube.com/channel/UCfMJ2MchTSW2kWaT0kK94Yw"
    )
    assert data["author"] == "William Osman"


@pytest.mark.asyncio
async def test_user_channel():
    data = await aytch.get_channel_info(
        channel_url="https://www.youtube.com/user/wsim7165"
    )
    assert data["author"] == "William Sim"


@pytest.mark.asyncio
async def test_description_channel():
    data = await aytch.get_channel_info(
        channel_url="https://www.youtube.com/user/LinusTechTips"
    )
    assert (
        data["description"]
        == 'Linus Tech Tips is a passionate team of "professionally curious" experts in '
        "consumer technology and video production who aim to educate and entertain.\n"
    )


@pytest.mark.asyncio
async def test_username_channel():
    data = await aytch.get_channel_info(
        channel_url="https://www.youtube.com/@DjangoSchool"
    )
    assert data["author_id"] == "UC_hPYclmFCIENpMUHpPY8FQ"
