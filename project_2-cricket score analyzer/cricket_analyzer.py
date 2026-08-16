import numpy as np
players=[]
scores=[]
for i in range(11):
    name=input("Enter Player Name:")
    score=int(input("Enter Score:"))
    players.append(name)
    scores.append(score)
scores=np.array(scores)
print(scores)

total=np.sum(scores)
highest=np.max(scores)
lowest=np.min(scores)
average=np.mean(scores)

print("Team Total:", total)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)


fiftes=scores[scores>=50]
print("scored above Fifite:",fiftes)

indexes = np.where(scores >= 50)[0]
print("Players who scored 50+:")
for i in indexes:
    print(players[i], "scored", scores[i])

hundreds=scores[scores>=100]
print("Players who scored 100+:",hundreds)
indexes = np.where(scores >= 100)[0]
for i in indexes:
    print(players[i], "scored", scores[i])

grades = np.where(scores >= 100, "A",
            np.where(scores >= 50, "B",
                np.where(scores >= 25, "C", "D")))

print("Player Grades:")
for i in range(11):
    print(players[i], "→", scores[i], "→ Grade:", grades[i])

print("--- BOWLER STATS ---")

bowlers=[]
overs=[]
runs_given=[]
wickets=[]

for i in range(5):
    name=input("Enter Bowler Name:")
    over=int(input("Enter Overs Bowled:"))
    run=int(input("Enter Runs Given:"))
    wicket=int(input("Enter Wickets Taken:"))
    bowlers.append(name)
    overs.append(over)
    runs_given.append(run)
    wickets.append(wicket)

overs=np.array(overs)
runs_given=np.array(runs_given)
wickets=np.array(wickets)

economy=runs_given/overs

print("Bowler Performance:")
for i in range(5):
    print(bowlers[i],"→ Overs:",overs[i],"Runs:",runs_given[i],"Wickets:",wickets[i],"Economy:",round(economy[i],2))

best_index=np.argmax(wickets)
print("Best Bowler:",bowlers[best_index])
print("Wickets:",wickets[best_index])
print("Economy:",round(economy[best_index],2))

print("Total Wickets:",np.sum(wickets))
print("Best Economy:",bowlers[np.argmin(economy)],"→",round(np.min(economy),2))

print("--- MATCH SIMULATION ---")

import random

opponent_scores = np.array([random.randint(0, 120) for i in range(11)])
opponent_total = np.sum(opponent_scores)

print("Opponent Scores:", opponent_scores)
print("Opponent Total:", opponent_total)
print("Your Team Total:", total)

if total > opponent_total:
    print("Your Team Wins!")
elif total < opponent_total:
    print("Opponent Wins!")
else:
    print("Match Tied!")