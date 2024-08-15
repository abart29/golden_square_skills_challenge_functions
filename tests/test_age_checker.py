import pytest
from lib.age_checker import *


from datetime import datetime

"""
Given a DOB, that equates to current age >= 16,
It returns "access is granted"

age_checker('1993-02-02') => "access is granted"
"""

def test_given_dob_turns_access_granted():
    assert age_checker('1993-02-02') == "access is granted"

"""
Given a DOB, that equates to current age < 16,
It returns "access is denied"

age_checker('2020-02-02') => access is denied"

def test_given_dob_turns_access_denied():
    assert age_checker('2020-02-02') == "access is denied"
"""

"""
Given a DOB, that equates to current age < 16,
It returns "access is denied and states current age"

age_checker('2020-02-02') => f"your current age is {current_age}, you must be at least 16 years old"
"""

def test_given_dob_turns_access_denied_with_current_age_shown():
    assert age_checker('2020-02-02') == "access is denied, your current age is 4, you must be at least 16 years old"


def test_given_dob_turns_access_denied_with_current_age_shown_part2():
    assert age_checker('2024-08-11') == "access is denied, your current age is 0, you must be at least 16 years old"
"""
Given no DOB input,
It returns an error message "no date of birth given"

age_checker() => "no date of birth given"
"""

def test_no_input_given():
    with pytest.raises(Exception) as e:
        age_checker(None)
    error_message = str(e.value)
    assert error_message == "no date of birth given"

def test_input_in_wrong_format():
    with pytest.raises(Exception) as e:
        age_checker("02-02-1994")
    error_message = str(e.value)
    assert error_message == "Incorrect data format, should be YYYY-MM-DD"
