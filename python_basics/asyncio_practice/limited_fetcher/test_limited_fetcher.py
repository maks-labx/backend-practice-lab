import unittest

from limited_fetcher import fetch_page, fetch_pages_with_limit


class LimitedFetcherTests(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_page_returns_page_data(self):
        result = await fetch_page("https://example.com")

        self.assertEqual(
            result,
            {
                "url": "https://example.com",
                "status": "ok",
            },
        )

    async def test_fetch_pages_with_limit_returns_all_pages(self):
        urls = [
            "https://example.com",
            "https://python.org",
            "https://github.com",
        ]

        result = await fetch_pages_with_limit(urls, limit=2)

        self.assertEqual(
            result,
            [
                {"url": "https://example.com", "status": "ok"},
                {"url": "https://python.org", "status": "ok"},
                {"url": "https://github.com", "status": "ok"},
            ],
        )

    async def test_fetch_pages_with_limit_returns_empty_list(self):
        result = await fetch_pages_with_limit([], limit=2)

        self.assertEqual(result, [])

    async def test_invalid_limit_raises_error(self):
        with self.assertRaises(ValueError):
            await fetch_pages_with_limit(["https://example.com"], limit=0)


if __name__ == "__main__":
    unittest.main()
