import random
from collections import defaultdict, deque

moves = ["rock", "paper", "scissors"]

winning_moves = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

user_history = deque([], maxlen=3)
history_model = defaultdict(lambda: defaultdict(int))

def ai_predict_move():
    if len(user_history) < 3:
        return random.choice(moves)
    state = tuple(user_history)
    next_moves = history_model[state]
    if not next_moves:
        return random.choice(moves)
    predicted_user_move = max(next_moves, key=next_moves.get)
    ai_move = winning_moves[predicted_user_move]
    return ai_move

def update_model(prev_state, user_move):
    if len(prev_state) == 3:
        history_model[tuple(prev_state)][user_move] += 1

def get_result(user, ai):
    if user == ai:
        return "Draw"
    elif winning_moves[user] == ai:
        return "AI Wins"
    else:
        return "You Win"

print("=== AI Rock-Paper-Scissors ===")
print("Make a move: rock / paper / scissors")
print("Type 'q' to quit\n")

while True:
    user_input = input("Your move: ").lower()
    if user_input == "q":
        print("Game Over.")
        break
    if user_input not in moves:
        print("Invalid input. Try again.")
        continue
    ai_move = ai_predict_move()
    print(f"AI chose: {ai_move}")
    print("Result:", get_result(user_input, ai_move))
    print("---")
    prev_state = list(user_history)
    update_model(prev_state, user_input)
    user_history.append(user_input)

