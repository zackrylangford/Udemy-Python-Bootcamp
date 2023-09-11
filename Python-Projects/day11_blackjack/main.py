from art import logo
import random
import time

print(logo)

play_game = input("Would you like to play a hand of black jack? (y/n)").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
    """Deal a card to either the player or dealer"""
    if hand == "player":
        player_hand.append(random.choice(cards))
    if hand == "dealer":
        dealer_hand.append(random.choice(cards))

while play_game == "y":
    # Inital cards are dealt
    print("Dealing cards to player...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")

    player_hand = []
    deal_card("player")
    deal_card("player")
    print(f"Players hand: {player_hand}")

    #Dealing cards to dealer
    print("Dealing cards to dealer...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    dealer_hand = []
    dealer_hand.append("X")
    deal_card("dealer")
    print(f"Dealers hand: {dealer_hand}")
    print(f"Players hand: {player_hand}")

    # Player is prompted to hit or stay
    player_total = sum(player_hand)

    player_stays = False
    player_busts = False

    while not player_stays and not player_busts:
        if player_total == 21:
            print("Blackjack! Player automatically stands at 21")
            player_stays = True
        while player_total < 21 and player_stays == False:
            print(f"Your total is {player_total}")
            if player_total < 21:
                hit = input("Do you wish to hit or stay? (h for hit, s for stay)")
                if hit == "h":
                    deal_card("player")
                    player_total = sum(player_hand)
                    print(f"Players hand: {player_hand}\nPlayer total is {player_total}")
                    if player_total == 21:
                        print("Player stays at 21")
                        player_stays = True
                    elif player_total > 21:
                        print("Player busts\nYou lose")
                        player_busts = True
                elif hit == "s":
                    player_stays = True
    if player_busts:
        dealer_hand[0] = random.choice(cards)
        dealer_total = sum(dealer_hand)
        print(f"Dealer hand revealed: {dealer_hand} which equals {dealer_total}")
    if player_stays and not player_busts:
        dealer_hand[0] = random.choice(cards)
        dealer_total = sum(dealer_hand)
        print(f"Player stays and the dealer has: {dealer_hand}")
        print(f"Dealer total: {dealer_total}") 
        time.sleep(1)  
        while dealer_total < 17 and dealer_total < 21:
            print("Dealing another card to dealer...")
            #Sleep for 2 seconds and print a filler ellipses
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            deal_card("dealer")
            print(dealer_hand)
            dealer_total = sum(dealer_hand)
            print(f"Dealer has: {dealer_total}")
        if dealer_total > 21:
            print(f"You have {player_total} and the Dealer busts...You WIN!")
        elif dealer_total <= 21 and dealer_total > player_total:
            print(f"Dealer has {dealer_total} and you have {player_total}, Dealer wins!")
        elif dealer_total <=21 and dealer_total < player_total:
            print(f"Dealer has {dealer_total} and you have {player_total}, You win!")
        elif dealer_total <=21 and dealer_total == player_total:
            print(f"Dealer has {dealer_total} and you have {player_total}, it's a draw!")

    play_game = input("Would you like to play another hand of black jack? (y/n)").lower()

print("Thanks for playing!")