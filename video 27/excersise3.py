import random

# Questions and answers stored as lists of tuples
questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What is the largest mammal in the world?", "Blue Whale"),
    ("In which year did World War II end?", "1945")
]

# Prize money for each question
prizes = [1000, 5000, 10000, 50000, 100000]

def play_game():
    total_prize = 0
    
    print("Welcome to the KBC-style Quiz Game!")
    print("Answer 5 questions correctly to win 100,000!")
    
    for i, (question, correct_answer) in enumerate(questions):
        print(f"\nQuestion {i+1} for ${prizes[i]}:")
        print(question)
        
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            total_prize = prizes[i]
            print(f"Correct! You've won ${total_prize}!")
        else:
            print(f"Sorry, that's incorrect. The correct answer was {correct_answer}.")
            print(f"Game over. You're taking home ${total_prize}.")
            return total_prize
    
    print("\nCongratulations! You've won the maximum prize!")
    return total_prize

def main():
    final_prize = play_game()
    print(f"\nThank you for playing! You're taking home ${final_prize}.")

if __name__ == "__main__":
    main()