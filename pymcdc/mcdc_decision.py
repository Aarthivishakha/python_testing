"""MC/DC fixture containing a compound Boolean decision."""


def classify_score(score, is_bonus, is_premium):
    if score >= 75 and (is_bonus or is_premium):
        return "pass_with_credit"
    return "standard"
