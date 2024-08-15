# {improve grammer} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

*Include the name of the function, its parameters, return value, and side effects.*

```python
# EXAMPLE

today = datetime.now()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


def grammer_checker(mixed_words):
    """clarify whether a text starts with a capaital letter and ends with suitable punctuation mark.

    Parameters: text (string)
        

    Returns: String to verify if text started with capital letter and ended with punctuation.
        If no capital letter and no punc mark = "Does text start with capital letter: No. Does text end with punctuation mark: No."

        If yes capital letter but no end to punctuation mark = "Does text start with capital letter: Yes. Does text end with punctuation mark: No."

        If no capital letter but yes ends with punctuation mark = "Does text start with capital letter: No. Does text end with punctuation mark: Yes."

        If has both = "Well done. Text starts with a capital letter and ends with a suitable punctuation mark."

        If no text = raise exception "There is no text to verify."

    Side effects: None
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

*Make a list of examples of what the function will take and return.*

```python
# EXAMPLE

"""
Given a string with capital and punc mark
It returns grammer is ok
"""
grammer_checker("Hello world.") => ["Well done. Text starts with a capital letter and ends with a suitable punctuation mark."]

"""
Given a string that starts with a capital and no punc mark
It returns a string to improve grammer.
"""
grammer_checker("Hello world") => "Does text start with capital letter: Yes. Does text end with punctuation mark: No."


"""
Given a string that starts with no capital but ends with a punc mark
It returns a string to improve grammer.
"""
grammer_checker("hello world!") => "Does text start with capital letter: No. Does text end with punctuation mark: Yes."


"""
Given a string that starts with no capital and doesn't ends with a punc mark
It returns a string to improve grammer.
"""
grammer_checker("hello world") => "Does text start with capital letter: No. Does text end with punctuation mark: No."


"""
Given an empty string
It returns an error
"""
grammer_checker("") => "There is no text to verify."

```

*Encode each example as a test. You can add to the above list as you go.*

## 4. Implement the Behaviour

*After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.*

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!