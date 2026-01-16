import re

def count_valid_emails(emails):
    """
    Count the number of syntactically valid email addresses.

    Args:
        emails (list): A list of email strings.

    Returns:
        int: The number of valid email addresses.
    """
    if not emails:
        return 0

    # Simple RFC 5322-compliant email pattern 
    pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    count = 0
    for email in emails:
        if isinstance(email, str) and pattern.match(email):
            count += 1

    return count
