from art import logo
import random
import time

print(logo)

play_game = input("Would you like to play a hand of black jack? (y/n)").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = ["X"]

def deal_card(hand, num):
    """Deal a card to either the player or dealer"""
    for x in range(num):
        if hand == "player":
            player_hand.append(random.choice(cards))
        if hand == "dealer":
            dealer_hand.append(random.choice(cards))

def time_delay(num):
    """Pause the game to make it more engaging"""
    for x in range(num):
        time.sleep(1)
        print(".")

def initial_deal():
    """Initial Cards are dealt"""
    print(f"Dealing cards...")
    time_delay(1)
    deal_card("player", 2)
    deal_card("dealer", 1)
    print(f"Dealers hand: {dealer_hand}")
    player_total = sum(player_hand)
    print(f"Players hand: {player_hand}, Total: {player_total}")

def dealer_reveal():
    dealer_hand[0] = random.choice(cards)
    dealer_total = calculate_score(dealer_hand)
    return f"Dealer hand: {dealer_hand} Dealer Total: {dealer_total}"


def check_results(dealer_total, player_total):
    if dealer_total > 21:
        print(f"You have {player_total} and the Dealer busts...You WIN!")
    elif dealer_total <= 21 and dealer_total > player_total:
        print(f"Dealer has {dealer_total} and you have {player_total}, Dealer wins!")
    elif dealer_total <=21 and dealer_total < player_total:
        print(f"Dealer has {dealer_total} and you have {player_total}, You win!")
    elif dealer_total <=21 and dealer_total == player_total:
        print(f"Dealer has {dealer_total} and you have {player_total}, it's a draw!")
    
def calculate_score(cards):
    """Calculates the current score of the hand, considering ace can be 1 or 11"""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

    
while play_game == "y":
    #Deal the cards and set up the hand
    initial_deal()
    player_stays = False
    player_busts = False
    player_total = sum(player_hand)

    while not player_stays and not player_busts:
        if player_total == 21 and len(player_hand) == 2:
            print("Blackjack! Player automatically stands at 21")
            time_delay(2)
            player_stays = True
        while player_total < 21 and not player_stays:
            hit = input("Do you wish to hit or stay? (h for hit, s for stay)")
            if hit == "h":
                deal_card("player", 1)
                print("Dealing card...")
                time_delay(2)
                player_total = calculate_score(player_hand)
                print(player_total)
                print(f"Players hand: {player_hand}\nPlayer total is {player_total}")
                if player_total == 21:
                    print("Player stays at 21")
                    player_stays = True
                elif player_total > 21:
                    print("Player busts")
                    player_busts = True
            elif hit == "s":
                player_stays = True
    if player_busts:
        print("Player loses! " + dealer_reveal())
    if player_stays and not player_busts:
        print(f"Player stays: " + dealer_reveal())
        dealer_total = sum(dealer_hand)
        time.sleep(1)  
        while dealer_total < 17 and dealer_total < 21:
            print("Dealing another card to dealer...")
            time_delay(2)
            deal_card("dealer", 1)
            dealer_total = calculate_score(dealer_hand)
            print(dealer_total)
            print(f"Dealer has: {dealer_total}")
        check_results(dealer_total, player_total)

    player_hand = []
    dealer_hand = ["X"]
    play_game = input("Would you like to play another hand of black jack? (y/n)").lower()

print("Thanks for playing!")