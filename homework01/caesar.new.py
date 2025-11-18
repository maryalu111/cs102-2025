def decrypt_poly_shift(ciphertext: str, odd_shift: int, even_shift: int) -> str:
    plaintext = ""
    alphabet = 32  # Количество букв в русском алфавите (без Ё/ё)
    text_to_decrypt = ciphertext.replace("Ё", "Е").replace("ё", "е")
    upper_a_num = ord("А")
    lower_a_num = ord("а")
    for index, elem in enumerate(text_to_decrypt):
        if "а" <= elem <= "я" or "А" <= elem <= "Я":
            register = lower_a_num if elem.islower() else upper_a_num
            shift = odd_shift if index % 2 == 1 else even_shift
            element_code = (ord(elem) - shift - register) % alphabet + register
            plaintext += chr(element_code)
        else:
            plaintext += elem

    return plaintext
