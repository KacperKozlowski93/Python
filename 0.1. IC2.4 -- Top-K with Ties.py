scores = {"a": 90, "b": 85, "c": 90, "d": 70, "e": 85, "f": 60}


def top_k_with_ties(score, k):
    sort_list = []
    for i in scores.items():
        sort_list.append(i)

    sorted(sort_list, key=lambda x: x[1], reverse=True)
    result = []
    threshold = sort_list[k - 1][1]
    for name, score in sort_list:
        if score >= threshold:
            result.append(name)
        else:
            break
    return result


print(top_k_with_ties(scores, 6))
