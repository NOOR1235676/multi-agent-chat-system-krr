# src/main.py

from coordinator import Coordinator

if __name__ == "__main__":
    system = Coordinator()

    print("=== Simple Multi-Agent Chat System ===")
    print("Type 'exit' to quit\n")

    while True:
        user_query = input("USER: ")

        if user_query.lower() == "exit":
            print("System terminated.")
            break

        response = system.handle_query(user_query)

        print("\nSYSTEM RESPONSE:")
        for item in response["response"]:
            print(item)
        print("-" * 50)
