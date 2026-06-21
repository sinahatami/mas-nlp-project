class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am a {self.role}.")