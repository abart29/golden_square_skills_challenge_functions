import pytest
from lib.manage_time import *

"""
Given text AND how many words read per minute
Returns text as string and number of words per min
"""
# def test_given_text_returns_as_string():
#     assert manage_time("walk the dogs today") == "walk the dogs today" 

"""
Given a text as string
Returns how many words are in the text
"""
# def test_counts_how_many_words_in_text():
#     assert manage_time("walk the dogs today") == 4 

"""
Given how 10 words in text
Returns calcuation how many seconds it takes to read 10 words based of 200 words per min
"""
def test_time_to_read_10_words():
    assert manage_time("walk the dogs today and train them and feed them") == 3

"""
Given how 200 words in text
Returns calcuation how many minutes seconds
"""
def test_time_to_read_200_words():
    text = " ".join(["hello"] * 200)
    assert manage_time(text) == 60 


"""
Given how 300 words in text
Returns calcuation how many seconds 
"""
def test_pass_300_words():
    text = " ".join(["hello"] * 300)
    assert manage_time(text) == 90

"""
Given 98 words in a text
Returns calculations how many seconds to read the text based of 200 words per min
"""
def test_pass_98_words():
    text = " ".join(["hello"] * 98)
    assert manage_time(text) == 30

def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        manage_time("")
    error_message =str(e.value)
    assert error_message == "Can't estimate a reading time for an empty text"