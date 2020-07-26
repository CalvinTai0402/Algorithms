# O(N) T O(N) S
def caesarCipherEncryptor(string, key):
    key = key % 26
    result = []
    for i in range(len(string)):
        if ord(string[i]) + key <= ord("z"):
            result.append(chr(ord(string[i]) + key))
        else:
            result.append(chr(-1 + ord("a") + (ord(string[i]) + key) % ord("z")))
    return "".join(result)
