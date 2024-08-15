from lib.count_words import count_words

"""
Given a single worded string as an argument 
Returns single worded string
"""
# def test_returns_one_worded_string():
#     assert count_words("Hello") == "Hello"

"""
Given multiple worded string
Returns multiple worded string
"""
# def test_multiple_worded_string():
#     assert count_words("one, two, three, four") == "one, two, three, four"


"""
If given empty string
Return zero
"""
def test_count_empty_string():
    assert count_words("") == 0

"""
Given string with muplitple words  
Returns number of words from given string
"""
def test_counts_words_in_given_string():
    assert count_words("Make sure you walk the dogs and train them.") == 9

