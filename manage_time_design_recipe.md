# {Manage time} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def manage_time(text):
    # Params: Take given text (string), words_per_min (int)
    # Returns: Time it takes to read text (int) (use f string to print out time?)
    # Side-effect: None
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given text AND how many words read per minute
Returns text as string and number of words per min
"""
manage_time("walk the dogs today") == "walk the dogs today", 200

"""
Given a text as string
Returns how many words are in the text
"""

manage_time("walk the dogs today") == 4 words

"""
Given how 10 words in text
Returns calcuation how many seconds it takes to read 10 words based of 200 words per min
"""
manage_time("walk the dogs today and train them and feed them") == 3 seconds

"""
Given how 200 words in text
Returns calcuation how many minutes > which should be 1  
"""
manage_time("hello" * 200) == 60 seconds or 1 minute

"""
Given how 300 words in text
Returns calcuation how many minutes > which should be 1  
"""
manage_time("hello" * 200, 200) == "It should take you 1 minute 30 seconds"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

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
