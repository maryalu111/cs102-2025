def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    alphabet = 26  # 26 - количество букв в английском алфавите
    A_num = ord("A")
    a_num = ord("a")
    for char in plaintext:
        if char.isalpha():
            size = A_num if char.isupper() else a_num
            position = (ord(char) - size + shift) % alphabet
            ciphertext += chr(size + position)
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    alphabet = 26  # 26 - количество букв в английском алфавите
    A_num = ord("A")
    a_num = ord("a")
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                size = A_num
            else:
                size = a_num
            position = (ord(char) - size - shift) % alphabet
            plaintext += chr(size + position)
        else:
            plaintext += char
    return plaintext
