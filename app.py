#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


def game():
        options = ["rock", "paper", "scissors"]
        score = [0, 0]

        while True:
            player1 = input("Player 1, choose rock, paper o scissors: ")
            player2 = input("Player 2, choose rock, paper o scissors: ")

            if player1 not in options or player2 not in options:
                print("Wrong option. Please, choose rock, paper o scissors.")
                continue

            if player1 == player2:
                print("Tie!")
            elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
                print("Player 1 wins!")
                score[0] += 1
            else:
                print("Player 2 wins!")
                score[1] += 1

            option = input("¿ Want to play again ? (y/n): ")
            if option.lower() != "y":
                break

        print("Final score:")
        print("Player 1:", score[0])
        print("Player 2:", score[1])

game()
