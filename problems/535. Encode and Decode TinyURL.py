'''
=== 535. Encode and Decode TinyURL ===

Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''
# === 36ms(34.73%) && 12.8MB(100%) === #
class Codec:

    def __init__(self):
        self.mapping = {}
    
    def random_short_url(self):
        chars = string.ascii_letters + string.digits
        return "".join(
            random.choice(chars) for _ in range(6)
        )
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = self.random_short_url()
        # print(short_url)
        self.mapping[short_url] = longUrl
        return "http://tinyurl.com/{}".format(short_url)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # print(self.mapping)
        return self.mapping[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))