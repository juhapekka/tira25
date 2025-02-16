def hash_value(string):
    A = 23
    M = 2**32
    result = 0
    for c in string:
        value = ord(c) - ord('a')
        result = (result * A + value) % M
    return result

def find_other(string):
    A = 23
    M = 2**32
    original_hash = hash_value(string)
    
    # Start with an empty string and build it character by character
    result = []
    current_hash = 0
    n = len(string)

    for i in range(n - 1, -1, -1):
        # Calculate the required value to achieve the target hash at this position
        target_value = (original_hash - current_hash) * pow(A, n - 1 - i, M) % M
        
        # Find the correct character that matches this target value
        char_index = target_value % 26
        
        # Append the character to the result list
        result.append(chr(char_index + ord('a')))
        
        # Update the current hash with this character's contribution
        current_hash = (current_hash * A + char_index) % M

    return ''.join(reversed(result))

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682