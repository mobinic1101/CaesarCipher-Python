from string import ascii_lowercase, digits
from typing import List


def cycle(iterable: List, start: int = 0):
    while 1:
        for i in range(start, len(iterable)):
            yield iterable[i]
        start = 0


class CaesarCipher:
    def __init__(self):
        self.ascii_chars = [*ascii_lowercase]
        self.digits = [*digits]
        self.all_chars = self.digits + self.ascii_chars

    def __shift_char(self, char: str, shift: int):
        char = char.lower()
        if shift > len(self.ascii_chars) or shift < -len(self.ascii_chars):
            raise ValueError("Invalid shift")

        iterable = self.ascii_chars + self.digits if shift > 0 else self.ascii_chars[::-1] + self.digits[::-1]
        current_char = ""
        c = cycle(iterable, iterable.index(char))

        for _ in range(abs(shift) + 1):
            current_char = next(c)

        return current_char

    def encrypt(self, text, shift=1):
        new_text = ""
        for char in text:
            if char not in self.all_chars:
                new_text += char
                continue
            new_text += self.__shift_char(char, shift)
        return new_text

    def decrypt(self, text, shift=-1):
        return self.encrypt(text, shift)


# testing it!
if __name__ == '__main__':
    e = CaesarCipher()
    password = "hello world 123"
    passwordE = e.encrypt(password, shift=10)
    passwordD = e.decrypt(passwordE, shift=-10)
    print(f"encrypted of '{password}': ", passwordE)
    print(f"decrypted of '{passwordE}': ", passwordD)