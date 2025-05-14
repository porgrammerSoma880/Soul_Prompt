import sys      #to pass the command line arguement/argv
import time     #to give a animative vibe



def motivation(user):
    """Function to show the motivational qoutes on the screen"""
    qoute_list=[f"{user}, fail fast, learn faster."
            ,"Build what others fear.",
            "Remember, success loves bold minds.",
            "Test, break, rebuild—repeat.",
            f"{user} launch your vision or stay grounded.",
            "Dream big or stay average.",
            "Try until you fail!",
            "Remember, comfort kills innovation.",
            f"{user}, let obsession drive execution."
            ,"Be relentless or be forgotten.",
            "Hardwork is the key to success.",
            f"{user}, Never give up!",
            "In any situation, be patience.",
            f"And the last advice for you, dear {user}: ",
            "Disrupt or be disrupted !"]
    
    for item in qoute_list:      #iteration in the list
        print(item)
        print("  ")        #gaps between the qoutes/texts to have a clearer look
        time.sleep(5)      #creates a animative feeling at the terminal



if __name__=="__main__":
    try:
        name=sys.argv[1]      #the user will have to type their name on the command line
        motivation(name)      #the arguement passed on command line will be taken as the function's parameter
    except IndexError:        
        print("Write your name as the arguement to run the program.")   
    #if no arguement is passed, the error will be catched hereover