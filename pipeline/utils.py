def extract_market_value(market_value):
    if 'bn' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000_000
    if 'm' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000_000
    elif 'Th' in market_value:
        return float(''.join(c for c in market_value if c.isdigit() or c == '')) * 1_000
    else:
        return 0.0


def extract_age(age):
    if age == '-':
        return 0.0
    return age
