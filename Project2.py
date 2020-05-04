import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'Deck: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('\nPlease make a bet: '))

        except:
            print('\nYou entered not a number. Please enter a number')

        else:
            if chips.bet > chips.total:
                print('\nSorry, insufficient balance. Available balance: {}'.format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('\nDo you want Hit or Stand?: Choose h or s : ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('\nPlayer stand.Dealers turn')
            playing = False
        else:
            print('\nPlease choose Hit or Stand, insert h or s : ')
            continue
        break


def show_some(player, dealer):
    print('\nDealers Cards:')
    print('\n <Hidden Card>')
    print('', dealer.cards[1])
    print('\nPlayers Cards:\n', *player.cards, sep='\n ')


def show_all(player, dealer):
    print('\nDealers Cards:', *dealer.cards, sep='\n ')
    print('Dealer Cards =', dealer.value)
    print('\nPlayers Card:', *player.cards, sep='\n ')
    print('\nPlayers Cards =', player.value)


def player_busts(player, dealer, chips):
    print('\nPlayer loose > 21')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('\nPlayer won')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('\nPlayer won. Dealer > 21')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('\nDealer won')
    chips.lose_bet()


def push(player, dealer):
    print('\nDraw')


while True:
    print('\nWelcome to Blackjack Game!')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            dealer_busts(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    print('\n Player chips: {}'.format(player_chips.total))

    new_game = input('\nDo you want to play again? y or n : ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('\nThanks for playing!')
        break
