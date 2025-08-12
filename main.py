from study import study
from play import play

# main program start
if __name__ == "__main__":
    plan1 = study()
    plan2 = play()

    do_plan1 = plan1.spend_time()
    do_plan2 = plan2.spend_time()
    
    if do_plan1 and do_plan2:
        print("I trust nessie, therefore:")
        print("I have work life balance :)")
    else:
        print("Why I can't have work life balance")