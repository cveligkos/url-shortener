import hashlib
import random
import string

BASE62 = string.ascii_lowercase + string.ascii_uppercase + string.digits


def shorten_url(url: str) -> str:
    salt = random.randint(1, 150666410)
    url_hash = int(hashlib.md5(url.encode()).hexdigest()[:5], 16)
    result = salt ^ url_hash
    return encode_int_to_base62(result)


def encode_int_to_base62(n: int):
    output = []
    while n > 0:
        mod = n % 62
        output.append(BASE62[mod])
        n //= 62

    output.reverse()
    print("base62 -> " + "".join(output))
    return "".join(output)
