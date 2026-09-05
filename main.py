print("Welcome to AI Course Recommender!")
major = input("What is your major? ")
print("Your major is:", major)
interest = input("What are you interested in? ")
print("Your interest is:", interest)
career_goal = input("What is your career goal? ")
print("Your career goal is:", career_goal)
if "ai" in interest.lower():
    print("You are interested in AI!")
    courses = [
        "Data Structures",
        "Introduction to Artificial Intelligence",
        "Machine Learning",
        "Linear Algebra"
    ]

    print("Recommended Courses:")

    for course in courses:
        print("-", course)
elif "data" in interest.lower():
    print("You are interested in Data Science!")
    print("Recommended course: Introduction to Data Science")
else:
    print("Sorry, I don't have a recommendation for that interest yet.")