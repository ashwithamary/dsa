class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

    def add_item(self, item_name):
        items_list = {"banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"}

        if item_name in items_list:
            self.items.append(item_name)

def print_results(race_results):
    ct =1
    for racer in race_results:
        print(f"{ct}. {racer.character}")

def get_place(my_player):
    place = 1
    current= my_player
    while current.ahead:
        place+=1
        current = current.ahead
    return place
# pb 1
# player_one = Player("Yoshi", "Super Blooper")
# print(player_one.character)
# print(player_one.kart) 
# print(player_one.items)

# pb 2
# player_one = Player("Yoshi", "Dolphin Dasher")
# print(player_one.items)

# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)

# pb 3
# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M")
# luigi = Player("Luigi", "Super Blooper")
# race_one = [peach, mario, luigi]

# print_results(race_one)

# pb 4
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
player2_rank = get_place(peach)
player3_rank = get_place(mario)

print(player1_rank)
print(player2_rank)
print(player3_rank)
