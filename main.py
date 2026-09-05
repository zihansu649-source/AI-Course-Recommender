courses = [
    {
        "name": "Data Structures",
        "category": "Computer Science",
        "difficulty": "Intermediate",
        "keywords": ["data structures", "algorithms", "programming", "computer science"]
    },
    {
        "name": "Machine Learning",
        "category": "Artificial Intelligence",
        "difficulty": "Advanced",
        "keywords": ["ai", "machine learning", "data", "python"]
    },
    {
        "name": "Python Programming",
        "category": "Computer Science",
        "difficulty": "Beginner",
        "keywords": ["python", "programming", "coding", "beginner"]
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
        print("Courses matching your interest:")

scored_courses = []

for c in courses:
    score = 0

    if interest.lower() in c["keywords"]:
        score = score + 1

    if c["difficulty"].lower() == difficulty.lower():
        score = score + 1

    for keyword in c["keywords"]:
        if keyword in career_goal.lower():
            score = score + 1
            break

    scored_courses.append({
        "name": c["name"],
        "score": score
    })
scored_courses.sort(key=lambda x: x["score"], reverse=True)

print("Top Recommendations:")

for course in scored_courses[:3]:
    print("-", course["name"], "Score:", course["score"])
