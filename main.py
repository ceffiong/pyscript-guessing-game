from pyscript import window, document
from pyweb import pydom
import random


secret = 0
gameStarted = False
numOfGuess = 0
maxGuess = 3

def start(event):
    global secret
    global numOfGuess
    # Generate random number from 0 - 9
    secret = random.randrange(0,10)
    print(f"Secret number is {secret}")

    # enable the buttons
    myButtons = document.querySelectorAll(".btn")
    for btn in myButtons:
        btn.disabled = False
        btn.classList.add("choise-btn-active")
    
    # change start button text
    startBtn = document.querySelector("#start-game")
    startBtn.innerHTML = 'Restart game'

    # update number of guess and game log
    elem = document.querySelector("#no-of-guess")
    elem.innerHTML = 0

    gameLog = document.querySelector("#game-log")
    gameLog.innerHTML = ""

    numOfGuess = 0




def create_logs(text, classes):
    new_div = pydom.create("div")
    new_p = new_div.create("p", classes=[classes], html=text)
    pydom['#game-log'][0].append(new_div)

def choice(event):
    global numOfGuess
    numOfGuess = numOfGuess + 1
    
    # update number of guess
    elem = document.querySelector("#no-of-guess")
    elem.innerHTML = numOfGuess

    selected = int(event.target.id)
    print(f"secret: {secret}  -> selected: {selected}")
    if(numOfGuess == maxGuess and secret != selected):
        print("You loss")
        create_logs("You lost &#128521; Try again! ", "wrong-guess")

        # disable the buttons
        myButtons = document.querySelectorAll(".btn")
        for btn in myButtons:
            btn.disabled = True
            btn.classList.remove("choise-btn-active")

    else: 
        if(selected == secret):
            print("You win")
            create_logs("You guess was right. You won! &#127881; &#127882; ", "right-guess")

            # disable the buttons
            myButtons = document.querySelectorAll(".btn")
            for btn in myButtons:
                btn.disabled = True
                btn.classList.remove("choise-btn-active")
        else:
            if(secret < selected):
                print("Secret number is less than your current guess")
                create_logs("Secret number is less than your current guess &#128521; ", "wrong-guess")
            else:
                print("Secreat number is greater than your current guess")
                create_logs("Secret number is greater than your current guess &#128521; ", "wrong-guess")
    




