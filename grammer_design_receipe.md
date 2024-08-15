
# {Grammer Stats} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem



## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

# **** REUSE SOME CODE ***** #

class GrammarStats():
    def __init__(self):
        # store sentence after check
        pass

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        pass

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
No string is given
Raise exception error
"""
def test_no_string_to_check():
    sentence = GrammarStats()
    with pytest.raises(Exception) as e:
        sentence.check("")
    error_message = str(e.value)
    assert error_message == "Unable to check grammer as no sentence was given."


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
Given a string that starts with a capital letter but doesn't end with suitable punctuation
Returns False
"""
def test_given_string_ends_without_punctuation():
    sentence = GrammarStats()
    assert sentence.check("Hello World") == False

"""
Given a string that starts without a capital letter and doesn't end with suitable punctuation
Returns False
"""
def test_given_string_ends_without_punctuation():
    sentence = GrammarStats()
    assert sentence.check("hello world") == False


"""
Checks the sentence for the percentage that passed
Returns an int percentage that passed the check
Example - 55% passed
"""
def test_check_pass_percentage_of_sentence
    sentence = GrammarStats()
    sentence.percentage_good(self.sentence)

"""
No string/sentence to check over 
Raise exception error
"""
def test_no_string_to_check():
    sentence = GrammarStats()
    with pytest.raises(Exception) as e:
        sentence.percentage_good(self.text)
    error_message = str(e.value)
    assert error_message == "Unable to check percentage pass rate as no sentence was given."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
