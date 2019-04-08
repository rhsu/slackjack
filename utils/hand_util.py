def hand_string(hand):
    return " ".join(map(lambda x: str(x), hand))


def hand_sum(hand):
    # there can only be 1 ace that is 11
    # so need to 1 check if has aces, if not then compute simple sum

    # if has aces, then make the first ace an 11 and compute the as simple sum
    # add the two together
    # return sum(map(lambda x: x.value(), hand))
    hand_copy = list(hand)
    simple_sum = _simple_sum(hand_copy)
    if _contains_ace(hand_copy):
        new_sum = 11 + _simple_sum(hand)
        if new_sum > 21:
            return simple_sum
        else:
            return new_sum
        pass
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
