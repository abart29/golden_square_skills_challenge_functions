import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have title and contents")
        self.title = title
        self.contents = contents
        self.read_so_far = 0
        

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Can't calculate reading time without wpm of 0")
        reading_time = len(self.contents.split()) / wpm 
        return math.ceil(reading_time)

    def reading_chunk(self, wpm, minutes):
        words_per_chunk = wpm * minutes
        words = self.contents.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_per_chunk
        chunk_of_words = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_of_words)


