from datetime import datetime

class Arix:

    def __init__(self):
        self.name = "ARIX"

    def get_response(self, user):

        user = user.lower()

        if any(word in user for word in ["hi", "hello", "hey"]):
            return "Hello bro!"
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
        
        elif user in ["quit", "bye"]:
            return "ARIX: Goodbye bro!"

        else:
            return "I don't know that yet."

    def save_name(self, name):

    with open("memory.txt", "w") as file:
        file.write(name)


def get_name(self):

    try:
        with open("memory.txt", "r") as file:
            return file.read()

    except:
        return None
    
        
        
        