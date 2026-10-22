
def validate_student(name, marks):
    """Validate a student's name and marks."""
    name = name.strip()

    if not name:
        raise ValueError("Student name cannot be empty.")

    try:
        marks = float(marks)
    except (ValueError, TypeError):
        raise ValueError(f"Marks must be numeric for {name}.")

    if not 0 <= marks <= 100:
        raise ValueError(f"Marks must be between 0 and 100 for {name}.")

    return {"name": name, "marks": marks}
