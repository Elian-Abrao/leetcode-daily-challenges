class Solution:
    def __init__(self) -> None:
        self._prefix = "http://tinyurl.com/"
        self._key_to_url = {}
        self._url_to_key = {}
        self._next_id = 1
        self._alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _to_base62(self, value: int) -> str:
        if value == 0:
            return self._alphabet[0]

        encoded_chars = []
        base = len(self._alphabet)

        while value > 0:
            value, remainder = divmod(value, base)
            encoded_chars.append(self._alphabet[remainder])

        return "".join(reversed(encoded_chars))

    def encode(self, longUrl: str) -> str:
        if longUrl in self._url_to_key:
            return self._prefix + self._url_to_key[longUrl]

        key = self._to_base62(self._next_id)
        self._next_id += 1

        self._key_to_url[key] = longUrl
        self._url_to_key[longUrl] = key

        return self._prefix + key

    def decode(self, shortUrl: str) -> str:
        key = shortUrl[len(self._prefix):]
        return self._key_to_url[key]


Codec = Solution