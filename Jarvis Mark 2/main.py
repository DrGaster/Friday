def command(cmd):
    return [word for word in cmd.split()]

user = input("What is your name? ")

class Jarvis:
    def __init__(self, user):
        self.user = user
    
    def intro(self):
        print("Hello", self.user + ", ", "I'm Jarvis")

    def assist(self):
        cmd = True
        while cmd:
            cmd = command(input("What can I do for you? "))

            if cmd == "exit":
                cmd = False
                break
            if cmd == "google":
                break


J = Jarvis(user)

J.intro()
J.assist()