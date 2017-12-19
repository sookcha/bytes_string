# -*- coding: utf-8 -*-
import array


class BytesString:
    def __init__(self, size):
        self.byte_arr = bytearray(size)
        self.bytes_str_arr = ['00' for x in range(size)]

    def add_string(self, text, index):
        pass

    def add_integer(self, number, index):
        text = hex(number).replace("0x", "")
        splited_arr = self.split_by_n(text, 2)
        print(list(splited_arr))

    def position(self, new_position):
        self.byte_arr.zfill(new_position)

    def get_bytearray(self):
        return self.byte_arr

    def split_by_n(self, seq, n):
        while seq:
            yield seq[:n]
            seq = seq[n:]
            seq = ("0%s" % seq) if len(seq) == 1 else seq
