"Game similar to blackjack"
import random

def create_new_deck():
    """
    Create a deck of cards
    """
    full_deck = {
        "Ace of Spades": [1, 11],
        "Ace of Hearts": [1, 11],
        "Ace of Diamonds": [1, 11],
        "Ace of Clubs": [1, 11],
        "Two of Spades": 2,
        "Two of Hearts": 2,
        "Two of Diamonds": 2,
        "Two of Clubs": 2,
        "Three of Spades": 3,
        "Three of Hearts": 3,
        "Three of Diamonds": 3,
        "Three of Clubs": 3,
        "Four of Spades": 4,
        "Four of Hearts": 4,
        "Four of Diamonds": 4,
        "Four of Clubs": 4,
        "Five of Spades": 5,
        "Five of Diamonds": 5,
        "Five of Clubs": 5,
        "Five of Hearts": 5,
        "Six of Spades": 6,
        "Six of Hearts": 6,
        "Six of Diamonds": 6,
        "Six of Clubs": 6,
        "Seven of Spades": 7,
        "Seven of Clubs": 7,
        "Seven of Diamonds": 7,
        "Eight of Hearts": 8,
        "Eight of Clubs": 8,
        "Eight of Diamonds": 8,
        "Eight of Spades": 8,
        "Nine of Clubs": 9,
        "Nine of Diamonds": 9,
        "Nine of Hearts": 9,
        "Nine of Spades": 9,
        "Ten of Clubs": 10,
        "Ten of Diamonds": 10,
        "Ten of Hearts": 10,
        "Ten of Spades": 10,
        "Jack of Clubs": 10,
        "Jack of Diamonds": 10,
        "Jack of Hearts": 10,
        "Jack of Spades": 10,
        "Queen of Clubs": 10,
        "Queen of Diamonds": 10,
        "Queen of Hearts": 10,
        "Queen of Spades": 10,
        "King of Clubs": 10,
        "King of Diamonds": 10,
        "King of Hearts": 10,
        "King of Spades": 10
    }


    return full_deck

def calculate_value(player_hnd):
    """
    calculates the value of the input hand
    """
    ace_counter = 0
    hand_value = 0

    for k in player_hnd:
        if isinstance(player_hnd[k], list):
            ace_counter += 1
        else:
            hand_value += player_hnd[k]

    if (hand_value + ace_counter) > 10:
        hand_value += ace_counter
    else:
        hand_value += (11 + (ace_counter - 1))

    return hand_value




def deal_cards():
    """
deal_cards gives each player 2 cards initially
"""
    #card_deal = 0
    dealer_hand = {}
    player_hand = {}

    new_deck = create_new_deck()
    for num in range(2):
        #key, value = d1.popitem()  # Removes and returns the last inserted key-value pair
        #d2[key] = value
        #   # Pick a random key
        # return key, d.pop(key)
        key = random.choice(list(new_deck.keys()))
        value = new_deck.pop(key)
        player_hand[key] = value
        key = random.choice(list(new_deck.keys()))
        value = new_deck.pop(key)
        dealer_hand[key] = value
        if num < 1:
            print("Dealer is showing " + "".join(list(dealer_hand.keys())))
        if num == 1:
            print("Players hand has " + " and ".join(list(player_hand.keys())))
        #card_deal += 1
    # elif card_deal == 1:
    #     key = random.choice(list(new_deck.keys()))
    #     value = new_deck.pop(key)
    #     player_hand[key] = value
    #     key = random.choice(list(new_deck.keys()))
    #     value = new_deck.pop(key)
    #     dealer_hand[key] = value
    #     print(player_hand.keys())

    return [player_hand, dealer_hand, new_deck]

def p_hit(inp_hand, inp_deck):
    """
    Hit choice adds a card to player hand
    """
    key = random.choice(list(inp_deck.keys()))
    value = inp_deck.pop(key)
    inp_hand[key] = value
    return [inp_hand, inp_deck]

# def busted():
#     return None

def output_winner(first_hnd, scnd_hnd):
    """
    Selects a winner
    """
    if first_hnd > scnd_hnd:
        print("Player Wins!")
    else:
        print("Computer Wins!")

def play_game():
    "Actual Blackjack Gameplay"
    print("Welcome to 21")
    game_con = deal_cards()
    my_hand = game_con[0]
    computer_hand = game_con[1]
    game_deck = game_con[2]
    computer_wins = False


    while True:
        answer = input("Please choose whether to hit or stay: ")
        if answer == "hit":
            hit_list = p_hit(my_hand, game_deck)
            my_hand = hit_list[0]
            print(my_hand)
            game_deck = hit_list[1]
            hand_value = calculate_value(my_hand)
            print(hand_value)
            if hand_value > 21:
                computer_wins = True
                print("Computer_wins")
                break

        if answer == 'stay':
            hand_value = calculate_value(my_hand)
            print("You chose to stay!")
            break


    if not computer_wins:
      
        while True:
            computer_value = calculate_value(computer_hand)
            if computer_value < 17:
                hit_list = p_hit(computer_hand, game_deck)
                computer_hand = hit_list[0]
                game_deck = hit_list[1]
                computer_value = calculate_value(computer_hand)
                if computer_value > 21:
                    print(computer_hand)
                    print("Player_Wins")
                    break
            if computer_value > 16:
                print(computer_hand)
                output_winner(hand_value, computer_value)
                break
    play_again = input("Would you like to play again? Please enter y or n")
    while play_again not in ['y', 'n']:
        play_again = input("Please specifically enter a y or an n ")
    if play_again == y:
        play_game()



play_game()
