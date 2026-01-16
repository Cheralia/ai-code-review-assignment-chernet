# AI Code Review Assignment (Python)

## Candidate
- Name: Chernet Erdachew
- Approximate time spent:

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
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
