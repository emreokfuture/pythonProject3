player_one=Player("one")
player_two=Player("two")
new_deck=Deck()
new_deck.shuffle()
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


round_num=0
while game_on:
    round_num +=1
    print(f"{round_num}")

    if len(player_one.add_cards)==0:
        print("player 1 is lost")
        game_on=False
        break
    if len(player_two.add_cards) == 0:
        print("player 2 is lost")
        game_on = False

        break
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

###new round
     player_one_cards=[]
