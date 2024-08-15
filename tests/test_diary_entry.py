import pytest
from lib.diary_entry import DiaryEntry

"""
Given empty title and contents
Raised error
"""
def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
    error_message = str(err.value)
    assert error_message == "Diary entries must have title and contents"


"""
Given diary entry with title and contents
Return correctly formatted diary entry
"""

def test_given_diary_entry_returned_correct_format():
    entry = DiaryEntry("Monday", "I failed to debug correctly")
    assert entry.format() == "Monday: I failed to debug correctly"


"""
Given diary entry
Returns the amount of words in the diary entry
"""
def test_amount_of_words_in_entry():
    entry = DiaryEntry("Monday", "I failed to debug correctly")
    assert entry.count_words() == 5

"""
Given diary entry to calculate reading time of contents
Returns estimate in minutes (int) of reading time 
"""
def test_estimate_reading_time_in_minutes():
    entry = DiaryEntry("Monday", "Hello hello hello hello hello")
    assert entry.reading_time(5) == 1

"""
Given diary entry to calculate reading time of contents
Returns estimate in minutes (int) of reading time 
"""
def test_estimate_reading_time_in_minutes():
    entry = DiaryEntry("Monday", "Hello hello hello hello hello")
    assert entry.reading_time(2) == 3

"""
Given a wpm of 0
Raises exception error 
"""
def test_errors_on_0_wpm_given():
    entry = DiaryEntry("Title", "One two three")
    with pytest.raises(Exception) as err:
        entry.reading_time(0)
    error_message = str(err.value)
    assert error_message == "Can't calculate reading time without wpm of 0"

"""
Given diary entry and int rep num wpm user can read per min
AND int rep num of minutes the user to read
Return string which show the contents the user could read dep on the minutes given
"""

def test_show_words_depending_on_minutes_user_had_to_read():
    entry = DiaryEntry("Monday", "one two three four five six seven eight nine ten")
    assert entry.reading_chunk(5, 1) == "one two three four five"

"""
Given contents of 10 words
reading_chunk > First time with given wpm 5 and 1 min return "one two three four five"
reading_chunk > Second time with given wpm 1 and 1 min return return "six"
reading_chunk > Third time with given wpm 4 and 1 min return return return "seven eight nine ten"
"""

def test_reading_chunk_called_multiple_times_with_various_wpm():
    entry = DiaryEntry("Monday", "one two three four five six seven eight nine ten")
    assert entry.reading_chunk(5, 1) == "one two three four five"
    assert entry.reading_chunk(1, 1) == "six"
    assert entry.reading_chunk(4, 1) == "seven eight nine ten"
    
"""
Given context of six words
if reading_chunk called repeatedly 
Last chunk is the last words in text, even if shorter than could be read
Next chunk after starts again
"""

def test_reading_chunk_called_multiple_times_and_starts_again():
    entry = DiaryEntry("Monday", "one two three four five six seven eight nine ten")
    assert entry.reading_chunk(5, 1) == "one two three four five"
    assert entry.reading_chunk(5, 1) == "six seven eight nine ten"
    assert entry.reading_chunk(5, 1) == "one two three four five"