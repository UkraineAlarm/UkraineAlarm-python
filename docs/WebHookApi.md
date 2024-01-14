# UkraineAlarm.WebHookApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_webhook_delete**](WebHookApi.md#api_v3_webhook_delete) | **DELETE** /api/v3/webhook | Відписка на WebHook про нові сирени та їх відбій
[**api_v3_webhook_patch**](WebHookApi.md#api_v3_webhook_patch) | **PATCH** /api/v3/webhook | Оновлення WebHook посилання про нові сирени та їх відбій
[**api_v3_webhook_post**](WebHookApi.md#api_v3_webhook_post) | **POST** /api/v3/webhook | Підписка на WebHook про нові сирени та їх відбій. У вебхукі відпрявляється подія тривоги/відбою (приклад в відповіді \&quot;200\&quot;)

# **api_v3_webhook_delete**
> api_v3_webhook_delete(body=body)

Відписка на WebHook про нові сирени та їх відбій

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
api_instance = UkraineAlarm.WebHookApi(UkraineAlarm.ApiClient(configuration))
body = UkraineAlarm.WebHookModel() # WebHookModel |  (optional)

try:
    # Відписка на WebHook про нові сирени та їх відбій
    api_instance.api_v3_webhook_delete(body=body)
except ApiException as e:
    print("Exception when calling WebHookApi->api_v3_webhook_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebHookModel**](WebHookModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_webhook_patch**
> api_v3_webhook_patch(body=body)

Оновлення WebHook посилання про нові сирени та їх відбій

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
api_instance = UkraineAlarm.WebHookApi(UkraineAlarm.ApiClient(configuration))
body = UkraineAlarm.WebHookModel() # WebHookModel |  (optional)

try:
    # Оновлення WebHook посилання про нові сирени та їх відбій
    api_instance.api_v3_webhook_patch(body=body)
except ApiException as e:
    print("Exception when calling WebHookApi->api_v3_webhook_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebHookModel**](WebHookModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_webhook_post**
> AlertRegionModel api_v3_webhook_post(body=body)

Підписка на WebHook про нові сирени та їх відбій. У вебхукі відпрявляється подія тривоги/відбою (приклад в відповіді \"200\")

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
api_instance = UkraineAlarm.WebHookApi(UkraineAlarm.ApiClient(configuration))
body = UkraineAlarm.WebHookModel() # WebHookModel |  (optional)

try:
    # Підписка на WebHook про нові сирени та їх відбій. У вебхукі відпрявляється подія тривоги/відбою (приклад в відповіді \"200\")
    api_response = api_instance.api_v3_webhook_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebHookApi->api_v3_webhook_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebHookModel**](WebHookModel.md)|  | [optional] 

### Return type

[**AlertRegionModel**](AlertRegionModel.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

