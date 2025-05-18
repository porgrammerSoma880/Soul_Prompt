import sys      #to pass the command line arguement/argv
import time     #to give a animative vibe

# names should only by a string
# this function will check if the arguement is a string


def motivation(user):
    # Motivational quotes personalized for the user
    quotes = [
        f"{user}, fail fast, learn faster.",
        "Build what others fear.",
        "Remember, success loves bold minds.",
        "Test, break, rebuild—repeat.",
        f"{user}, launch your vision or stay grounded.",
        "Dream big or stay average.",
        "Try until you fail!",
        "Remember, comfort kills innovation.",
        f"{user}, let obsession drive execution.",
        "Be relentless or be forgotten.",
        "Hard work is the key to success.",
        f"{user}, never give up!",
        "In any situation, be patient.",
        f"And the last advice for you, dear {user}:",
        "Disrupt or be disrupted!"
    ]
    for quote in quotes:
        print(quote)
        print()  # Print a blank line for readability
        time.sleep(1)


def main():
    if len(sys.argv) < 2:
        print("Please provide your name as a command line argument.")
        sys.exit(1)
    name = sys.argv[1]
    motivation(name)
    

if __name__=="__main__":
    main()

