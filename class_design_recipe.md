# {Task Tracker} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

nouns = tasks, program, focus, 
verbs = track, see a list, add, focus, mark, complete, disappear, 

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

"""
add tasks
see a list of tasks
Mark tasks as done and then remove them from the list (maybe present again to check)
"""


class TaskManager():
    # User-facing properties:
    #   name: string

    def __init__(self): # 1 test - set empty initialiser (list)
        # Parameters:
        #   None: 
        # Side effects:
        #   self.task list = Sets the name property of the self object list
        # AND sets empty list to store tasks
        pass # No code here yet

    def add_task(self, task): # 2 tests - added correctly, if not in correct format throws error
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object list (self.list)
        # Second Side-effect:
        #   Throws an exception if data type (not a string) is incorrect
        pass # No code here yet

    def display_task(self): # 2 tests - 1 for format, 1 for error
        # Returns:
        #   A string showing the tasks the user has in the task list
        # Side-effects:
        #   Throws an exception if no task has been stored
        pass # No code here yet

    def complete_task(self, task): # 2 tests - 1 removes task from list, 1 error if task doesn't match
        # Parameters:
        #   task: string which represents the task that's been completed
                # Returns:
                #   edge case: Maybe show a list of tasks to show which one to complete to help with spelling etc 
        # Side-effects:
        #   Removes completed task from self object list
        pass # No code here yet

##################          should be 8 tests             ###############
```
## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initialise class object
Check empty list has been initialised
"""
def test_initialise_object_with_empty_list():
    task = TaskManager()
    assert task._task_list == []

"""
Given a task
#check it's been added to task_list
"""
def test_add_task_to_task_manager():
    task = TaskManager()
    task.add_task("Walk the dog")
    assert task._task_list == ["Walk the dog"]

"""
Given task with incorrect data type 
#raise error 
"""
def test_add_task_with_empty_string_input():
    task = TaskManager()
    with pytest.raises(Exception) as e:
        task.add_task("")  # Empty string input
    error_message = str(e.value)
    assert error_message == "Unable to add task. Input must be a string"

"""
Display tasks
#return formatted string with tasks
"""
def test_display_tasks_correctly():
    task = TaskManager()
    task.add_task("Walk the dog")
    task.add_task("Feed the dog")
    task.add_task("Water the plants")
    assert task.dislpay_task() == "To-do: Walk the dog, Feed the dog, Water the plants."

"""
When called to display tasks but list is empty
#raise error 
"""
def test_raise_error_when_task_list_empty():
    task = TaskManager()
    with pytest.raises(Exception) as e:
        task.display_task()  # No tasks in list
    error_message = str(e.value)
    assert error_message == "No tasks to-do!"

"""
When a task has been compete
#check its been removed from task list
"""
def test_display_tasks_correctly():
    task = TaskManager()
    task.add_task("Walk the dog")
    task.add_task("Feed the dog")
    task.add_task("Water the plants")
    task.complete_task("Feed the dog")
    assert task.task_list == ["Walk the dog", "Water the plants"]

"""
When a task has been competed and removed
#returns correctly updated task list in formatted string 
"""
def test_display_tasks_correctly_after_removed_task():
    task = TaskManager()
    task.add_task("Walk the dog")
    task.add_task("Feed the dog")
    task.add_task("Water the plants")
    task.complete_task("Feed the dog")
    assert task.dislpay_task() == "To-do: Walk the dog, Water the plants."


"""
Given task isn't on the list/doesn't match any tasks
#raise error because given not on task list
"""
def test_raise_error_when_given_task_not_in_task_list():
    task = TaskManager()
    task.add_task("Walk the dog")
    task.add_task("Feed the dog")
    task.add_task("Water the plants")
    with pytest.raises(Exception) as e:
        task.complete_task("Take dog to the vet")  # Tasks in list
    error_message = str(e.value)
    assert error_message == "This task doesn't match any on your to-do list."

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
