# Copyright 2017 Taylor DeHaan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import array


def byte_str_to_int(byte_str):
    str_len = len(byte_str)
    result = 0
    shift = 0

    for byte in map(ord, byte_str):
        shift += 1
        result += byte << ((str_len - shift) * 8)

    return result


def int_to_byte_str_leading_zeroes(integer, size):
    """Optimized for byte strings with leading zeroes"""
    byte_str = ""
    local_chr = chr

    while integer:
        byte_str = local_chr(integer%256) + byte_str
        integer >>= 8

    return byte_str.rjust(size, "\x00")


def int_to_byte_str_non_zero(integer, size):
    """Optimized for byte string with a majority of non-zero bytes"""
    byte_list = []

    while integer:
        byte_list.append(integer%256)
        integer >>= 8

    byte_list.reverse()
    return array.array('B', byte_list).tostring().rjust(size, "\x00")


def int_to_byte_str_mixed(integer, size):
    """
    Optimized for byte strings with leading non-zero bytes, zeroes in the
    middle, and non-zero bytes at the end
    """
    upper_byte_str = ""
    lower_byte_str = ""
    local_chr = chr
    n_bytes = 0

    while True:
        x = 1 << (8 * (size - n_bytes - 1))
        r = integer / x

        if r == 0:
            break
        else:
            upper_byte_str = local_chr(r) + upper_byte_str
            integer -= x
            n_bytes += 1

    while integer:
        lower_byte_str = local_chr(integer%256) + lower_byte_str
        integer >>= 8
        n_bytes += 1

    return upper_byte_str + (size - n_bytes) * "\x00" + lower_byte_str


def int_to_byte_str_zero_groupings(integer, size):
    """Optimized for keys with large groupings of zeroes"""
    byte_str = ""
    n_zeroes = 0
    local_chr = chr

    while integer:
        r = integer % 256
        integer >>= 8
        if r == 0:
            n_zeroes += 1
        elif n_zeroes > 0:
            byte_str = local_chr(r) + \
                       byte_str.rjust(len(byte_str) + n_zeroes, "\x00")
            n_zeroes = 0
        else:
            byte_str = local_chr(r) + byte_str

    return byte_str.rjust(size, "\x00")
