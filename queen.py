at_war = True
while at_war:
    if player_one_cards[-1].value > player_two_cards[-1].value:
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        at_war=False
    elif player_one_cards[-1].value < player_two_cards[-1].value:
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        at_war=False
    else:
        print("War")

        if len(player_one.all_cards) < 3:
            print("player 1 unable to declare a war")
            print("player two wins")
            game_on=False
            break

        elif len(player_two.all_cards) < 3:
            print("player 1 unable to declare a war")
            print("player two wins")
            game_on = False
            break
        else:
            for num in range (3):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())