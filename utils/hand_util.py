def hand_string(hand):
    return " ".join(map(lambda x: str(x), hand))


def hand_sum(hand):
    # from pdb import set_trace; set_trace()
    hand_copy = list(hand)
    simple_sum = _simple_sum(hand_copy)
    if _contains_ace(hand_copy):
        new_sum = 11 + _simple_sum(hand_copy)
        if new_sum > 21:
            return simple_sum
        else:
            return new_sum
    return simple_sum


def _simple_sum(hand):
    return sum(map(lambda x: x.value(), hand))


def _contains_ace(hand):
    count = 0
    for card in hand:
        if card.rank == "A":
            hand.pop(count)
            return True
        count += 1
    return False
