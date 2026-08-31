import unittest

from student_grades import StudentGrades


class StudentGradesTests(unittest.TestCase):
    def test_creates_student_with_name(self):
        student = StudentGrades("Max")

        self.assertEqual(student.student_name, "Max")
        self.assertEqual(student.grades, [])

    def test_strips_student_name(self):
        student = StudentGrades(" Max ")

        self.assertEqual(student.student_name, "Max")

    def test_add_grade_adds_grade_to_list(self):
        student = StudentGrades("Max")

        student.add_grade(90)

        self.assertEqual(student.grades, [90])

    def test_get_average_grade_returns_average(self):
        student = StudentGrades("Max")

        student.add_grade(80)
        student.add_grade(90)
        student.add_grade(100)

        self.assertEqual(student.get_average_grade(), 90)

    def test_get_average_grade_returns_zero_without_grades(self):
        student = StudentGrades("Max")

        self.assertEqual(student.get_average_grade(), 0)

    def test_has_passed_returns_true_when_average_is_enough(self):
        student = StudentGrades("Max")

        student.add_grade(70)
        student.add_grade(80)

        self.assertTrue(student.has_passed())

    def test_has_passed_returns_false_when_average_is_too_low(self):
        student = StudentGrades("Max")

        student.add_grade(40)
        student.add_grade(50)

        self.assertFalse(student.has_passed())

    def test_get_grade_count_returns_number_of_grades(self):
        student = StudentGrades("Max")

        student.add_grade(80)
        student.add_grade(90)

        self.assertEqual(student.get_grade_count(), 2)

    def test_invalid_grade_raises_error(self):
        student = StudentGrades("Max")

        with self.assertRaises(ValueError):
            student.add_grade(-1)

        with self.assertRaises(ValueError):
            student.add_grade(101)

        with self.assertRaises(ValueError):
            student.add_grade("90")

    def test_invalid_student_name_raises_error(self):
        with self.assertRaises(ValueError):
            StudentGrades("")

        with self.assertRaises(ValueError):
            StudentGrades("   ")

        with self.assertRaises(ValueError):
            StudentGrades(None)


if __name__ == "__main__":
    unittest.main()
