class StudentGrades:
    def __init__(self, student_name):
        self.student_name = self._validate_name(student_name)
        self.grades = []

    def add_grade(self, grade):
        if not isinstance(grade, int):
            raise ValueError("Grade must be an integer")

        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")

        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def has_passed(self, passing_grade=60):
        return self.get_average_grade() >= passing_grade

    def get_grade_count(self):
        return len(self.grades)

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Student name must be a string")

        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError("Student name is required")

        return normalized_name
