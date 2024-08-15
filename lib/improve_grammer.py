def improve_grammer(text):
    punc_marks = [".", "!", "?"]
    if text == "":
        raise Exception("There is no text to verify.")
    elif text[0].isupper() and text[-1] in punc_marks:
        return "Grammer is ok."
    elif text[0].islower() and text[-1] not in punc_marks:
        return "Text doesn't start with capital or end with punctuation mark."
    elif text[0].islower():
        return "Text doesn't start with a capital letter."
    elif text[-1] not in punc_marks:
        return "Text doesn't end with a punctuation mark."