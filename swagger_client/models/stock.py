# coding: utf-8

"""
    Fitmarket

    Mali broj ljudi - donori - dijele dnevna mjerenja svoje težine. Iz dnevne težine jednog donora određujemo vrijednosti dviju dionica:  - dionica X ima vrijednost koja odgovara težini donora na taj dan. - inverzna dionica ~X ima vrijednost (150 kg - X).  Primjetimo da:  - kako X raste, ~X pada. - X + ~X = 150 kg  Svaki igrač počinje igru sa 10,000 kg raspoloživog novca. Igrač koristi taj novac za trgovanje dionicama. Ukupna vrijednost igrača je zbroj rapoloživog novca i aktualne vrijednosti svih dionica koje posjeduje. Cilj igre je maksimizirati ukupnu vrijednost dobrim predviđanjem kretanja vrijednosti dionica. Na primjer, u prvom danu igrac kupi 125 dionica \"X\" za 80 kg. U drugom danu, dionica naraste na 82 kg. Ako igrac proda sve dionice \"X\", zaradio je 2 kg * 125 = 250 kg!  Igra ne dopušta donoru da trguje vlastitim dionicama. 

    OpenAPI spec version: 1.0.2
    
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

from pprint import pformat
from six import iteritems
import re


class Stock(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, stream_name=None, latest_weight=None):
        """
        Stock - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'stream_name': 'str',
            'latest_weight': 'float'
        }

        self.attribute_map = {
            'stream_name': 'stream_name',
            'latest_weight': 'latest_weight'
        }

        self._stream_name = stream_name
        self._latest_weight = latest_weight


    @property
    def stream_name(self):
        """
        Gets the stream_name of this Stock.


        :return: The stream_name of this Stock.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this Stock.


        :param stream_name: The stream_name of this Stock.
        :type: str
        """
        if stream_name is None:
            raise ValueError("Invalid value for `stream_name`, must not be `None`")

        self._stream_name = stream_name

    @property
    def latest_weight(self):
        """
        Gets the latest_weight of this Stock.


        :return: The latest_weight of this Stock.
        :rtype: float
        """
        return self._latest_weight

    @latest_weight.setter
    def latest_weight(self, latest_weight):
        """
        Sets the latest_weight of this Stock.


        :param latest_weight: The latest_weight of this Stock.
        :type: float
        """
        if latest_weight is None:
            raise ValueError("Invalid value for `latest_weight`, must not be `None`")

        self._latest_weight = latest_weight

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
