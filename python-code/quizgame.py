def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    user_answer = input("Enter the number of your answer: ")
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False
    else:
        print("Please enter a number.")
        return False

def play_quiz():
    questions = [
        ("What is the capital of France?", ["Paris", "London", "Berlin"], 1),
        ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], 1),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe"], 2),
        ("What is Ryans favourite fruit?", ["Apple", "Banana", "Orange"], 3)
    ]

    score = 0
    for question, options, correct_answer in questions:
        if ask_question(question, options, correct_answer):
            score += 1
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    play_quiz()
