def find_duplicate_emails(emails):
    seen = set()
    duplicates = set()

    for email in emails:
        normalized_email = email.strip().lower()

        if not normalized_email:
            continue

        if normalized_email in seen:
            duplicates.add(normalized_email)
        else:
            seen.add(normalized_email)

    return sorted(duplicates)
