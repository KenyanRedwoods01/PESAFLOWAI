# greetingsModel.py
from datetime import datetime
import random

def get_greeting(user_name: str = None) -> str:
    now = datetime.now()
    hour = now.hour

    if hour < 12:
        greetings = ["Good morning", "Top of the morning", "Morning"]
    elif hour < 18:
        greetings = ["Good afternoon", "Hello", "Afternoon"]
    else:
        greetings = ["Good evening", "Evening", "Hope you had a great day"]

    greeting = random.choice(greetings)
    if user_name:
        greeting = f"{greeting}, {user_name}!"
    else:
        greeting = f"{greeting}!"

    return greeting

# Example usage:
if __name__ == "__main__":
    print(get_greeting("Alice"))
