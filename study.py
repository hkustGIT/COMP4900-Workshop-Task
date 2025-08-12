from activities import activities

# study class is inherit from study class
class study(activities):
    def __init__(self):
        super().__init__("study")
    
    # We have time to study so return True
    def spend_time(self) -> bool:
        print("I have time to study :)")
        return True