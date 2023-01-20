import random

class SpotHandler:
    def __init__(self):
        pass
    def process(self, text: str) -> str:
        text_list = list(text)
        random.shuffle(text_list)
        return ''.join(text_list)

spot_handler = SpotHandler()
