def shift_word_italian(word, shift, italian_alphabet):
    shifted_word = ''
    for char in word:
        if char.isalpha():  # Check if the character is alphabetic
            is_upper = char.isupper()
            char = char.lower()
            if char in italian_alphabet:
                idx = italian_alphabet.index(char)
                new_idx = (idx + shift) % len(italian_alphabet)
                new_char = italian_alphabet[new_idx]
                shifted_word += new_char.upper() if is_upper else new_char
            else:
                shifted_word += char  # For characters not in the Italian alphabet
        else:
            shifted_word += char  # Non-alphabetic characters remain unchanged
    return shifted_word

def main():
    # Italian alphabet without J, K, W, X, Y
    italian_alphabet = "abcdefghilmnopqrstuvz"
    
    user_word = input("Inserisci una parola crittografata che desideri decrittografare. Controlla le possibili combinazioni di seguito per quale suona come una parola originale: ")
    print("\nCombinazioni con spostamento:")
    for shift in range(1, len(italian_alphabet)):  # Generate shifts from 1 to 20
        shifted = shift_word_italian(user_word, shift, italian_alphabet)
        print(f"{shift} lettera spostata: {shifted}")

if __name__ == "__main__":
    main()
