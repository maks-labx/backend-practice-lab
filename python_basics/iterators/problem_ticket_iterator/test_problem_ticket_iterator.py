import unittest

from problem_ticket_iterator import ProblemTicketIterator


class ProblemTicketIteratorTests(unittest.TestCase):
    def test_iterates_only_over_problem_tickets_by_default(self):
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

    def test_can_filter_by_custom_status(self):
        tickets = [
            {"id": 1, "status": "OK"},
            {"id": 2, "status": "PROBLEM"},
            {"id": 3, "status": "OK"},
        ]

        result = list(ProblemTicketIterator(tickets, target_status="OK"))

        self.assertEqual(
            result,
            [
                {"id": 1, "status": "OK"},
                {"id": 3, "status": "OK"},
            ],
        )

    def test_returns_empty_list_when_no_matching_tickets(self):
        tickets = [
            {"id": 1, "status": "OK"},
            {"id": 2, "status": "OK"},
        ]

        result = list(ProblemTicketIterator(tickets))

        self.assertEqual(result, [])

    def test_skips_tickets_without_status_key(self):
        tickets = [
            {"id": 1},
            {"id": 2, "status": "PROBLEM"},
        ]

        result = list(ProblemTicketIterator(tickets))

        self.assertEqual(result, [{"id": 2, "status": "PROBLEM"}])


if __name__ == "__main__":
    unittest.main()