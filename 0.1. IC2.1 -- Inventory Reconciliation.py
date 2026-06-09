from collections import Counter

worker_a = ["bolt", "nut", "nut", "screw", "washer", "bolt",
            "bolt"]
worker_b = ["bolt", "bolt", "nut", "screw", "screw", "washer"]


def count_each_item(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    dct = {}
    diff = counter_a - counter_b
    for i in set(worker_a + worker_b):
        dct[i] = {"a": counter_a[i], "b": counter_b[i], "diff" : diff[i]}

    return dct


print(count_each_item(worker_a, worker_b))
