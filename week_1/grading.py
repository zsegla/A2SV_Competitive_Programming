# https://www.hackerrank.com/challenges/grading/problem



def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade >= 38:
            modulo = grade % 5
            if modulo >= 3:
                grade += (5 - modulo)
        result.append(grade)
    return result
