import random
import time
from typing import Tuple

# Konstanty pro snadnou změnu hry
DIGITS_COUNT = 4

def generate_secret(length: int) -> str:
    """Vygeneruje unikátní tajné číslo, které nezačíná nulou."""
    digits = list(range(10))
    while True:
        sampled = random.sample(digits, length)
        if sampled[0] != 0:
            return "".join(map(str, sampled))

def validate_input(guess: str, length: int) -> Tuple[bool, str]:
    """Ověří, zda je uživatelský vstup platný podle pravidel."""
    if not guess.isdigit():
        return False, "Vstup musí obsahovat pouze číslice."
    if len(guess) != length:
        return False, f"Zadej přesně {length} číslice."
    if guess[0] == '0':
        return False, "Číslo nesmí začínat nulou."
    if len(set(guess)) != length:
        return False, "Číslice se nesmí opakovat."
    return True, ""

def evaluate_guess(secret: str, guess: str) -> Tuple[int, int]:
    """Spočítá počet bulls (shoda pozice) a cows (shoda číslice)."""
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def format_plural(count: int, singular: str, plural: str) -> str:
    """Pomocná funkce pro správné skloňování (bull/bulls)."""
    return f"{count} {singular if count == 1 else plural}"

def play_game():
    """Hlavní smyčka hry."""
    print("Hi there!")
    print("-" * 47)
    print(f"I've generated a random {DIGITS_COUNT} digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    secret = generate_secret(DIGITS_COUNT)
    guesses = 0
    start_time = time.time()

    while True:
        user_input = input("Enter a number: ").strip()
        guesses += 1
        
        is_valid, error_msg = validate_input(user_input, DIGITS_COUNT)
        if not is_valid:
            print(error_msg)
            print("-" * 47)
            continue

        if user_input == secret:
            end_time = time.time()
            duration = int(end_time - start_time)
            print(f"Correct, you've guessed the right number\nin {guesses} guesses!")
            print("-" * 47)
            print(f"That's amazing! Time: {duration} seconds.")
            break

        bulls, cows = evaluate_guess(secret, user_input)
        
        b_text = format_plural(bulls, "bull", "bulls")
        c_text = format_plural(cows, "cow", "cows")
        print(f"{b_text}, {c_text}")
        print("-" * 47)

if __name__ == "__main__":
    play_game()