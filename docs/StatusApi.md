# swagger_client.StatusApi

All URIs are relative to *https://fitmarket.xfer.hr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actual_state_get**](StatusApi.md#actual_state_get) | **GET** /actual_state | Dohvaca JSON sa trenutnim cijenama svih dionica.
[**mystate_get**](StatusApi.md#mystate_get) | **GET** /mystate | Dohvaca JSON koji prikazuje korisnikovu ukupnu vrijednost, neinvestiranu vrijednost i vrijednosti investirane u dionice.
[**plot_txt_get**](StatusApi.md#plot_txt_get) | **GET** /plot_txt | Dohvaca CSV sa cijenama svih dionica u svim prijasnjim mjerenjima.


# **actual_state_get**
> list[Stock] actual_state_get(token)

Dohvaca JSON sa trenutnim cijenama svih dionica.

### Example 
```python
from __future__ import print_statement
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Autorizacijski token | 

### Return type

[**list[Stock]**](Stock.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mystate_get**
> Status mystate_get(token)

Dohvaca JSON koji prikazuje korisnikovu ukupnu vrijednost, neinvestiranu vrijednost i vrijednosti investirane u dionice.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()
token = 'token_example' # str | Autorizacijski token

try: 
    # Dohvaca JSON koji prikazuje korisnikovu ukupnu vrijednost, neinvestiranu vrijednost i vrijednosti investirane u dionice.
    api_response = api_instance.mystate_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->mystate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Autorizacijski token | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_txt_get**
> file plot_txt_get(token)

Dohvaca CSV sa cijenama svih dionica u svim prijasnjim mjerenjima.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()
token = 'token_example' # str | Autorizacijski token

try: 
    # Dohvaca CSV sa cijenama svih dionica u svim prijasnjim mjerenjima.
    api_response = api_instance.plot_txt_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->plot_txt_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Autorizacijski token | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

