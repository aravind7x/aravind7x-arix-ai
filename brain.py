from datetime import datetime

class Arix:

    def __init__(self):
        self.name = "ARIX"

    def get_response(self, user):

        user = user.lower()

        if "hello" in user:
            return "Hello bro!"
        
        if user in ["exit", "quit", "bye"]:
            return "ARIX: Goodbye bro!"

        elif "your name" in user:
            return f"My name is {self.name}"

        elif "time" in user:
            return datetime.now().strftime("%H:%M:%S")
        
        elif "date" in user:
            return datetime.now().strftime("%d-%m-%Y")
        
        elif "day" in user:
            return f"Today is {datetime.now().strftime('%A')}"

        elif "how are you" in user:
            return "I'm doing great bro!"

        else:
            return "I don't know that yet."
    
        
        
        