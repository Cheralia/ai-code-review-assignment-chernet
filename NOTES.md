# Notes 
This file provides additional context and assumptions for the reviewer that do not fit cleanly in `submission_template.md`.

---

## Task 1 — Average Order Value
- Assumption: Orders without a `"status"` key are treated as valid (non-cancelled) orders.
- Known limitation: Orders with non-numeric `"amount"` values that cannot be converted to float are ignored, rather than raising an error.
- Alternative considered: Raising an exception for invalid amounts, but skipped to maintain robustness in real-world datasets.

---

## Task 2 — Count Valid Emails
- Assumption: Simple regex validation is sufficient; we do not strictly enforce full RFC 5322 compliance.
- Known limitation: Emails with unusual but technically valid formats (e.g., quotes, comments) may be rejected.
- Alternative considered: Using the `email` standard library (`email.utils.parseaddr`) for stricter validation, but regex was chosen for simplicity and readability.

---
