"""
Bite_44: License Key generator
"""

def gen_key(*, parts=4, chars_per_part=8) -> str:
    """get_key - gen key based on chars per parts.
    """
    import secrets
    hex_data = secrets.token_hex(256)
    result = []

    for part in range(parts):
        if part + chars_per_part > len(hex_data):
            raise Exception("too big!")

        result.append(hex_data[part:part + chars_per_part])

    return "-".join([char.upper() for char in result])
