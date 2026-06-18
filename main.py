from brain import Arix


from brain import Arix


def main():
    arix = Arix()
    print(arix.introduce())
    print("Type 'exit' or 'quit' to stop.")

    while True:
        user_input = input("You: ").strip()
        
        
        if user_input.lower() in {"exit", "quit", "bye"}:
            print(f"{arix.name}: Goodbye, {arix.user_name or 'friend'}!")
            break

        response = arix.respond(user_input)
        print(f"{arix.name}: {response}")


if __name__ == "__main__":
    main()
    