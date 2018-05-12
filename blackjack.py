from random import shuffle

# define the card ranks and suits
ranks = [_ for _ in range(2,11)] + ['Jack','Queen','King','Ace']
suits = ['Spade','Heart','Diamond','Club']

def get_deck():
    '''
    Return a new deck of cards.
    '''
    return[[rank, suit] for rank in ranks for suit in suits]

# get deck of cards, and randomly shuffle it
deck = get_deck()
shuffle(deck)

# boolean variable that indicates wether the player has gone bust
player_in = True

# issue the player and dealer their first two cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

def card_value(card):
    '''
    Returns the integer value of a single card.
    '''
    rank = card[0]
    if rank in ranks[0:-4]:
        return int(rank)
    elif rank is 'Ace':
        return 11
    else:
        return 10

def hand_value(hand):
    '''
    Returns the integer value of a set of cards.
    '''
    # Naivly sum up the cards in the deck
    tmp_value = sum(card_value(_) for _ in hand)
    # Count the sum of Aces in the hand.
    num_aces = len([_ for _ in hand if _[0] is 'Ace'])

    # Aces can count for 1, or 11. If it is possible to bring the value
    # of the hand under 21 by making 11 -> 1 substitutions , do so.

    while num_aces > 0:
        if tmp_value > 21 and 'Ace' in ranks:
            tmp_value -= 10
            num_aces -= 1
        else:
            break
    
    # Return a string and an integer representing the value of the hand.
    # if the hand is bust return 100.

    if tmp_value < 21:
        return[str(tmp_value),tmp_value]
    elif tmp_value == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!',100]

# As long as the player remains in the game, ask them if they'd like to hit
# for another card, or stay with their current hand.
while player_in:
    # Display player's current hand, as well as its value.
    current_score = hand_value(player_hand)[0]
    print(f'\nYou are currently at {current_score} {player_hand}')

    # if the player's hand is bust, don't ask them for a decision.
    if hand_value(player_hand)[1] == 100:
        break

    if player_in:
        response = int(input('Hit or stay? (Hit = 1, Stay = 0)'))
        # If the player asks to be hit, take the first card from the top of
        # the deck and add it to their hand. If they ask to stay, change
        #player_in to falsem and move on to the dealer's hand.
        if response:
            player_in = True
            new_player_card = deck.pop()
            player_hand.append(new_player_card)
            print(f'You draw {new_player_card}')
        else:
            player_in = False

player_score_label, player_score = hand_value(player_hand)
dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score <= 21:
    print(f'Dealer is at {dealer_score_label}\n with the hand {dealer_hand}')
else:
    print('Dealer wins!')

while hand_value(dealer_hand)[1] < 17:
    new_dealer_card = deck.pop()
    dealer_hand.append(new_dealer_card)
    print(f'Dealer draws {new_dealer_card}')

dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score < 100 and dealer_score == 100:
    print('You beat the dealer!')
elif player_score > dealer_score:
    print('You beat the dealer!')
elif player_score == dealer_score:
    print('You tied the dealer, nobody wins!')
else:
    print('Dealer wins!')