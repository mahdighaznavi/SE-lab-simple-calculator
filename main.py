if __name__ == "__main__":
    print("Welcome to our simple calculator")
    command = input().strip()
    while command != "exit":
        ops = command.split(' ')
        # recognize the command
        if ops[0] == "+":
            print(int(ops[1]) + int(ops[2]))
        command = input().strip()
    print("Thanks for choosing us :)")
