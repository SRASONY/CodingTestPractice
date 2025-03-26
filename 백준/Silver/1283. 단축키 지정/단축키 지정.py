N = int(input())
alphabet = [input() for _ in range(N)]
shortcut = []
result = []

for a in alphabet:
    words = a.split()
    found = False

    for i in range(len(words)):
        if words[i][0].lower() not in shortcut:
            shortcut.append(words[i][0].lower())
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            found = True
            break

    if not found:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j].lower() not in shortcut:
                    shortcut.append(words[i][j].lower())
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j + 1:]
                    found = True
                    break
            if found:
                break

    result.append(' '.join(words))

for r in result:
    print(r)
