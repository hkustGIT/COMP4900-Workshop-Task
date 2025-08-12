from abc import ABC, abstractmethod

class activities(ABC):
    def __init__(self, plan):
        print(f"I aim to {plan} today!!!!!")
    
    @abstractmethod
    def spend_time(self) -> bool:
        pass