"""Combined branch-coverage and dead-definition fixture."""


def evaluate_order(total, is_member):
    unused_note = "not used"
    if total > 100:
        discount = 0.1
    else:
        discount = 0.0
    if is_member:
        discount += 0.05
    return total * (1 - discount)
