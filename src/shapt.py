import hashlib
import sys
import base64

class shapt:

    def encode_step(text, key):
        index = 0
        max_index = 127
        output = ""
        hkey = hashlib.sha512(key.encode()).hexdigest()
        for c in text:
            index += 1
            if index > max_index:
                index = 0
                hkey = hashlib.sha512(hkey.encode()).hexdigest()
            output += chr(ord(hkey[index]) ^ ord(c))
        return output, hkey

    def encode(text, key):
        output = text
        last_key = key
        der = (len(text) * len(key)) % 16
        der = (3 if der == 0 else der)
        for _ in range(der):
            output, last_key = shapt.encode_step(output, last_key)
        return output

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("use encode (key) (text) or decode (key) (cryptogram).")
    elif sys.argv[1] == "encode":
        text = " ".join(sys.argv[3:])
        key = sys.argv[2]

        output = shapt.encode(text, key)

        print(base64.b64encode(output.encode()).decode())
    elif sys.argv[1] == "decode":
        text = " ".join(sys.argv[3:])
        key = sys.argv[2]

        output = shapt.encode(base64.b64decode(text.encode()).decode(), key)

        print(output)
