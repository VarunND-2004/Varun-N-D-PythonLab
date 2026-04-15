import re
data = "Email: test123@gmail.com, backup: user456@yahoo.com"

start_check = re.match(r"Email", data)
print("Starts with Email" if start_check else "No start match")


email = re.search(r"\w+@\w+\.\w+", data)
print("First email found:", email.group() if email else "None")


all_emails = re.findall(r"\w+@\w+\.\w+", data)
print("All emails:", all_emails)


for e in re.finditer(r"\w+@\w+\.\w+", data):
    print("Email:", e.group(), "| Position:", e.start(), "-", e.end())


parts = re.split(r"[ ,]+", data)
print("Split parts:", parts)


hidden = re.sub(r"\w+(?=@)", "***", data)
print("Hidden emails:", hidden)