def hand_string(hand):
    return " ".join(map(lambda x: str(x), hand))


def hand_sum(hand):
    return sum(map(lambda x: x.value(), hand))
