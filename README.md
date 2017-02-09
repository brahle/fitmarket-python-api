# swagger_client
Mali broj ljudi - donori - dijele dnevna mjerenja svoje težine. Iz dnevne težine jednog donora određujemo vrijednosti dviju dionica:  - dionica X ima vrijednost koja odgovara težini donora na taj dan. - inverzna dionica ~X ima vrijednost (150 kg - X).  Primjetimo da:  - kako X raste, ~X pada. - X + ~X = 150 kg  Svaki igrač počinje igru sa 10,000 kg raspoloživog novca. Igrač koristi taj novac za trgovanje dionicama. Ukupna vrijednost igrača je zbroj rapoloživog novca i aktualne vrijednosti svih dionica koje posjeduje. Cilj igre je maksimizirati ukupnu vrijednost dobrim predviđanjem kretanja vrijednosti dionica. Na primjer, u prvom danu igrac kupi 125 dionica \"X\" za 80 kg. U drugom danu, dionica naraste na 82 kg. Ako igrac proda sve dionice \"X\", zaradio je 2 kg * 125 = 250 kg!  Igra ne dopušta donoru da trguje vlastitim dionicama. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/brahle/fitmarket-python-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/brahle/fitmarket-python-api.git`)

Then import the package:
```python
import swagger_client 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.StatusApi()
token = 'token_example' # str | Autorizacijski token

try:
    # Dohvaca JSON sa trenutnim cijenama svih dionica.
    api_response = api_instance.actual_state_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->actual_state_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://fitmarket.xfer.hr/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*StatusApi* | [**actual_state_get**](docs/StatusApi.md#actual_state_get) | **GET** /actual_state | Dohvaca JSON sa trenutnim cijenama svih dionica.
*StatusApi* | [**mystate_get**](docs/StatusApi.md#mystate_get) | **GET** /mystate | Dohvaca JSON koji prikazuje korisnikovu ukupnu vrijednost, neinvestiranu vrijednost i vrijednosti investirane u dionice.
*StatusApi* | [**plot_txt_get**](docs/StatusApi.md#plot_txt_get) | **GET** /plot_txt | Dohvaca CSV sa cijenama svih dionica u svim prijasnjim mjerenjima.
*TradingApi* | [**sell_all_post**](docs/TradingApi.md#sell_all_post) | **POST** /sell_all | Ovaj poziv ce prodati sve dionice koje korisnik ima. Primjetite da se ovaj poziv moze implementirati koristenjem vise poziva metode \&quot;submit\&quot;.
*TradingApi* | [**submit_post**](docs/TradingApi.md#submit_post) | **POST** /submit | Poziv mijenja korisnikov portfolio. U tijelu poruke posaljite JSON sa opisom transakcije.


## Documentation For Models

 - [Status](docs/Status.md)
 - [Stock](docs/Stock.md)
 - [StockWithCount](docs/StockWithCount.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



