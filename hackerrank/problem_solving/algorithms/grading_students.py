#!/bin/python

def grading_students(grades):

    rounded = []

    for grade in grades:

        next_mult_5 = ((grade // 10) * 10) + (5 - (grade % 10) + (grade % 10))

        if grade < 38:
            rounded.append(grade)
        elif next_mult_5 - grade < 3:
            rounded.append(next_mult_5)
        else:
            rounded.append(grade)

    print rounded


if __name__ == "__main__":
    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    grading_students(grades)