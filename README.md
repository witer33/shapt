# shapt
A simple cryptographic algorithm designed and developed without a specific purpose.

Algorithm operations:

<code>last_key = sha512(key)
result += (512 bit) part of text ^ last_key

last_key = sha512(last_key)
result += (512 bit) part of text ^ last_key

...</code>

until the text ends.
