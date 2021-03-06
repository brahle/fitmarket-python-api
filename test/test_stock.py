# coding: utf-8

"""
    Fitmarket

    Mali broj ljudi - donori - dijele dnevna mjerenja svoje težine.  Iz dnevne težine jednog donora određujemo vrijednosti dviju dionica:  - dionica X ima vrijednost koja odgovara težini donora na taj dan. - inverzna dionica ~X ima vrijednost (150 kg - X).  Primjetimo da:  - kako X raste, ~X pada. - X + ~X = 150 kg  Svaki igrač počinje igru sa 10,000 kg raspoloživog novca. Igrač koristi taj novac za trgovanje dionicama. Ukupna vrijednost igrača je zbroj rapoloživog novca i aktualne vrijednosti svih dionica koje posjeduje. Cilj igre je maksimizirati ukupnu vrijednost dobrim predviđanjem kretanja vrijednosti dionica. Na primjer, u prvom danu igrac kupi 125 dionica \"X\" za 80 kg. U drugom danu, dionica naraste na 82 kg. Ako igrac proda sve dionice \"X\", zaradio je 2 kg * 125 = 250 kg!  Igra ne dopušta donoru da trguje vlastitim dionicama. 

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import fitmarket_api
from fitmarket_api.rest import ApiException
from fitmarket_api.models.stock import Stock


class TestStock(unittest.TestCase):
    """ Stock unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStock(self):
        """
        Test Stock
        """
        model = fitmarket_api.models.stock.Stock()


if __name__ == '__main__':
    unittest.main()
