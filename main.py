# import the 'activities' from corresponding python file
from study import study
from play import play

def printLine():
    print("="*50)
# main program start
if __name__ == "__main__":

    printLine()
    print("Today is a wonderful day!")

    # Make plan for today
    printLine()
    print("What should I aim for today?")
    plan1 = study()
    plan2 = play()

    # Work on the plan
    printLine()
    print("And is time to work on the plan, and...")
    do_plan1 = plan1.spend_time()
    do_plan2 = plan2.spend_time()
    
    # End of today
    printLine()
    print("Is almost the end of today, and ", end='')
    if do_plan1 and do_plan2:                           # Successfully merge two branch
        print("I have work life balance!!!")
        print("Thanks for doing merge on my 'study' and 'play' branch to 'master' branch :)))")
    else:
        print("Why I can't have work life balance :(")  # Didn't merge for two branch
        print("I should do the merge my 'study' and 'play' branch to 'master' branch and make my life better")

    printLine()
    print("Btw Nessie is cute :3")                      # Random Nessie Appear
