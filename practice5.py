leaderboard = [
	('Alice', 88),
	('Bob', 92),
	('Charlie', 92),
	('David', 85)
]

scores = [('Zelda', 100), ('Mario', 120), ('Link', 100), ('Sonic', 100)]
def sort_leaderboard(leaderboard):
    leaderboard.sort()
    for i in range(len(leaderboard)):
        for j in range(i+1, len(leaderboard)):
            if leaderboard[i][1] < leaderboard[j][1]:
                leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]
    return leaderboard
            
    # for i in leaderboard:
    #     if i[1] > maxium:
    #         maxium = i[1]
    # return maxium

print(sort_leaderboard(leaderboard))
print(sort_leaderboard(scores))

