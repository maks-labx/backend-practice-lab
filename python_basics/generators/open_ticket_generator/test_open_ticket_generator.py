import unittest
from types import GeneratorType

from open_ticket_generator import get_open_tickets


class OpenTicketGeneratorTests(unittest.TestCase):
    def test_returns_only_open_tickets(self):
        tickets = [
            {"id": 1, "status": "open"},
            {"id": 2, "status": "closed"},
            {"id": 3, "status": "open"},
        ]

        result = list(get_open_tickets(tickets))

        self.assertEqual(
            result,
            [
                {"id": 1, "status": "open"},
                {"id": 3, "status": "open"},
            ],
        )

    def test_returns_empty_list_when_no_open_tickets(self):
        tickets = [
            {"id": 1, "status": "closed"},
            {"id": 2, "status": "closed"},
        ]

        result = list(get_open_tickets(tickets))

        self.assertEqual(result, [])

    def test_function_returns_generator(self):
        tickets = [
            {"id": 1, "status": "open"},
        ]

        result = get_open_tickets(tickets)

        self.assertIsInstance(result, GeneratorType)


if __name__ == "__main__":
    unittest.main()