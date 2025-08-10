# RPS.py

def player(prev_play, opponent_history=[]):
    # Initialize opponent history if first game
    if prev_play != "":
        opponent_history.append(prev_play)

    # Default move (can be improved)
    guess = "R"

    return guess

# RPS.py

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Default move
    guess = "R"

    # Basic pattern recognition
    if len(opponent_history) >= 3:
        last_three = "".join(opponent_history[-3:])

        # Check for repeated patterns
        if last_three == "RRR":
            guess = "P"
        elif last_three == "PPP":
            guess = "S"
        elif last_three == "SSS":
            guess = "R"
        # Check for common sequences
        elif last_three == "RPS":
            guess = "S"  # They might play S next
        elif last_three == "PSR":
            guess = "R"  # They might play R next
        elif last_three == "SRP":
            guess = "P"  # They might play P next

    return guess

# RPS.py

def player(prev_play, opponent_history=[], player_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Counter strategies for each bot
    counter = {'P': 'S', 'R': 'P', 'S': 'R'}

    # Strategy 1: Counter most common move
    if len(opponent_history) >= 10:
        most_common = max(set(opponent_history), key=opponent_history.count)
        guess = counter[most_common]
    # Strategy 2: Counter predictable patterns
    elif len(opponent_history) >= 3:
        last_two = "".join(opponent_history[-2:])
        if last_two == "RP":
            guess = "P"
        elif last_two == "PS":
            guess = "S"
        elif last_two == "SR":
            guess = "R"
        else:
            # Fallback to counter last move
            guess = counter.get(opponent_history[-1], "R")
    else:
        # Default to Rock if no history
        guess = "R"

    # Remember our own moves for more complex strategies
    player_history.append(guess)

    return guess

# RPS.py

import random
from collections import defaultdict

def player(prev_play, opponent_history=[], sequence_length=3):
    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    # Initialize pattern dictionary if not enough history
    if len(opponent_history) <= sequence_length:
        return random.choice(['R', 'P', 'S'])

    # Build pattern dictionary
    last_sequence = "".join(opponent_history[-sequence_length:])
    potential_plays = [
        "".join([*opponent_history[-sequence_length+1:], "R"]),
        "".join([*opponent_history[-sequence_length+1:], "P"]),
        "".join([*opponent_history[-sequence_length+1:], "S"]),
    ]

    sub_history = opponent_history[:-1]

    pattern_dict = defaultdict(int)
    for i in range(len(sub_history) - sequence_length):
        pattern = "".join(sub_history[i:i+sequence_length])
        next_move = sub_history[i+sequence_length]
        pattern_dict[pattern + next_move] += 1

    # Predict next move based on patterns
    possible_patterns = [
        last_sequence + "R",
        last_sequence + "P",
        last_sequence + "S"
    ]

    for pattern in possible_patterns:
        if pattern not in pattern_dict:
            pattern_dict[pattern] = 0

    predicted_move = max(possible_patterns, key=lambda x: pattern_dict[x])[-1]

    # Counter the predicted move
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    guess = counter_moves[predicted_move]

    return guess