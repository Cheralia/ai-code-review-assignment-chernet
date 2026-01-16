# AI Code Review Assignment (Python)

## Candidate
- Name: Chernet Erdachew
- Approximate time spent: 50 minute

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Divides by total number of orders, including cancelled ones, leading to incorrect averages.
- Raises ZeroDivisionError when input list is empty or when all orders are cancelled.

### Edge cases & risks
- Orders with missing or non-numeric "amount" values cause runtime errors.
- Orders missing the "status" key are not handled safely.

### Code quality / design issues
- No validation or error handling.
- Poor variable naming (`count` vs. actual number of valid orders).

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only non-cancelled orders.
- Safely handle missing or invalid data.
- Avoid division by zero.
- Use float conversion defensively.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
To ensure `calculate_average_order_value` works correctly and safely in all realistic scenarios, I would focus on the following areas:
- Empty list input: Confirm the function handles empty datasets without crashing and returns 0.0 as expected.
- All orders cancelled: Ensure cancelled orders are excluded and the average correctly returns 0.0.
- Mixed valid and invalid amounts: Verify that only non-cancelled orders are counted and the average is correct.
- Orders with missing "status" key: Confirm that orders missing the "status" key are treated as valid, preventing KeyError crashes.
- Orders with invalid "amount" values: Ensure the function safely ignores non-numeric amounts without crashing.
- Orders with floating-point amounts: Confirm that float amounts are handled correctly in the average calculation.

see `test_task1.py`


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Claims correctness while dividing by total orders instead of valid orders.
- Does not mention error cases or invalid data handling.

### Rewritten explanation
- This function computes the average value of all non-cancelled orders by summing their valid numeric amounts and dividing by the count of such orders. It safely handles empty inputs, missing fields, and invalid data, returning 0.0 when no valid orders exist.

## 4) Final Judgment
- Decision: Request Changes
- Justification: Original implementation produces incorrect results and can crash on valid inputs.
- Confidence & unknowns: High confidence after fixes; no major unknowns.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Treats any string containing "@" as a valid email, which is incorrect.

### Edge cases & risks
- Accepts invalid formats like "@", "a@", "@b", or "a@b".
- Does not handle non-string inputs.

### Code quality / design issues
- Lacks validation logic.
- No input type checking

## 2) Proposed Fixes / Improvements
### Summary of changes
- Use a regular expression to validate email format.
- Ignore non-string values.
- Handle empty input safely.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
- Empty list: Confirm the function returns 0 without crashing when no emails are provided.
- All valid emails: Verify the function correctly counts all valid emails.
- All invalid emails: Ensure the function correctly ignores invalid email formats and returns 0.
- Mixed valid and invalid emails: Confirm that only valid emails are counted, ignoring invalid ones.
- Non-string inputs: Check that the function safely ignores non-string types without crashing.
- Emails with leading/trailing whitespace: Verify that improperly formatted emails with whitespace are treated as invalid, maintaining strict validation.

see `test_task2.py`

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Incorrectly claims validity checking is done.
- Overstates safety and correctness.

### Rewritten explanation
- This function counts the number of syntactically valid email addresses in the input list using a regular expression. It safely ignores invalid formats, non-string values, and handles empty input by returning 0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: Original logic is fundamentally incorrect for email validation.
- Confidence & unknowns: High confidence after regex-based fix.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Divides by total input length instead of count of valid values.
- Raises ZeroDivisionError when input is empty or all values are None.
- Crashes on non-numeric, non-None values.

### Edge cases & risks
- Mixed types (e.g., strings, objects).
- Empty list input.

### Code quality / design issues
- No defensive programming.
- Misleading variable naming (`count` vs. valid count).

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only valid numeric values.
- Use try/except for safe float conversion.
- Return 0.0 if no valid values exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
- Empty input list: Confirm the function returns 0.0 without crashing when no measurements are provided.
- All None values: Verify that None values are ignored and the function correctly returns 0.0 when no valid measurements exist.
- All valid numeric values: Ensure the average is calculated correctly with all valid numeric inputs.
- Mixed valid numbers and None: Confirm that None values are ignored and only valid numbers are averaged.
- String representations of numbers: Check that numeric strings are correctly converted to float and included in the average.
- Invalid non-numeric values: Ensure invalid values are skipped without causing crashes.
- Negative numbers and zeros: Confirm the function correctly handles negative numbers and zero in the average calculation.

see `test_task3.py`


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Function does not actually handle mixed types safely.
- Average calculation is incorrect when None values are present.

### Rewritten explanation
- This function computes the average of all valid numeric measurements by ignoring None values and safely converting numeric inputs to floats. It handles mixed input types gracefully and returns 0.0 when no valid values are present.

## 4) Final Judgment
- Decision: Request Changes
- Justification: Original implementation is incorrect and unsafe for common inputs.
- Confidence & unknowns: High confidence after corrections.
