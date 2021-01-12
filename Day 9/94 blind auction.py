bids_dict = {}
bids=[]
another_bidder = "yes"

def get_bid():
    name = input("What is your name?")
    bid = input("What is your bid?")
    bids_dict[name] = bid

def get_winner(bids_dict):
    highest_bid = 0
    winner = ""
    for i in bids_dict:
        bid = bids_dict[i]
        if bid > winner:
            highest_bid = bid
            winner = i
    return i

while another_bidder == "yes":
    get_bid()
    another_bidder = input("Is there another bidder? (Yes / No)")
    another_bidder.lower()

winner=get_winner(bids_dict)

print(winner)

