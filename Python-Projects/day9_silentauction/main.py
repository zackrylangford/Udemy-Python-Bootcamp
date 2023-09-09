from art import logo


print(logo)

auction_closed = False

bids = []

while not auction_closed:
    name = input("Please input your name:\n")
    bid = int(input("Please input your bid price\n"))
    entry = {name:bid}
    bids.append(entry)
    close_auction = input("Are there any other bidders? Y or N\n")
    if close_auction == "N":
        auction_closed = True
    else:
        #clear the screen
        print("\n" * 100)

        

# Initialize the highest bid to zero and the winner as an empty string
highest_bid = 0
winner = ""

# Iterate over all bids to find the highest bid and the winner
for bid in bids:
    for name, bid_amount in bid.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name

# Print the highest bid and the winner
print(f"The highest bid is: ${highest_bid} by {winner}")

print("Auction completed")
