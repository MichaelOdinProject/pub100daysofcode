
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    # This iterates through the KEYS
    for bidder in bids:
        # find the value by passing the key
        bid_price = bids[bi dder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of £{bid_price}.")


# empty bids dict
bids = {}
bidding_finished = False
while not bidding_finished:
    # Get bidder name
    bidder_name = input("What is your name?: ")
    # ask their bid
    bid_amount = int(input("What is your bid?: "))
    # Store bidder info
    bids[bidder_name] = bid_amount

    # Are there other bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    # If no other bidders - Find highest bidder THEN end auction else do nothing
    if other_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)

    # END - reveal highest bidder
