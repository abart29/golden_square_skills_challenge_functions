import pytest
from lib.grammer_stats import GrammarStats

"""
Given a string that starts with a capital letter and ends with suitable punctuation 
Returns True 
"""
def test_string_starts_with_capital_ends_with_punctuation():
    sentence = GrammarStats()
    assert sentence.check("Hello World!") == True

"""
Given a string that starts without a capital letter but ends with suitable punctuation
Returns False
"""
def test_given_string_starts_without_capital_letter():
    sentence = GrammarStats()
    assert sentence.check("hello World!") == False

"""
No string is given
Raise exception error
"""

def test_empty_string_input():
    sentence = GrammarStats()
    with pytest.raises(ValueError) as e:
        sentence.check("")  # Empty string input
    error_message = str(e.value)
    assert error_message == "Unable to check grammar as no sentence was given."



def test_non_string_input():
    sentence = GrammarStats()
    with pytest.raises(TypeError) as e:
        sentence.check(123)  # Non-string input
    error_message = str(e.value)
    assert error_message == "Input must be a string."



"""
Given a string that starts without a capital letter and doesn't end with suitable punctuation
Returns False
"""
def test_given_string_ends_without_punctuation():
    sentence = GrammarStats()
    assert sentence.check("hello world") == False

"""
Given 2 checks 
Returns an int percentage of how many have passed and how many have failed
Example - 2 sentences given: 1 fails. 1 passes. = 50% passed
"""
def test_check_pass_percentage_of_two_sentence():
    sentence = GrammarStats()
    sentence.check("One two three!")
    sentence.check("one two three")
    assert sentence.percentage_good() == 50

"""
Given 12 checks 
Returns an int percentage of how many have passed and how many have failed
Example - 12 sentences given: 3 fails. 9 passes. = 75% passed
"""
def test_check_pass_percentage_of_twelve_sentences():
    sentence = GrammarStats()
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    assert sentence.percentage_good() == 75

"""
Given 12 checks 
Returns an int percentage of how many have passed and how many have failed
Example - 12 sentences given: 9 fails. 3 passes. = 25% passed
"""
def test_check_pass_percentage_of_twelve_sentences_with_nine_fails():
    sentence = GrammarStats()
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("One two three!")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    sentence.check("one two three")
    assert sentence.percentage_good() == 25

"""
No string/sentence to check over 
Raise exception error
"""
def test_no_string_to_check():
    sentence = GrammarStats()
    with pytest.raises(Exception) as e:
        sentence.percentage_good()
    error_message = str(e.value)
    assert error_message == "Unable to check percentage pass rate as no sentence was given."