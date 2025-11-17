def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    alphabet = 26  # 26 - количество букв в английском алфавите
    A_num = ord("A")
    a_num = ord("a")
    keyword = keyword.upper()
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char) - A_num
            if char.isupper():
                size = A_num
            else:
                size = a_num
            position = (ord(char) - size + shift) % alphabet
            ciphertext += chr(size + position)
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    alphabet = 26  # 26 - количество букв в английском алфавите
    A_num = ord("A")
    a_num = ord("a")
    keyword = keyword.upper()
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char) - A_num
            if char.isupper():
                size = A_num
            else:
                size = a_num
            position = (ord(char) - size - shift) % alphabet
            plaintext += chr(size + position)
        else:
            plaintext += char
    return plaintext
