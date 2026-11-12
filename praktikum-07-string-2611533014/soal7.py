# Name: Nabila Tasmayeni
# NIM: 2611533014
# Question 7


name = "nabila tasmayeni"
nim = "2611533014"

space = name.find(" ")
first_name = name if space == -1 else name[:space]
username = first_name + nim[-3:]
intake = "20" + nim[:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)
