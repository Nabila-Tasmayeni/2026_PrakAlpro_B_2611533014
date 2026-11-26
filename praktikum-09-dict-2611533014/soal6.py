schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}
#6a
busiest_day = ""
most_courses = 0

for day, courses in schedule.items():
    if len(courses) > most_courses:
        busiest_day = day
        most_courses = len(courses)

print("Busiest day:", busiest_day,
      "(" + str(most_courses) + " courses)")

#6b

course = input("Course: ")

count = 0

for day, courses in schedule.items():
    if course in courses:
        count = count + 1

print(course + ":", count, "days")
