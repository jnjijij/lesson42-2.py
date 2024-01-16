import re

input_file = "вихідний_файл.txt"
output_file = "новий_файл.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

gmail_emails = []
for line in lines:
    match = re.search(r"\b[A-Za-z0-9._%+-]+@gmail.com\b", line)
    if match:
        gmail_emails.append(match.group())

with open(output_file, "w") as file:
    for email in gmail_emails:
        file.write(email + "\n")
