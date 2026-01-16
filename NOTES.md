# Notes 
This file provides additional context and assumptions for the reviewer that do not fit cleanly in `submission_template.md`.

---

## Task 1 — Average Order Value
- Assumption: Orders without a `"status"` key are treated as valid (non-cancelled) orders.
- Known limitation: Orders with non-numeric `"amount"` values that cannot be converted to float are ignored, rather than raising an error.
- Alternative considered: Raising an exception for invalid amounts, but skipped to maintain robustness in real-world datasets.

---

