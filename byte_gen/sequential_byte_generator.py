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

from .converters import byte_str_to_int, int_to_byte_str_leading_zeroes


class SequentialByteGenerator(object):

    def __init__(self, size, start="\x00"):
        self._current_integer = byte_str_to_int(start)
        self._size = size

    def get_next(self):
        byte_str = int_to_byte_str_leading_zeroes(self._current_integer, self._size)
        self._current_integer += 1
        return byte_str
