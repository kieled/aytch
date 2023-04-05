import pytest

from aytch.utils import DictSearch


@pytest.mark.asyncio
async def test_dict_search():
    input_item = {"a": 1, "b": {"c": 2, "d": {"e": 3}}, "f": [{"g": 4}, {"h": 5}]}
    dict_search = DictSearch(input_item)

    assert list(dict_search.search("e")) == ["b.d.e"]
    assert list(dict_search.search("g")) == ["f[0].g"]
    assert list(dict_search.search("i")) == []

    assert dict_search.get_value("a") == 1
    assert dict_search.get_value("b.c") == 2
    assert dict_search.get_value("b.d.e") == 3
    assert dict_search.get_value("f[0].g") == 4
    assert dict_search.get_value("f[1].h") == 5
    assert dict_search.get_value("i") is None
