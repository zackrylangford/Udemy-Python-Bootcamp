# This doesn't work


from art import logo
import random
import time

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def deal_initial_hand():
    return [deal_card(), deal_card()]

def display_hands(player_hand, dealer_hand, reveal_dealer=False):
    if reveal_dealer:
        print(f"Dealer's hand: {dealer_hand}")
    else:
        print(f"Dealer's hand: ['X', {dealer_hand[1]}]")
    
    print(f"Player's hand: {player_hand}, current score: {sum(player_hand)}")

def check_blackjack(hand):
    return sum(hand) == 21

while input("Would you like to play a hand of black jack? (y/n)").lower() == "y":
    
    player_hand = deal_initial_hand()
    dealer_hand = deal_initial_hand()
    
    display_hands(player_hand, dealer_hand)

    game_over = False

    while not game_over:

        if check_blackjack(player_hand):
            print("Blackjack! You win!")
            break

        player_choice = input("Do you wish to hit or stay? (h for hit, s for stay)").lower()
        
        if player_choice == "h":
            player_hand.append(deal_card())
            display_hands(player_hand, dealer_hand)
            
            if sum(player_hand) > 21:
                print("You went over 21. You lost!")
                game_over = True
        else:
            game_over = True

    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    display_hands(player_hand, dealer_hand, reveal_dealer=True)

    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    if dealer_score > 21 or dealer_score < player_score:
        print("You win!")
    elif dealer_score > player_score:
        print("You lose!")
    else:
        print("It's a draw!")
    
    time.sleep(2)
