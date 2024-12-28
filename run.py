import re

email = "mark@example.comcom"

pattern = r"^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$"
p = re.compile(pattern, re.I or re.S)

m = p.search(email)

if not m: print("Не совпадает")
else: print("Совпадает")