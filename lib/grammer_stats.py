class GrammarStats():
    def __init__(self):
        self._passed_check = 0
        self._failed_check = 0

    def check(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        if text == "":
            raise ValueError("Unable to check grammar as no sentence was given.")
        
        punc_marks = [".", "!", "?"]
        if text[0].islower() or text[-1] not in punc_marks:
            self._failed_check += 1
            return False
        else:
            self._passed_check += 1
            return True
            
    def percentage_good(self):
        total_sentences_checked = self._passed_check + self._failed_check
        if total_sentences_checked == 0:
            raise Exception("Unable to check percentage pass rate as no sentence was given.")
        pass_rate = (self._passed_check / total_sentences_checked) * 100 
        return int(pass_rate)