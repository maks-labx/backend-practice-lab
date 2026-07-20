import unittest
from types import GeneratorType

from open_ticket_generator import get_tickets_by_status


class TicketGeneratorTests(unittest.TestCase):
    def test_returns_open_tickets_by_default(self):
        tickets = [
            {"id": 1, "status": "open", "priority": 1},
            {"id": 2, "status": "closed", "priority": 3},
            {"id": 3, "status": "open", "priority": 2},
        ]

        result = list(get_tickets_by_status(tickets))

        self.assertEqual(
            result,
            [
                {"id": 1, "status": "open", "priority": 1},
                {"id": 3, "status": "open", "priority": 2},
            ],
        )

    def test_can_filter_by_custom_status(self):
        tickets = [
            {"id": 1, "status": "open", "priority": 1},
            {"id": 2, "status": "closed", "priority": 3},
            {"id": 3, "status": "closed", "priority": 2},
        ]

        result = list(get_tickets_by_status(tickets, status="closed"))

        self.assertEqual(
            result,
            [
                {"id": 2, "status": "closed", "priority": 3},
                {"id": 3, "status": "closed", "priority": 2},
            ],
        )

    def test_can_filter_by_min_priority(self):
        tickets = [
            {"id": 1, "status": "open", "priority": 1},
            {"id": 2, "status": "open", "priority": 3},
            {"id": 3, "status": "open", "priority": 5},
        ]

        result = list(get_tickets_by_status(tickets, min_priority=3))

        self.assertEqual(
            result,
            [
                {"id": 2, "status": "open", "priority": 3},
                {"id": 3, "status": "open", "priority": 5},
            ],
        )

    def test_skips_tickets_without_status_key(self):
        tickets = [
            {"id": 1, "priority": 5},
            {"id": 2, "status": "open", "priority": 2},
        ]

        result = list(get_tickets_by_status(tickets))

        self.assertEqual(result, [{"id": 2, "status": "open", "priority": 2}])

    def test_returns_generator_object(self):
        tickets = [
            {"id": 1, "status": "open", "priority": 1},
        ]

        result = get_tickets_by_status(tickets)

        self.assertIsInstance(result, GeneratorType)


if __name__ == "__main__":
    unittest.main()