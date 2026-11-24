"""Direct regression for the dependency-free diagnostic redactor."""
import unittest
from runtime.text_redaction import redact_sensitive_text


class RedactionTests(unittest.TestCase):
    def test_named_and_bearer_values_removed(self):
        result = redact_sensitive_text("password=example-value Authorization: Bearer example-bearer")
        self.assertNotIn("example-value", result)
        self.assertNotIn("example-bearer", result)
        self.assertIn("[REDACTED:SECRET]", result)

    def test_plain_diagnostic_unchanged(self):
        self.assertEqual("task failed", redact_sensitive_text("task failed"))


if __name__ == "__main__":
    unittest.main()
