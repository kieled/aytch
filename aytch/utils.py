from dataclasses import dataclass


@dataclass
class DictSearch:
    input_item: dict

    def search(self, search_value: str):
        def process(data, path=""):
            if not isinstance(data, dict):
                return
            for k, v in data.items():
                new_path = f"{path}.{k}" if path else k
                if k == search_value:
                    yield new_path
                if isinstance(v, dict):
                    yield from process(v, new_path)
                if isinstance(v, list):
                    for i, value in enumerate(v):
                        yield from process(value, f"{new_path}[{i}]")

        return process(self.input_item)

    def get_value(self, path: str):
        current = self.input_item
        for key in path.split("."):
            if "[" in key:
                paths = key.split("[")
                current = current.get(paths[0], {})[int(paths[1][:-1])]
            else:
                current = current.get(key, {})
        return current if current != {} else None
