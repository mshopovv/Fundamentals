def grades(current_grade: float) -> str:
    result = ""
    if 2.00 <= current_grade <= 2.99:
        result = "Fail"
    elif 3.00 <= current_grade <= 3.49:
        result = "Poor"
    elif 3.50 <= current_grade <= 4.49:
        result = "Good"
    elif 4.50 <= current_grade <= 5.49:
        result = "Very Good"
    elif 5.50 <= current_grade <= 6.00:
        result = "Excellent"
    return result

grade = float(input())
grade_in_words = grades(grade)
print(grade_in_words)