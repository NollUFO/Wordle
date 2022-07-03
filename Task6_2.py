target = input().upper()
guess = input().upper()
feedback = ["." for i in range(len(guess))]
accurate = []
inaccurate = []
for i,k in enumerate(guess):
    if k == target[i]:
        feedback[i] = k
        accurate.append(i)
for i,k in enumerate(guess):
    for j,l in enumerate(target):
        if j in inaccurate or j in accurate:
            continue
        if k == l:
            feedback[i] = k
            inaccurate.append(j)
            break
for i in range(len(feedback)):
    if not i in accurate:
        feedback[i] = feedback[i].lower()
print("".join(feedback))
