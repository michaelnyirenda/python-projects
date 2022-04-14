from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)


bids = {}
no_bids = False

def winning_bid(bid_ting):
    highest_bid = 0
    for bidder in bid_ting:
        amount = bid_ting[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")

while not no_bids:
    name = input("what's your name? : ")
    price = int(input("what's your bid? $"))
    bids[name] = price
    more = input("are there more user that wanna bid? type 'yes' or 'no' : ")
    if more == "no":
        no_bids = True
        winning_bid(bids)
    elif more == "yes":
        clear()
        


