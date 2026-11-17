# Lea Corpsdhomme - Group A
# 1. In: The player's name and scenarios_A.csv. The CSV uses commas and 14 columns:
# ID, Scenario, three option texts, three budget changes, three reputation
# changes and three feedback messages. Changes are signed whole numbers.
# 2. What happens during one day:
# Show the day, budget, reputation, situation and three choices.
# Ask for A, B or C until the player gives a valid answer.
# Apply the chosen changes, limit reputation to 100 and show feedback.
# Save the reputation change in the history and check whether the player is fired.
# 3. Out: The result (Fired or a title), the final gauges, and the best and worst
# moves. results.csv gets: name,budget,reputation,title,date (one row per game).
# 4. What could go wrong:
# A wrong choice: ask again. A gauge at 0 or less: stop the game immediately.
# A missing or invalid scenario file: explain the problem without crashing.
# Feature A: Three reputation gains in a row earn 500 EUR. I chose it because
# it rewards several good marketing decisions in a row.

import csv
import random
from datetime import date
from pathlib import Path


# Find the files next to the game, even if Python is launched elsewhere.
FOLDER = Path(__file__).resolve().parent
SCENARIO_FILE = FOLDER / "scenarios_A.csv"
RESULTS_FILE = FOLDER / "results.csv"


# Read the CSV and create a tuple for each of the three options.
def load_scenarios():
    scenarios = []
    with open(SCENARIO_FILE, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = {}
            for letter in ("A", "B", "C"):
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
            scenarios.append((row["Scenario"], options))
    if len(scenarios) < 10:
        raise ValueError("The scenario file needs at least 10 scenarios.")
    return scenarios


# Repeat the question when the player types something other than A, B or C.
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C.")


# Apply one option, then return the two updated gauges as a tuple.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)
    print(feedback)
    return budget, reputation


# Give a title only to a player who survived all ten days.
def get_title(budget, reputation):
    score = reputation + budget // 200
    if score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"
    return score, title


# Add one game result, creating the header only for a new or empty file.
def save_result(name, budget, reputation, title):
    needs_header = not RESULTS_FILE.exists() or RESULTS_FILE.stat().st_size == 0
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if needs_header:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# Play ten shuffled scenarios, or finish sooner if one gauge reaches zero.
def play_game():
    try:
        scenarios = load_scenarios()
    except (OSError, ValueError, KeyError, csv.Error) as error:
        print("Cannot load scenarios_A.csv:", error)
        return

    name = input("Player's name: ").strip()
    while not name:
        name = input("Please enter your name: ").strip()

    random.shuffle(scenarios)
    budget = 10000
    reputation = 50
    streak = 0
    history = []
    fired = False

    for day, (situation, options) in enumerate(scenarios[:10], start=1):
        print("\n--- Day", day, "---")
        print("Budget:", budget, "EUR | Reputation:", str(reputation) + "/100")
        print(situation)
        for letter in ("A", "B", "C"):
            print(letter + ":", options[letter][0])

        choice = ask_choice()
        option = options[choice]
        old_reputation = reputation
        budget, reputation = apply_choice(budget, reputation, option)
        actual_reputation_change = reputation - old_reputation
        print("Budget change:", option[1], "EUR | Reputation change:", actual_reputation_change)
        history.append((actual_reputation_change, day, option[0]))

        # A zero gauge ends the game before any streak bonus can rescue it.
        if budget <= 0 or reputation <= 0:
            fired = True
            break

        # Three positive reputation gains in a row earn 500 EUR.
        if actual_reputation_change > 0:
            streak = streak + 1
        else:
            streak = 0
        if streak == 3:
            budget = budget + 500
            print("Streak bonus! +500 EUR for three reputation gains in a row.")
            streak = 0

    # Show the final outcome and the days with the best and worst reputation change.
    print("\n==============================")
    if fired:
        reasons = []
        if budget <= 0:
            reasons.append("budget reached zero")
        if reputation <= 0:
            reasons.append("reputation reached zero")
        title = "Fired"
        print(name + ", you are fired:", " and ".join(reasons) + ".")
    else:
        score, title = get_title(budget, reputation)
        print("Quarter survived!")
        print("Final score:", score)
        print(name + ", your title:", title)

    print("Budget left:", budget, "EUR | Reputation:", str(reputation) + "/100")
    best = max(history)
    worst = min(history)
    print("Best move: day", best[1], "-", best[2], "(" + str(best[0]) + ")")
    print("Worst move: day", worst[1], "-", worst[2], "(" + str(worst[0]) + ")")
    save_result(name, budget, reputation, title)
    print("Saved in results.csv")


# Start only when this file is run as the main program.
if __name__ == "__main__":
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. No result saved.")
