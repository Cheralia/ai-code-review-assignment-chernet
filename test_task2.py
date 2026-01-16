import unittest
from correct_task2 import count_valid_emails

class TestCountValidEmails(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_valid_emails([]), 0)

    def test_all_valid_emails(self):
        emails = ["test@example.com", "user.name@domain.co", "a@b.org"]
        self.assertEqual(count_valid_emails(emails), 3)

    def test_all_invalid_emails(self):
        emails = ["test@", "@example.com", "example.com", "a@", "@", " "]
        self.assertEqual(count_valid_emails(emails), 0)

    def test_mixed_emails(self):
        emails = ["valid@example.com", "invalid@", "@invalid.com", "also.valid@site.org"]
        self.assertEqual(count_valid_emails(emails), 2)

    def test_non_string_inputs(self):
        emails = ["valid@example.com", None, 123, ["list"], {"dict": "value"}]
        self.assertEqual(count_valid_emails(emails), 1)

    def test_whitespace_handling(self):
        emails = [" valid@example.com ", "user@domain.com"]
        self.assertEqual(count_valid_emails(emails), 1)

if __name__ == "__main__":
    unittest.main()
