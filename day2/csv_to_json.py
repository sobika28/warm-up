
import csv
import json
from pathlib import Path
from validators import validate_student

folder = Path(__file__).parent
csv_file = folder / "students.csv"
json_file = folder / "summary.json"


def main():
    students = []

    try:
        with open(csv_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or not {"name", "marks"}.issubset(
                reader.fieldnames
            ):
                raise ValueError("CSV must contain name and marks columns.")

            for line_number, row in enumerate(reader, start=2):
                try:
                    student = validate_student(
                        row.get("name"), row.get("marks")
                    )
                    students.append(student)
                except ValueError as error:
                    print(f"Skipping row {line_number}: {error}")

        if not students:
            raise ValueError("No valid student records found.")

        average = sum(s["marks"] for s in students) / len(students)
        topper = max(students, key=lambda s: s["marks"])

        summary = {
            "total_students": len(students),
            "average_marks": round(average, 2),
            "topper": topper["name"],
            "topper_marks": topper["marks"],
            "students": students
        }

        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(summary, file, indent=4)

        print("Summary created successfully!")
        print(f"Average marks: {average:.2f}")
        print(f"Topper: {topper['name']} ({topper['marks']})")

    except FileNotFoundError:
        print(f"Error: Could not find {csv_file.name}.")
    except (OSError, csv.Error, ValueError) as error:
        print(f"Error: {error}")
    finally:
        print("CSV processing finished.")


if __name__ == "__main__":
    main()
