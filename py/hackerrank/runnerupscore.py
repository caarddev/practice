n = int(input())
arr = list(map(int, input().split()))
unique_scores = sorted(set(arr), reverse=True)
runner_up_score = unique_scores[1]
print(runner_up_score)

