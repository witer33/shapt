# shapt
A simple cryptographic algorithm designed and developed without a specific purpose.

Algorithm operations:

<b>last_key = sha512(key)
  
result += (512 bit) part of text ^(xor) last_key

last_key = sha512(last_key)

result += (512 bit) part of text ^(xor) last_key

...</b>

until the text ends.

The process repeats for ((len(text) * len(key)) % 16) times. (if result comes 0 it becomes 3)
