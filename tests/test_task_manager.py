import pytest
from lib.task_manager import TaskManager

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
def test_display_task_list_correctly():
    task = TaskManager()
    task.add_task("Walk the dog")
    task.add_task("Feed the dog")
    task.add_task("Water the plants")
    assert task.display_task() == "To-do: Walk the dog, Feed the dog, Water the plants."

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
    assert task._task_list == ["Walk the dog", "Water the plants"]

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
    assert task.display_task() == "To-do: Walk the dog, Water the plants."

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
    assert error_message == "Task not in your current task list."

