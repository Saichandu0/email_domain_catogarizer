import re

def group_emails_by_domain(emails):
    domains = {}

    for k in emails:
        match = re.search(r'@([\w.-]+)', k)
        if match:
            domain = match.group(1)
            if domain not in domains:
                domains[domain] = []
            domains[domain].append(k)

    for k in domains:
        print(f"Emails from domain '{k}':")
        for email in domains[k]:
            print(email)


emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com", "dave@outlook.com"]
group_emails_by_domain(emails)
