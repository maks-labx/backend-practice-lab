import unittest

from problem_ticket_iterator import ProblemTicketIterator


class ProblemTicketIteratorTests(unittest.TestCase):
    def test_iterates_only_over_problem_tickets(self):
        tickets = [
            {"id": 1, "status": "OK"},
            {"id": 2, "status": "PROBLEM"},
            {"id": 3, "status": "PROBLEM"},
        ]

        result = list(ProblemTicketIterator(tickets))

        self.assertEqual(
            result,
            [
                {"id": 2, "status": "PROBLEM"},
                {"id": 3, "status": "PROBLEM"},
            ],
        )

    def test_returns_empty_list_when_no_problem_tickets(self):
        tickets = [
            {"id": 1, "status": "OK"},
            {"id": 2, "status": "OK"},
        ]

        result = list(ProblemTicketIterator(tickets))

        self.assertEqual(result, [])

    def test_empty_input_returns_empty_list(self):
        result = list(ProblemTicketIterator([]))

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()