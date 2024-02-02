class Hello:

    def __init__(self) -> None:
        self.myname = "Class 1"
        pass


    def say(self,yourMessage):
        print(f"Hello ... {yourMessage}")


hello = Hello()
hello.say("warapetch")