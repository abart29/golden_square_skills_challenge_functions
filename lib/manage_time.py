import math

def manage_time(text):
    if text == "":
        raise Exception("Can't estimate a reading time for an empty text")
    words = len(text.split())
    return math.ceil((60 / 200) * words)