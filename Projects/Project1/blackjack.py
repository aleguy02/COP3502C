from p1_random import P1Random

# defining game elements for statistics
games_played = 0
player_wins = 0
dealer_wins = 0
ties = 0

rng = P1Random()


def get_card():  # determines the card number for the player
    l_card_num = rng.next_int(13) + 1  # I called the variable l_card_num to differentiate it from the global card_num
                                       # that I use later
    return l_card_num


def print_menu():  # prints menu
    print('1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit')


def print_card_and_hand():
    card_num = get_card()  # card is drawn
    global total_hand

    if card_num == 11 or card_num == 12 or card_num == 13:  # face cards add a value of 10 to the total hand
        total_hand += 10
    else:
        total_hand += card_num  # non-face cards and ACE add their value to the total hand

    if card_num == 1:  # card value is reformatted only for face cards
        card_num = 'ACE'
    elif card_num == 11:
        card_num = 'JACK'
    elif card_num == 12:
        card_num = 'QUEEN'
    elif card_num == 13:
        card_num = 'KING'
    print(f'Your card is a {card_num}!')

    print(f'Your hand is: {total_hand}')


flag = True  # I used a flag variable to run the program because choice 4, which ends the game, is in a nested loop

while flag:  # this loop runs each new game
    games_played += 1
    print(f'START GAME #{games_played}')

    total_hand = 0
    dealer_hand = 0  # gotta reset hands after each game

    print_card_and_hand()

    while True:  # this loop runs what happens within each game

        if total_hand == 21:
            print('BLACKJACK! You win!')
            break
        elif total_hand > 21:
            print('You exceeded 21! You lose.')
            break

        print_menu()  # prints menu

        choice = int(input('Choose an option: '))
        if choice == 1:
            print_card_and_hand()
        elif choice == 2:  # determines value of dealer's hand, then who wins
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {total_hand}")
            if dealer_hand > 21:
                print('You win!')
                player_wins += 1
                break
            elif total_hand == dealer_hand:
                print("It's a tie! No one wins!")
                ties += 1
                break
            elif total_hand > dealer_hand:
                print('You win!')
                player_wins += 1
                break
            elif total_hand < dealer_hand:
                print('Dealer wins!')
                dealer_wins += 1
                break
        elif choice == 3:  # prints statistics
            print(f'Number of Player wins: {player_wins}')
            print(f'Number of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {ties}')
            print(f'Total # of games played is: {games_played}')
            percentage = "{:.1f}".format((player_wins / games_played) * 100)
            print(f'Percentage of Player wins: {percentage}%')
        elif choice == 4:
            flag = False
            break  # this is why I used a flag variable, because this break only ends the current game, not the whole
                   # program
        else:
            print('Invalid input!\nPlease enter an integer value between 1 and 4.')
