from functools import cmp_to_key


def compare_paris(pair1, pair2):
    word1, number1 = pair1
    word2, number2 = pair2
    if number1 == number2:
        if word1 < word2:
            return 1
        else:
            return -1
    if number1 < number2:
        return -1
    else:
        return 1


compare_key = cmp_to_key(compare_paris)


def kFrequentWords(words, k):
    hashMap = dict()

    for item in words:
        hashMap[item] = hashMap.get(item, 0) + 1

    pairs = list()
    for key in hashMap.keys():
        t = (key, hashMap[key])
        pairs.append(t)

    del hashMap

    pairs = sorted(pairs, key=compare_key, reverse=True)

    print(pairs)

    words = list()
    for i in range(k):
        words.append(pairs[i][0])

    return words


print(kFrequentWords(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
