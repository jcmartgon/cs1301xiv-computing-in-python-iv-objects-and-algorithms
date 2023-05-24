# Jesus Carlos Martinez Gonzalez
# 23/05/2023
# Calories Burned

from exercise_tracker import ExerciseSession


def test_low():
    ex = ExerciseSession("one", "Low", 10)
    assert ex.calories_burned() == 40


def test_medium():
    ex = ExerciseSession("one", "Medium", 10)
    assert ex.calories_burned() == 80


def test_high():
    ex = ExerciseSession("one", "High", 10)
    assert ex.calories_burned() == 120
