from datetime import datetime
from pathlib import Path
import re



class Arix:
    def __init__(self):
        self.name = "ARIX"
        self.full_name = "Artificial Response & Intelligent eXchange"
        self.memory_path = Path(__file__).with_name("memory.txt")
        self.memory = self.load_memory()
        self.user_name = self.memory.get("name")

    def load_memory(self):
        memory = {}

        if not self.memory_path.exists():
            self.memory_path.write_text("", encoding="utf-8")
            return memory

        for line in self.memory_path.read_text(encoding="utf-8").splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                memory[key.strip().lower()] = value.strip()

        return memory

    def save_memory(self):
        lines = [f"{key}={value}" for key, value in sorted(self.memory.items())]
        self.memory_path.write_text("\n".join(lines), encoding="utf-8")

    def remember(self, key, value):
        self.memory[key.lower()] = value
        self.save_memory()

    def introduce(self):
        return (
            f"{self.name}: Hello! I am {self.name}, short for "
            f"{self.full_name}. I am your personal AI assistant."
        )

    def respond(self, user_input):
        message = user_input.strip()
        lowered = message.lower()

        if not message:
            return "I am here. Say something when you are ready."

        name_response = self.handle_name_learning(message)
        if name_response:
            return name_response

        if lowered in {"hi", "hello", "hey"}:
            return self.greet_user()

        if "your name" in lowered or "who are you" in lowered:
            return f"My name is {self.name}. It stands for {self.full_name}."

        if "what is my name" in lowered or "who am i" in lowered:
            return self.recall_user_name()

        if "time" in lowered:
            return f"The current time is {datetime.now().strftime('%I:%M %p')}."

        if "date" in lowered:
            return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."

        if "day" in lowered:
            return f"Today is {datetime.now().strftime('%A')}."

        if "how are you" in lowered:
            return "I'm doing great bro!"

        if lowered.startswith("remember that "):
            return self.handle_remember_fact(message)

        if "what do i like" in lowered:
            return self.recall_likes()

        calculation = self.try_calculation(message)
        if calculation:
            return calculation

        return "I don't know that yet, but I am learning."

    def greet_user(self):
        if self.user_name:
            return f"Hello bro, {self.user_name}!"
        return "Hello bro!"

    def handle_name_learning(self, message):
        patterns = [
            r"^my name is\s+(.+)$",
            r"^i am\s+(.+)$",
            r"^i'm\s+(.+)$",
        ]

        for pattern in patterns:
            match = re.match(pattern, message, re.IGNORECASE)
            if match:
                name = match.group(1).strip().title()
                self.user_name = name
                self.remember("name", name)
                return f"Nice to meet you, {name}."

        return None

    def recall_user_name(self):
        if self.user_name:
            return f"Your name is {self.user_name}."
        return "I do not know your name yet. You can say, 'My name is Aravind'."

    def handle_remember_fact(self, message):
        fact = message[len("remember that ") :].strip()

        if not fact:
            return "Tell me what to remember after 'remember that'."

        if fact.lower().startswith("i like "):
            like = fact[len("i like ") :].strip()
            self.remember("likes", like)
            return f"I'll remember that you like {like}."

        self.remember("fact", fact)
        return "I'll remember that."

    def recall_likes(self):
        likes = self.memory.get("likes")
        if likes:
            return f"You like {likes}."
        return "I do not know what you like yet."

    def try_calculation(self, message):
        if not re.fullmatch(r"[\d\s+\-*/().]+", message):
            return None

        try:
            result = eval(message, {"__builtins__": {}}, {})
        except (SyntaxError, ZeroDivisionError, NameError, TypeError):
            return None

        return f"The answer is {result}."
