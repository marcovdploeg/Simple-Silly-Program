# A Simple Silly Program
# It is a fairly simple script that will ask some questions and respond most sillyously.
# You can ask it to pick a number for you, then it asks you to input two numbers, 
# and it gives a response and picks a number between them.
# You can tell it to guess your card, but it will just randomly name them one by one.
# And you can enter your birthday, and it responds how many days until your next one 
# (or congratulates you), and remembers what it did on that day once.
# After completing all three options at least once, a fourth button appears.

import random
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

num_responses = ["That first number is absolutely marvelous, but about the second I'm not so sure.",
                 "Both of these numbers are just wonderful, have you considered a career in number inputting?",
                 "I can't say I'm a huge fan of that first number, but the second is pure delight.",
                 "Those are certainly numbers! Have you thought about using them in a dance routine?",
                 "Fascinating choices! They remind me of a story of a penguin and a pineapple, but that's a tale for another time.",
                 "That first number is like chocolate, but the second is more like raisins. I suppose that works.",
                 "Now that is a combination I haven't seen before. And I basically am numbers!",
                 "The probability of you picking those numbers was approximately 42%, which is also the answer to Life, the Universe and Everything.",
                 "I would like to inform you that your numbers have been rated 'Moderately Interesting' by the International Number Society.",
                 "I would sing a song for those numbers, but I can't connect to your speakers.",
                 "Those numbers remind me of a time I tried to juggle flamingos. It didn't go well.",
                 "For that first number alone I want to buy you a cookie, but my card keeps declining.",
                 "Yesterday I saw a squirrel on a unicycle, which was the most amazing thing I've ever seen, until I saw your second number.",
                 "The first isn't very original, but the second adds enough pizazz to make it work.",
                 "I just got off the e-mail with ESA, and they said your numbers have potential for space travel.",
                 "I showed your numbers to my blind goldfish, and even he seemed impressed!",
                 "I can't help but feel your numbers have a certain 'je ne sais quoi'. Fancy!"]

cards = ['Red Joker', 'Black Joker']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
for suit in suits:
    for rank in ranks:
        cards.append(f"{rank} of {suit}")
random.shuffle(cards)

day_responses = ["On that day, I learned to juggle flamingos. It didn't go well.",
                 "That very day, I saw a penguin in Italy. It ordered pineapple pizza and got away with it!",
                 "I can't seem to recall anything happened that day. Perhaps it was too silly even for me!",
                 "On that day I played golf with Darth Vader. The golf was strong with that one.",
                 "That day I had a croissant for breakfast, can you believe that?",
                 "On that day I learned it is not a good idea to give a parrot a dictionary.",
                 "Ce jour-là, j'ai appris à parler français un petit peu.",
                 "That sounds like the kind of day that would wear a top hat while dancing the tango.",
                 "I think that's when I discovered my love for disco music.",
                 "They say an apple a day keeps the doctor away, and that day, it certainly did!",
                 "I went scuba diving that day, but all I found were rubber ducks.",
                 "I remember sunterflunking that day, but it turned into a real qwerhabble!",
                 "I almost found the answer to Life, the Universe and Everything that day, but then I got distracted and flew away.",
                 "Now that is a day I will always remember as the day I forgot about something.",
                 "I'm fairly sure that on that date, in the far future, the universe will explode. But don't quote me on that.",
                 "They say that on that day, a great silliness was born. Perhaps it was you!",
                 "They say that on that day, a most lovely creature was born. Perhaps it was you!",
                 "One cat is only 5/6 cat, so on that day, I adopted three cats.",
                 "That is the best day to dance the mariachi on!",
                 "That day belongs to the bravest of heart, the kindest of soul, and the silliest of minds.",
                 "On that day, I discovered the secret to making the perfect cup of tea. It involves a rubber chicken and a kazoo.",
                 "What is love? I found out on that day.",
                 "Lorem ipsum dolor sit amet, consectetur adipiscing elit ...",
                 "Fun fact: on that day, the Big Bang happened, about 14 billion years ago. I just know these things.",
                 "They say that this day used to be two days, but they merged into one to confuse historians.",
                 "Last time it was that day I invented a new colour called 'silopew'. You can only see it in the dark with one eye closed on Tuesday afternoon under a full moon.",
                 "For some reason, every time I do the tango on that day, I trip and fall into a giant bowl of spaghetti.",
                 "Of all possible days, that day is certainly the dayest.",
                 "I recall that as the only day I successfully cooked a crêpe with only my little pinkie finger."]

# Track which buttons have been clicked
clicked_buttons = {"button1": False, "button2": False, "button3": False}
button4_created = False

def victory_message():
    messagebox.showinfo("Success", "You've clicked all buttons at least once! Now just keep clicking until you have seen every possible message! Or read the source code, if you have better things to do.")

