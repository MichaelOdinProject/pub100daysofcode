# # from random import sample


# # ask if they want to play
# play_game = input("Do you want to play BlackJack? Yes or No?: ")
# if play_game.lower() == "no" or play_game.lower() == "n":
#     print("Ok, Come and play some other time!")
# else:

#     # card deck
#     card_deck_string = (
#         "1❤️ 2❤️ 3❤️ 4❤️ 5❤️ 6❤️ 7❤️ 8❤️ 9❤️ 10❤️ J❤️ Q❤️ K❤️ A❤️"
#         " 1♦️ 2♦️ 3♦️ 4♦️ 5♦️ 6♦️ 7♦️ 8♦️ 9♦️ 10♦️ J♦️ Q♦️ K♦️ A♦️"
#         " 1♧ 2♧ 3♧ 4♧ 5♧ 6♧ 7♧ 8♧ 9♧ 10♧ J♧ Q♧ K♧ A♧"
#         " 1♤ 2♤ 3♤ 4♤ 5♤ 6♤ 7♤ 8♤ 9♤ 10♤ J♤ Q♤ K♤ A♤"
#     )
#     card_deck = card_deck_string.split(" ")

#     # deal the cards
#     user_cards = sample(card_deck, 2)
#     dealer_cards = sample(card_deck, 2)
#     print(f"Your hand is: {user_cards}")


##################################
##################################
##################################
import random


def deal_card():
    '''returns random card from deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Take a lsit of cards and return score calculated'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lost, Dealer has BlackJack"
    elif user_score == 0:
        return "Win, You have BlackJack"
    elif user_score > 21:
        return "Lost, You went bust"
    elif dealer_score > 21:
        return "Win, Dealer went bust"
    elif user_score > dealer_score:
        return "You win with a higher score!!"
    else:
        return "You have lost!! Dealer had a higher score!"


user_cards = []
dealer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())


while not is_game_over:

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f" Your cards: {user_cards}, Current Score: {user_score}")
    print(f" Dealer's first card: {dealer_cards[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True


while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

print("+++++ " * 3)
print("+++++ " * 3)
print("+++++ " * 3)

print(f" Your final hand: {user_cards}, final score: {user_score}")
print(
    f" Dealer's final hand: {dealer_cards}, Dealer's final score: {dealer_score}")
print("+++++ " * 3)
print("RESULTS")
print("+++++ " * 3)
print(compare(user_score, dealer_score))
