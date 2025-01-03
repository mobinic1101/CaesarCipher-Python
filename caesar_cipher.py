from string import ascii_lowercase, ascii_uppercase, digits
from typing import List


def cycle(iterable: List, start: int = 0):
    while 1:
        for i in range(start, len(iterable)):
            yield iterable[i]
        start = 0


class CaesarCipher:
    def __init__(self):
        self.ascii_lowercase = [*ascii_lowercase]
        self.ascii_uppercase = [*ascii_uppercase]
        self.digits = [*digits]
        self.__all_chars = self.digits + self.ascii_lowercase + self.ascii_uppercase
        self.__all_chars_reverse = [*reversed(self.__all_chars)]

    def __shift_char(self, char: str, shift: int):
        iterable = self.__all_chars if shift > 0 else self.__all_chars_reverse
        current_char = ""
        c = cycle(iterable, iterable.index(char))

        for _ in range(abs(shift) + 1):
            current_char = next(c)

        return current_char

    def encrypt(self, text, shift=1):
        new_text = ""
        for char in text:
            if char not in self.__all_chars:
                new_text += char
                continue
            new_text += self.__shift_char(char, shift)
        return new_text

    def decrypt(self, text, shift=-1):
        return self.encrypt(text, shift)


# testing it!
if __name__ == '__main__':
    e = CaesarCipher()
    password = "Hello World 1357$**"
    passwordE = e.encrypt(password, shift=10)
    passwordD = e.decrypt(passwordE, shift=-10)
    print(f"encrypted of '{password}': ", passwordE)
    print(f"decrypted of '{passwordE}': ", passwordD)
    # encrypted of 'Hello World 1357':  Rovvy 6yBvn bdfh
    # decrypted of 'Rovvy 6yBvn bdfh':  Hello World 1357