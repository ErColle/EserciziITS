def is_valid_ipv4(address: str):
    if address.count(".") != 3:
        return f"False (solo {address.count(".") + 1} parti )"

    tokens = address.split('.')

    for token in tokens:
        if not token.isdigit():
            return "False (parte non numerica)"
        
        valore = int(token)
        if not (0 <= valore <= 255):
            return f"False, {token} è fuori range"

    return True
