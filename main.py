from player import Player
from deck import Deck

player1 = Player("One")
player2 = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for i in range(26):
    player1.add_cards(new_deck.deal_a_card())
    player2.add_cards(new_deck.deal_a_card())

print(player1.all_cards[0])

print("Welcome to card war game!")
start = input("Do you want to start game? (Y/N): ")
if start.lower().startswith('y'):
    start_game = True
else:
    start_game = False
iterate = 0
while start_game:
    iterate += 1
    print(f"Round {iterate}")

    if len(player1.all_cards == 0):
        print("Player 1 is out of cards and player 2 wins!!")
        start_game = False
        break

    if len(player2.all_cards == 0):
        print("Player 2 is out of cards and player 1 wins!!")
        start_game = False
        break

    # Start playing next round
    player1_curr_cards = [player1.remove_card()]

    player2_curr_cards = [player2.remove_card()]


