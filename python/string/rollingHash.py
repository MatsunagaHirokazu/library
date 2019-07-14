# ハッシュの基数
# B = 10 ** 9 + 7
mod1 = 10 ** 9 + 7
mod2 = 10 ** 9 + 9

# 方法1　アリ本の実装だが、これはバグってる


def contain(a: str, b: str, B: int) -> bool:
    """
    aがbに含まれているかどうか判定する
    """
    al = len(a)
    bl = len(b)
    if al > bl:
        return False
    t = B ** al
    ah, bh = 0, 0
    for i in range(al):
        ah = ah * B + a[i]
    for i in range(bl):
        bh = bh * B + b[i]
    i = 0
    while i <= bl - al:
        if ah == bh:  # bのi文字目からのal文字が一致
            return True
        if i + al < bl:
            bh = bh * B + b[i + al] - b[i] * t
        i += 1
    return False

# 方法2 これはうまくいきそう


class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            # ord maps the character to a number
            # subtract out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) -
                          ord("a")+1)*(26**(sizeWord - i - 1))

        # start index of current window
        self.window_start = 0
        # end of index window
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            # remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]
                              ) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end]) - ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]


def rabin_karp(word, text):
    if word == "" or text == "":
        return False
    if len(word) > len(text):
        return False

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))
    # word_hash.move_window()

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                return i
        rolling_hash.move_window()
    return False


print(rabin_karp("x", "abcdefgh")
