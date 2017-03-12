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

import random


class RandomByteGenerator(object):

    def __init__(self, size, seed, random_size=False):
        self._choices = [chr(i) for i in range(256)]
        self._size = size
        self._random_size = random_size
        self._random_gen = random.Random(seed)

    def _size_range(self):
        if self._random_size:
            return range(self._random_gen.randint(1, self._size))
        else:
            return range(self._size)

    def get_next(self):
        return ''.join(self._random_gen.choice(self._choices) for _ in self._size_range())
