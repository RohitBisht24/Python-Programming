import random


questions = [
    {
        "question": "What is the file extension of Python files?",
        "options": {
            "a": ".java",
            "b": ".py",
            "c": ".html",
            "d": ".cpp"
        },
        "answer": "b"
    },
    {
        "question": "Who created Python?",
        "options": {
            "a": "Guido van Rossum",
            "b": "Dennis Ritchie",
            "c": "James Gosling",
            "d": "Mark Zuckerberg"
        },
        "answer": "a"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": {
            "a": "show()",
            "b": "display()",
            "c": "print()",
            "d": "output()"
        },
        "answer": "c"
    },
    {
        "question": "Which brackets are used to create a list in Python?",
        "options": {
            "a": "()",
            "b": "[]",
            "c": "{}",
            "d": "<>"
        },
        "answer": "b"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "a": "//",
            "b": "/* */",
            "c": "#",
            "d": "--"
        },
        "answer": "c"
    },
    {
        "question": "Which function is used to take input from the user?",
        "options": {
            "a": "input()",
            "b": "scan()",
            "c": "get()",
            "d": "read()"
        },
        "answer": "a"
    },
    {
        "question": "Which brackets are used to create a dictionary in Python?",
        "options": {
            "a": "[]",
            "b": "()",
            "c": "{}",
            "d": "<>"
        },
        "answer": "c"
    },
    {
        "question": "Python is a:",
        "options": {
            "a": "Low-level language",
            "b": "High-level language",
            "c": "Machine language",
            "d": "Assembly language"
        },
        "answer": "b"
    },
    {
        "question": "How do you write a string in Python?",
        "options": {
            "a": "Inside single or double quotes",
            "b": "Inside square brackets only",
            "c": "Using numbers only",
            "d": "Inside semicolons"
        },
        "answer": "a"
    },
    {
        "question": "Which keyword is used for a loop in Python?",
        "options": {
            "a": "repeat",
            "b": "loop",
            "c": "for",
            "d": "again"
        },
        "answer": "c"
    }
]


def start_quiz():
    score = 0

    # Shuffle questions each time the game starts
    random.shuffle(questions)

    print("\n" + "=" * 40)
    print("        WELCOME TO THE PYTHON QUIZ")
    print("=" * 40)

    for number, item in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {item['question']}")

        for key, value in item["options"].items():
            print(f"{key}) {value}")

        while True:
            user_answer = input(
                "\nEnter your answer (a/b/c/d): ").lower().strip()

            if user_answer in ["a", "b", "c", "d"]:
                break

            print("Invalid input. Please enter only a, b, c, or d.")

        if user_answer == item["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            correct_option = item["answer"]
            correct_answer = item["options"][correct_option]
            print(
                f"Wrong! ❌ The correct answer is: {correct_option}) {correct_answer}")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 40)
    print("              QUIZ RESULT")
    print("=" * 40)
    print(f"Your score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent work! 🌟")
    elif percentage >= 50:
        print("Good job! Keep practicing. 👍")
    else:
        print("Keep practicing and try again. 💪")


while True:
    start_quiz()

    play_again = input(
        "\nDo you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("\nThank you for playing. Goodbye! 👋")
        break