def check_all_clicked():
    # Create the fourth button if all three have been clicked at least once
    global button4_created
    
    if all(clicked_buttons.values()) and not button4_created:
        messagebox.showinfo("Success", "You've clicked all buttons at least once! Now just keep clicking until you have seen every possible message! Or read the source code, if you have better things to do.")
        button4 = tk.Button(root, text="Victory", command=victory_message)
        button4.place(relx=0.5, rely=0.5, anchor="center")
        button4_created = True

def pick_a_number():
    messagebox.showinfo("Info", "I can pick a number for you, but you need to give me two numbers it needs to be between first.")

    num_1 = simpledialog.askinteger("Input", "Please enter a number:")
    if num_1 is None:  # if window closed
        return  # just exit

    num_2 = simpledialog.askinteger("Input", "Please enter another number:")
    if num_2 is None:  # if window closed
        return  # just exit
    
    response = random.choice(num_responses)
    messagebox.showinfo("Info", response)

    lower = min(int(num_1), int(num_2))
    upper = max(int(num_1), int(num_2))
    if upper - lower <= 1:
        messagebox.showerror("Error", "There are no numbers between those two, I can't pick anything!")
        return  # exit
    random_number = random.randint(lower+1, upper-1)
    messagebox.showinfo("Result", f"My pick for you is: {random_number}.")

    # Click tracker
    clicked_buttons["button1"] = True
    check_all_clicked()

def guess_my_card():
    messagebox.showinfo("Info", "I will try to guess your card! Think of one from the standard 54-card deck.")
    
    for card in cards:
        user_response = simpledialog.askstring("Input", f"Is your card the {card}? Please answer 'yes' or 'no':")
        if user_response is None:  # if window closed
            return  # just exit

        user_response = user_response.strip().lower()
        if user_response == 'yes':
            messagebox.showinfo("Info", "It was only a matter of time!")
            break
        elif user_response == 'no':
            messagebox.showinfo("Info", "Then let me try again.")
            time.sleep(1)
        else:
            messagebox.showinfo("Info", "I didn't understand that, but I'll take it as a 'no'.")
            time.sleep(1)
    
    # Click tracker
    clicked_buttons["button2"] = True
    check_all_clicked()

def check_date_input(day, month):
    # Check if the input is actually a valid date
    is_valid_date = False
    while not is_valid_date:
        try:
            day = int(day)  # gives a ValueError if not a number
            month = int(month)
            datetime(datetime.now().year, month, day)  # gives a TypeError if not a valid date
            is_valid_date = True
        except ValueError or TypeError:
            messagebox.showerror("Error", "That's not a valid date!")
            day = simpledialog.askinteger("Input", "Please enter a valid day (1-31): ")
            if day is None:
                return None, None  # exit in main function
            month = simpledialog.askinteger("Input", "Please enter a valid month (1-12): ")
            if month is None:
                return None, None
    return day, month

def days_until_birthday():
    messagebox.showinfo("Info", "Tell me your birthday, and I'll tell you how many days until your next one!")
    day = simpledialog.askinteger("Input", "Enter the day (1-31):")
    if day is None:  # if window closed
        return  # just exit

    month = simpledialog.askinteger("Input", "Enter the month (1-12):")
    if month is None:  # if window closed
        return  # just exit
    day, month = check_date_input(day, month)
    if day is None or month is None:
        return  # exit

    time.sleep(1)
    response = random.choice(day_responses)
    messagebox.showinfo("Info", response)
    time.sleep(1)

    today = datetime.now()
    current_year = today.year
    birthday_this_year = datetime(current_year, month, day)

    # Normalize both dates to midnight for comparison
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    birthday_this_year = birthday_this_year.replace(hour=0, minute=0, second=0, microsecond=0)

    # Determine if the birthday has already occurred this year
    if birthday_this_year < today:
        birthday_next = datetime(current_year + 1, month, day)
    else:
        birthday_next = birthday_this_year

    delta = birthday_next - today
    days_left = delta.days

    if days_left == 0 and response == "Ce jour-là, j'ai appris à parler français un petit peu.":
        messagebox.showinfo("Info", "Joyeux anniversaire! 🎉")
    elif days_left == 0:
        messagebox.showinfo("Info", "Happy Birthday! 🎉")
    elif days_left == 1:
        messagebox.showinfo("Info", "Your birthday is tomorrow!")
    else:
        messagebox.showinfo("Info", f"There are {days_left} days until your next birthday.")
    
    # Click tracker
    clicked_buttons["button3"] = True
    check_all_clicked()

if __name__ == "__main__":
    # Start the main GUI loop
    root = tk.Tk()
    root.title("A Simple Silly Program")
    root.geometry("600x400")

    # Add three buttons to start screen, in a triangle
    button1 = tk.Button(root, text="Pick me a Number", command=pick_a_number)
    button1.place(relx=0.5, rely=0.1, anchor="center")

    button2 = tk.Button(root, text="Guess my Card", command=guess_my_card)
    button2.place(relx=0.2, rely=0.7, anchor="center")

    button3 = tk.Button(root, text="When is my Birthday?", command=days_until_birthday)
    button3.place(relx=0.8, rely=0.7, anchor="center")

    # Run it
    root.mainloop()
