def store(name, value):
    global_env[name] = value

global_env = {}

def run():
    while True:
        inc = input("")
        if inc == "" or inc == "quit":
           return

        comm = inc.split(" ")
        if len(comm) < 3:
            print("invalid command!")
            return

        command = comm[1]
        if command == "=":
            if not comm[2].isdigit():
                print("only int can be store!")
                return
            store(comm[0], int(comm[2]))
        elif command == "+":
            pass
        elif command == "-":
            pass
        else:
            print("unsupported command!")
            return

run()
print("exiting")