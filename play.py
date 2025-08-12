from activities import activities

# play class is inherit of activities class
class play(activities):
    def __init__(self):
        super().__init__("play")

    # We have time to play so return True
    def spend_time(self) -> bool:
        print("I have time to play :)")
        return True