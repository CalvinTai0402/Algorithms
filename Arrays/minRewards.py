# O(N) T O(N) S
def minRewards(scores):
    reward = []
    for i in scores:
        reward.append(1)
    for i in range(len(scores) - 1):
        if scores[i + 1] > scores[i]:
            reward[i + 1] = max(reward[i + 1], reward[i] + 1)
    for i in reversed(range(1, len(scores))):
        if scores[i - 1] > scores[i]:
            reward[i - 1] = max(reward[i - 1], reward[i] + 1)
    return sum(reward)
