def agent_brain(task): #agent function with task as parameter
    task = task.lower() #converts task to lowercase.

    if "weather" in task:
        return "I can't check live weather yet, but if it looks cloudy, take an umbrella."
    elif "joke" in task:
        return "Why don’t skeletons fight each other? They don’t have the guts."
    elif "time" in task:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    else:
        return "I don't know how to do that yet, but I'm learning!"


print("Hello! I’m your simple agent. Type 'quit' to stop.")

while True:
    user_input = input("What do you want me to do? ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    response = agent_brain(user_input)
    print(response)