import unittest

from problem_ticket_iterator import ProblemTicketIterator


class ProblemTicketIteratorTests(unittest.TestCase):
    def test_iterates_only_over_problem_tickets_by_default(self):
        tickets = [
            {"id": 1, "status": "OK", "priority": 1},
            {"id": 2, "status": "PROBLEM", "priority": 2},
            {"id": 3, "status": "PROBLEM", "priority": 3},
        ]

        result = list(ProblemTicketIterator(tickets))

        self.assertEqual(
            result,
            [
                {"id": 2, "status": "PROBLEM", "priority": 2},
                {"id": 3, "status": "PROBLEM", "priority": 3},
            ],
        )

    def test_can_filter_by_custom_status(self):
        tickets = [
            {"id": 1, "status": "OK", "priority": 1},
            {"id": 2, "status": "PROBLEM", "priority": 2},
            {"id": 3, "status": "OK", "priority": 3},
        ]

        result = list(ProblemTicketIterator(tickets, target_status="OK"))

        self.assertEqual(
            result,
            [
                {"id": 1, "status": "OK", "priority": 1},
                {"id": 3, "status": "OK", "priority": 3},
            ],
        )

    def test_can_filter_by_min_priority(self):
        tickets = [
            {"id": 1, "status": "PROBLEM", "priority": 1},
            {"id": 2, "status": "PROBLEM", "priority": 3},
            {"id": 3, "status": "PROBLEM", "priority": 5},
        ]

        result = list(ProblemTicketIterator(tickets, min_priority=3))

        self.assertEqual(
            result,
            [
                {"id": 2, "status": "PROBLEM", "priority": 3},
                {"id": 3, "status": "PROBLEM", "priority": 5},
            ],
        )

    def test_skips_tickets_without_status_key(self):
        tickets = [
            {"id": 1, "priority": 5},
            {"id": 2, "status": "PROBLEM", "priority": 2},
        ]

        result = list(ProblemTicketIterator(tickets))

        self.assertEqual(result, [{"id": 2, "status": "PROBLEM", "priority": 2}])

    def test_works_with_generator_input(self):
        tickets = (
            ticket
            for ticket in [
                {"id": 1, "status": "OK", "priority": 1},
                {"id": 2, "status": "PROBLEM", "priority": 2},
            ]
        )

        result = list(ProblemTicketIterator(tickets))

        self.assertEqual(result, [{"id": 2, "status": "PROBLEM", "priority": 2}])


if __name__ == "__main__":
    unittest.main()
