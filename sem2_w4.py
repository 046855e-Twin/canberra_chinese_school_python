import random

scores = []

for i in range(5):
    scores.append(random.randint(0,100))

def adjust_score(score):
    if score >= 90:
        score -= 5
        return score
    elif score <= 50:
        score += 10
        return score
    else:
        return score

new_scores = list(map(adjust_score, scores))
pass_or_not = list(map(lambda x:"pass" if x >= 60 else "fail", new_scores))
print(scores)
print(new_scores)
print(pass_or_not)