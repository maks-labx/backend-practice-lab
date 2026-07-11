import unittest

from ticket_iterator import TicketIterator


class TicketIteratorTests(unittest.TestCase):
    def test_iterates_over_all_tickets(self):
        tickets = ["ticket-1", "ticket-2", "ticket-3"]

        result = list(TicketIterator(tickets))

        self.assertEqual(result, ["ticket-1", "ticket-2", "ticket-3"])

    def test_empty_list_returns_empty_result(self):
        tickets = []

        result = list(TicketIterator(tickets))

        self.assertEqual(result, [])

    def test_next_returns_items_one_by_one(self):
        tickets = ["ticket-1", "ticket-2"]
        iterator = TicketIterator(tickets)

        self.assertEqual(next(iterator), "ticket-1")
        self.assertEqual(next(iterator), "ticket-2")

        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    unittest.main()
    