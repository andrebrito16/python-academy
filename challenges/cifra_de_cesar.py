
ENCRYPT = 1
DECRYPT = -1

def caesar(data, key, mode):
  alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
  new_data = ''
  for c in data:
    index = alphabet.find(c)
    if index == -1:
      new_data += c
    else:
      if mode == ENCRYPT:
        new_index = index + key
        new_index = new_index % len(alphabet)
      else:
        new_index = index - key
        new_index = new_index % len(alphabet)
      new_data += alphabet[new_index]
  
  return new_data

key = 4
original = "Insper"
chiprhered = caesar(original, key, ENCRYPT)
print(chiprhered)

plain = caesar(chiprhered, key, DECRYPT)
print(plain)