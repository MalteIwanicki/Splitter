class Splitter:
    """Splits a list into multiple ones"""

    def __init__(self, the_list_to_split: list) -> None:
        self.list = the_list_to_split

    def split_into(self, wanted_parts: int) -> list:
        length = len(self.list)
        out = []
        for i in range(wanted_parts):
            start_pos = i * length // wanted_parts
            end_pos = (i + 1) * length // wanted_parts
            out.append(self.list[start_pos:end_pos])
        return out
