courses = [
    {
        "name": "Data Structures",
        "category": "Computer Science",
        "difficulty": "Intermediate"
    },
    {
        "name": "Machine Learning",
        "category": "Artificial Intelligence",
        "difficulty": "Advanced"
    },
    {
        "name": "Python Programming",
        "category": "Computer Science",
        "difficulty": "Beginner"
    }
]
for c in courses:
    print("Course:", c["name"])
    print("Category:", c["category"])
    print("Difficulty:", c["difficulty"])
    print()

print("Welcome to AI Course Recommender!")
major = input("What is your major? ")
print("Your major is:", major)
interest = input("What are you interested in? ")
print("Your interest is:", interest)
career_goal = input("What is your career goal? ")
print("Your career goal is:", career_goal)
difficulty = input("What difficulty do you prefer? ").strip()
print("Your preferred difficulty is:", difficulty)
print("Courses matching your difficulty:")

for c in courses:
    if c["difficulty"].lower() == difficulty.lower():
        print("-", c["name"])
if "ai" in interest.lower() or "ai" in career_goal.lower():
    print("You are interested in AI!")

    if "bait" in major.lower():
        print("Since you are a BAIT student, I recommend building your CS foundation first.")
        courses = [
        "Data Structures",
        "Introduction to Artificial Intelligence",
        "Machine Learning",
        "Linear Algebra"
    ]
    else:
        courses = [
        "Introduction to Artificial Intelligence",
        "Machine Learning",
        "Python Programming"
    ]

    print("Recommended Courses:")

    for course in courses:
        print("-", course)
elif "data" in interest.lower() or "data" in career_goal.lower():
    print("You are interested in Data Science!")

    courses = [
        "Introduction to Data Science",
        "Statistics",
        "Python Programming",
        "Database Management"
    ]

    print("Recommended Courses:")

    for course in courses:
        print("-", course)
else:
    print("Sorry, I don't have a recommendation for that interest yet.")