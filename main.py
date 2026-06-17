from brain import Arix

ai = Arix()

print("ARIX Online")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    print("ARIX:", ai.get_response(user))
    
    print("\n") 


