# bytes_string
Manipulate bytestring on Python, without hassle.

## Usage

        bytes = BytesString(64)
        
        offset = 0
        bytes.add_integer(100, offset)

        offset += 4
        bytes.add_integer(100, offset)

        offset += 4
        bytes.add_integer(0, offset)

        bytes.add_string("Good", offset + 1, "ASCII")
        offset += BytesString

        print(bytes.get_bytearray())
