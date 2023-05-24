# Jesus Carlos Martinez Gonzalez
# 23/05/2023
# Exercise Tracker

from exercise_tracker import ExerciseSession


def test_get_exercise():
    ex = ExerciseSession("one", "Low", 0)
    assert ex.get_exercise() == "one"


def test_get_intensity():
    ex = ExerciseSession("one", "Low", 0)
    assert ex.get_intensity() == "Low"


def test_get_duration():
    ex = ExerciseSession("one", "Low", 0)
    assert ex.get_duration() == 0


def test_set_exercise():
    ex = ExerciseSession("one", "Low", 0)
    ex.set_exercise("two")
    assert ex.get_exercise() == "two"


def test_set_intensity():
    ex = ExerciseSession("one", "Low", 0)
    ex.set_intensity("Moderate")
    assert ex.get_intensity() == "Moderate"


def test_set_duration():
    ex = ExerciseSession("one", "Low", 0)
    ex.set_duration(10)
    assert ex.get_duration() == 10
