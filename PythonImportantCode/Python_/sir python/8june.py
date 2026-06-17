class Parent:
    def __init__(self,value):
        self.value=value

    def apple(self):
        print(f"exaecutng parent apple {self.value}")

    def google(self):
        print("executing parent goole")
        self.apple()

#child class having 
