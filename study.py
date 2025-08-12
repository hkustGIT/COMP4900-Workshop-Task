from activities import activities

class study(activities):
    def __init__(self):
        super().__init__("study")
    
    def spend_time(self) -> bool:
        print("I have time to study :(")
        return True