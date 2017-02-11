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


class SequentialByteGenerator(object):

    def __init__(self, size, start="\x00"):
        self._current_integer = byte_str_to_int(start)
        self._size = size

    def get_next(self):
        byte_str = ""
        local_chr = chr
        to_convert = self._current_integer

        while to_convert:
            byte_str = local_chr(to_convert%256) + byte_str
            to_convert >>= 8

        self._current_integer += 1
        return byte_str.rjust(self._size, "\x00")
