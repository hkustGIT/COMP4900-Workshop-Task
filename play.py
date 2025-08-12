from activities import activities

class play(activities):
    def __init__(self):
        super().__init__("play")

    def spend_time(self) -> bool:
        print("I don't have time to play :(")
        return False