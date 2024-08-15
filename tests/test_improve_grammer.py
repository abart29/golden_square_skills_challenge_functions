import pytest
from lib.improve_grammer import improve_grammer
"""
Given a string with capital and punc mark
It returns grammer is ok
"""
def test_given_correct_string():
    assert improve_grammer("Hello world.") == "Grammer is ok."

"""
Given a string that starts with a capital and no punc mark
It returns a string to improve grammer.
"""
def test_string_has_no_capital_letter():
    assert improve_grammer("hello world.") == "Text doesn't start with a capital letter."

"""
Given a string that starts with no capital but ends with a punc mark
It returns a string to improve grammer.
"""
def test_given_string_doesnt_end_with_punc_mark():
    assert improve_grammer("Hello world") == "Text doesn't end with a punctuation mark."
"""
Given a string that starts with no capital and doesn't ends with a punc mark
It returns a string to improve grammer.
"""
def test_no_capital_or_punc_mark():
    assert improve_grammer("hello world") == "Text doesn't start with capital or end with punctuation mark."

"""
Given an empty string
It returns an error
"""
def test_if_empty_text_raises_error():
    with pytest.raises(Exception) as e:
        improve_grammer("")
    error_message = str(e.value)
    assert error_message == "There is no text to verify."

"""
testing other punctuation marks
"""

def test_other_punc_mark():
    assert improve_grammer("Hello World!") == "Grammer is ok."