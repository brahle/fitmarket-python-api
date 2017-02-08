# swagger_client.TradingApi

All URIs are relative to *https://fitmarket.xfer.hr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sell_all_post**](TradingApi.md#sell_all_post) | **POST** /sell_all | Ovaj poziv ce prodati sve dionice koje korisnik ima. Primjetite da se ovaj poziv moze implementirati koristenjem vise poziva metode \&quot;submit\&quot;.
[**submit_post**](TradingApi.md#submit_post) | **POST** /submit | Poziv mijenja korisnikov portfolio. U tijelu poruke posaljite JSON sa opisom transakcije.


# **sell_all_post**
> sell_all_post(token)

Ovaj poziv ce prodati sve dionice koje korisnik ima. Primjetite da se ovaj poziv moze implementirati koristenjem vise poziva metode \"submit\".

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
token = 'token_example' # str | Autorizacijski token

try: 
    # Ovaj poziv ce prodati sve dionice koje korisnik ima. Primjetite da se ovaj poziv moze implementirati koristenjem vise poziva metode \"submit\".
    api_instance.sell_all_post(token)
except ApiException as e:
    print("Exception when calling TradingApi->sell_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Autorizacijski token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_post**
> submit_post(token, stream_name, action, count)

Poziv mijenja korisnikov portfolio. U tijelu poruke posaljite JSON sa opisom transakcije.

Parametri su: - action je \"buy\" ili \"sell\" - stream_name ime dionice koja se kupuje (ili prefix ~ za inverznu dionicu). - count koliko dionice se zeli kupiti. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradingApi()
token = 'token_example' # str | Autorizacijski token
stream_name = 'stream_name_example' # str | ime dionice kojom se trguje (ili prefix ~ za inverznu dionicu).
action = 'action_example' # str | akcija - buy ili sell.
count = 3.4 # float | s koliko dionica se zeli trgovati.

try: 
    # Poziv mijenja korisnikov portfolio. U tijelu poruke posaljite JSON sa opisom transakcije.
    api_instance.submit_post(token, stream_name, action, count)
except ApiException as e:
    print("Exception when calling TradingApi->submit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Autorizacijski token | 
 **stream_name** | **str**| ime dionice kojom se trguje (ili prefix ~ za inverznu dionicu). | 
 **action** | **str**| akcija - buy ili sell. | 
 **count** | **float**| s koliko dionica se zeli trgovati. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

