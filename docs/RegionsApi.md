# UkraineAlarm.RegionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_regions_get**](RegionsApi.md#api_v3_regions_get) | **GET** /api/v3/regions | Повертає список усіх областей, регіонів та міст

# **api_v3_regions_get**
> RegionsViewModel api_v3_regions_get()

Повертає список усіх областей, регіонів та міст

### Example
```python
from __future__ import print_function
import time
import UkraineAlarm
from UkraineAlarm.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = UkraineAlarm.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = UkraineAlarm.RegionsApi(UkraineAlarm.ApiClient(configuration))

try:
    # Повертає список усіх областей, регіонів та міст
    api_response = api_instance.api_v3_regions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->api_v3_regions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegionsViewModel**](RegionsViewModel.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

