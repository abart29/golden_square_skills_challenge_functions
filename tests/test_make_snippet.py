from lib.make_snippet import *

"""
Takes one worded string
Returns one worded string
"""
def test_returns_given_one_worded_string():
    result = make_snippet("hello")
    assert result == "hello"

"""
Takes string with four words
Returns string with four words
"""
def test_return_string_with_five_words():
    result = make_snippet("Walk the dog today")
    assert result == "Walk the dog today"

"""
Takes string with 5 words
Returns first 5 words
"""
def test_returns_first_five_words_in_string():
    result = make_snippet("Walk the dogs today Andy")
    assert result == "Walk the dogs today Andy"

"""
Takes string containing 5 or more words
Returns 5 words and adds "..." at the end > 5 
"""
def test_if_greater_than_five_words_return_5_words_and_ellipsis():
    result = make_snippet("You have to walk both dogs today")
    assert result == "You have to walk both..."