import random, art
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def deal_cards(count):
    dealt_cards = []
    for i in range(0,count):
        dealt_cards += random.choice(cards)
    return dealt_cards

def get_score(card):
    if card == "A":
        return int(11)
    elif card == "J" or card == "Q" or card == "K":
        return int(10)
    else:
        return int(card)

def check_score(deck,score,ace_status):
    if "A" not in deck and score >21:
        end_game(deck,score)
    elif "A" in deck and ace_status == True and score > 21:
        score -= 10
    return(score,ace_status)

def show_cards(player_deck,player_score,computer_deck):
    print(f"Your cards: {player_deck}, current score: {player_score}")
    print(f"Computers first card: {computer_deck[0]}")
    return = print("Type 'y' to get another card, type 'n' to pass:")




new_game = True
def game():
    print(art.logo)
    player_ace = True
    computer_ace = True
    player_deck = (deal_cards(2))
    computer_deck = (deal_cards(2))
    player_score = 0
    computer_score = 0
    for i in player_deck:
        player_score += get_score(i)
    for i in computer_deck:
        computer_score += get_score(i)
    play_on = True
    while play_on:
        show_cards()
    print(player_score)



game()

