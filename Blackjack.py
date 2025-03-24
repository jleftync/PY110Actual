import random

def create_new_deck():
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
    
    ace_counter = 0
    hand_value = 0

    for k in player_hnd:
        if type(player_hnd[k]) == list:
            ace_counter += 1
        else:
            hand_value += player_hnd[k]
    
    if hand_value > 10:
        hand_value += ace_counter
    else:
        hand_value += (11 + (ace_counter - 1))
    
    return hand_value

    """
    Import the player hand
    initialize an ace counter variable to zero
    initialize a hand value to zero
    use a for loop to iterate through the keys player hand,
    if the number 11 is found in the value of the player hand
        - increment the counter each time the value is found
    else:
        - add the value of the key to the value variable

    if pre ace hand value > 10  any number of aces in hand
    - ad 1 for each acea in the hand
    update deck value
-   else if pre ace value <= 10, ace value = 1 in hand
    - add 11 plus number of aces - 1 to deck value
    - update deck value
    

    """
    pass

def deal_cards():
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
            print(dealer_hand.keys())
        if num == 1:
            print(player_hand.keys())
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
    key = random.choice(list(inp_deck.keys()))
    value = inp_deck.pop(key)
    inp_hand[key] = value
    return [inp_hand, inp_deck]

def busted():
    return None
def output_winner(first_hnd, scnd_hnd):
    if first_hnd > scnd_hnd:
        print("Player Wins!")
    else:
        print("Computer Wins!")

def play_game():
    game_con = deal_cards()
    my_hand = game_con[0]
    computer_hand = game_con[1]
    game_deck = game_con[2]
    computer_wins = False
    
    
    while True:
        answer = input("hit or stay? ")
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
        
        
        


play_game()


"""
Algorithm:
- Make a function called create new deck
- New deck function creates a deck library
- library has 52 cards with corresponding card as key, poker value as value
- Ace has list of 2 values 1 and 2
-create hand compute varialble and set to zero
- Make a function called choose ace value that inputs hand non ace hand value
and ace count
-iterate through the cards, adding the value of non ace cards updating the
choose ace value
- if pre ace hand value,  > 10 any number of aces in hand
    - ad 1 as ace value
    update deck value
- else if pre ace value <= 10, 1 ace in hand
    - add 10 as ace value
    - update deck value

- else if pre ace value + 1 for each ace in hand beyond 1 < = 10
    - return 10 for 1 ace 1 for the rest
- else
    - return 4 for all aces
    - update deck value

- Make a function called compute hand value which imports card value, current 
hand value
- 
- add to it the value of the card dealt if the card dealt is not an ace
- else call choose ace value and add the result

-Make a deal function
    - generate an empty player dictionary and an empty dealer dictionary
    - generate 2 empty hand value variables, player and dictionary
    - call the create a new deck function
    - Pop a card and its value at random and assigns it to the 
    player dictionary, printing the card identity, call the change and calls the compute hand value
    function on the player hand value
    - Pop a card at and its value at random and assigns it to the dealer
    dictionary calling the compute hand fnctn on dealer hand value
    - Pops a card and its value and randomly assigns it to the player
    dictionary, printing the card identity, call and calls the compute hand value
    function on the player hand value.
    - Pops a card and its value and randomly assigns it to the dealer
    dictionary, printing the card identity, call and calls the compute hand value
    function on the player hand value.
    return player hand dict, computer hand dict, computer hand value, player hand value,
    resulting deck dict

-Make a hit function
    - import dictionary of current deck
    - import current hand library and value
    - pop a random card from a deck
    - call the hand value function on the card and current hand value
    -

- make a main play game function
- call the deal functin
- ask if player wishes to hit or stand
- if hit call hit function
- if value resulting is over 21, player busts, computer wins
- if stand
- computer checks to see if its value is over 17
- if not hit until it is either over 17 or it busts
- if both players stand, closer to 21 wins




"""