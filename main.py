from player import player


player1 = player("Sid", 2, 4, True)
player2 = player("Ahmet", 6, 4, True)
player3 = player("Gaetano", 7, 2, True)
player4 = player("Ben", 4, 1, True)
players = [player1, player2, player3, player4]
rankedplayers = []

def ranking(): # Getting the rank of players, returning a sorted list of the names, first name is rank number one.
    global rankedplayers
    playerscores = [] #Creating a list of the players' scores
    for player in players:
        player.calculateScore()
        playerscores.append(player.score)
    playerscores.sort()

    rankedplayers = [] # Finding the players' name corresponding with the players' score and making a list.
    # print(playerscores)
    for score in playerscores:
        for player in players:
            if player.score == score:
                rankedplayers.append(player.name)
                break
    rankedplayers = rankedplayers[::-1]

def scoreboard(): #printing sorted player name and score
    print()
    for name in rankedplayers:
        for player in players:
            if name == player.name:
                print(player.name, player.score)

ranking()

# print(rankedplayers)
scoreboard()