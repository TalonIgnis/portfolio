user_name = input("what is your name: \n")

print("welcome " +user_name+ ".")

def run_quiz():
    quiz = {
        "When was dnd first published?": {
            "options": ["A. 1974", "B. 1978 ", "C. 1982", "D. 1994"],
            "correct": "A"
        },
        "Who was the first Dungeon Master?": {
            "options": ["A. Dave Arneson", "B. Dave stevens", "C. Anrnalod Jackson", "D. Francis Travian"],
            "correct": "A"
        },
        "Which of these is not a core class?": {
            "options": ["A. Wizard", "B. Artificer", "C. Warlock", "D. Ranger"],
            "correct": "B"
        },
        "Which of these is not a first level spell?": {
            "options": ["A. Magic Missile", "B. Shield", "C. Heat metal", "D. Ceremony"],
            "correct": "C"
        },
        "Which of these classes is not a full caster?": {
            "options": ["A. Wizard", "B. Bard", "C. Cleric", "D. Warlock"],
            "correct": "D"
        }
    }

    score = 0
    
    for question, data in quiz.items():
        print(f"\n{question}")
        for option in data["options"]:
            print(option)
        
        user_answer = input("Please enter your answer (A, B, C, D): ").strip().upper()
        
        while user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please choose A, B, C, or D.")
            user_answer = input("Please enter your answer (A, B, C, D): ").strip().upper()
        
        if user_answer == data["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {data['correct']}.")
    
    print(f"\nYour final score is {score}/{len(quiz)}.")


run_quiz()