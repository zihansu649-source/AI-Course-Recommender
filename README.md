# AI Course Recommender

A Python-based course recommendation system that suggests courses based on a student's major, interests, career goals, and preferred difficulty level.

## Features

- Collects user information including major, interests, career goals, and preferred difficulty
- Stores course information using Python dictionaries and lists
- Matches user interests and career goals with course keywords
- Uses a scoring system to rank courses
- Returns the top 3 course recommendations

## Technologies

- Python
- Git
- GitHub

## How It Works

Each course contains:
- Name
- Category
- Difficulty
- Keywords

The recommendation score is calculated based on:
- Interest match
- Career goal match
- Difficulty match

Courses are ranked by their scores, and the top 3 recommendations are displayed.

## Example

Input:

```text
Major: BAIT
Interest: AI
Career Goal: AI Engineer
Difficulty: Beginner
```

Output:

```text
Top Recommendations:
- Machine Learning
- Python Programming
- Data Structures
```

## Future Improvements

- Add more courses and majors
- Use real university course data
- Improve the recommendation algorithm
- Add a web interface
- Explore machine learning-based recommendations