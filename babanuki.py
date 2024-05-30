import random

player_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
players = []

card_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_mark = ["♠", "♦", "♣", "♥"]
cards = []


def create_cards():
    for mark in card_mark:
        for i, num in enumerate(card_num):
            cards.append([i, mark + num])
    cards.append([13, "Joker"])

def shuffle_cards():
    random.shuffle(cards)

def add_player(name):
    player = {"name": name, "cards": []}
    players.append(player)

def deal_card():
    for i, c in enumerate(cards):
        players[i % len(players)]["cards"].append(c)

def show_cards():
    for player in players:
        player["cards"].sort()
        print(f'{player["name"]}の手札：{" ".join([c[1] for c in player["cards"]])}')

def delete_from_cards(lst, idxs):
    idxs.sort(reverse=True)
    for i in idxs:
        lst.pop(i)

def discard_pairs_for_player(player):
    discard_cards = []
    player_name = player["name"]
    player_cards = player["cards"]
    for i in range(len(player_cards)):
        for j in range(i + 1, len(player_cards)):
            if player_cards[i][0] == player_cards[j][0]:
                print(f"{player_name}が{player_cards[i][1]}と{player_cards[j][1]}を捨てました")
                player_cards[i][0] = player_cards[j][0] = -1
                discard_cards.append(i)
                discard_cards.append(j)
    delete_from_cards(player_cards, discard_cards)
    
def discard_pairs():
    for player in players:
        discard_pairs_for_player(player)

def draw_card(to_player, from_player):
    cidx = random.randint(0, len(from_player["cards"]) - 1)
    card = from_player["cards"].pop(cidx)
    to_player["cards"].append(card)
    print(f"{to_player["name"]}が{from_player["name"]}のカード{card[1]}を1枚引きました")
    discard_pairs_for_player(to_player)

def winner_check():
    wins = []
    for player in players:
        if len(player["cards"]) == 0:
            wins.append(player)
    return wins

def winner_win(winners):
    for winner in winners:
        print(f"*{winner["name"]}の勝利！")
        players.remove(winner)

def main():
    create_cards()
    shuffle_cards()
    deal_card()
    show_cards()
    discard_pairs()
    show_cards()

    prev_from_player = prev_to_player = None
    play_times = 0
    while 1 < len(players):
        from_player = players[play_times % len(players)]
        to_player = players[(play_times + 1) % len(players)]
        if prev_from_player != from_player and prev_to_player != to_player:
            draw_card(to_player, from_player)
            show_cards()
            wins = winner_check()
            if 0 < len(wins):
                winner_win(wins)
        prev_from_player = from_player
        prev_to_player = to_player
        play_times += 1
    print(f"*{players[0]["name"]}の敗北！")

if __name__ == "__main__":
    num = int(input("How many players? "))
    for i in range(num):
        add_player(player_names[i])
    main()
