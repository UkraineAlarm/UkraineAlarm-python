# UkraineAlarm.AlertsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_alerts_get**](AlertsApi.md#api_v3_alerts_get) | **GET** /api/v3/alerts | Області, регіони та громади з тривогами
[**api_v3_alerts_region_history_get**](AlertsApi.md#api_v3_alerts_region_history_get) | **GET** /api/v3/alerts/regionHistory | Отримати останніх 25 тривог регіону
[**api_v3_alerts_region_id_get**](AlertsApi.md#api_v3_alerts_region_id_get) | **GET** /api/v3/alerts/{regionId} | Статус області/регіону/громади
[**api_v3_alerts_status_get**](AlertsApi.md#api_v3_alerts_status_get) | **GET** /api/v3/alerts/status | Перевірка номеру останньої дії. Використовувати для перевірки необхідності оновлювати дані

# **api_v3_alerts_get**
> list[AlertRegionModel] api_v3_alerts_get()

Області, регіони та громади з тривогами

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
api_instance = UkraineAlarm.AlertsApi(UkraineAlarm.ApiClient(configuration))

try:
    # Області, регіони та громади з тривогами
    api_response = api_instance.api_v3_alerts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->api_v3_alerts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertRegionModel]**](AlertRegionModel.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_alerts_region_history_get**
> list[RegionAlarmsHistory] api_v3_alerts_region_history_get(region_id=region_id)

Отримати останніх 25 тривог регіону

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
api_instance = UkraineAlarm.AlertsApi(UkraineAlarm.ApiClient(configuration))
region_id = 'region_id_example' # str |  (optional)

try:
    # Отримати останніх 25 тривог регіону
    api_response = api_instance.api_v3_alerts_region_history_get(region_id=region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->api_v3_alerts_region_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**|  | [optional] 

### Return type

[**list[RegionAlarmsHistory]**](RegionAlarmsHistory.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_alerts_region_id_get**
> list[AlertRegionModel] api_v3_alerts_region_id_get(region_id)

Статус області/регіону/громади

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
api_instance = UkraineAlarm.AlertsApi(UkraineAlarm.ApiClient(configuration))
region_id = 'region_id_example' # str | ID області/регіону/громади

try:
    # Статус області/регіону/громади
    api_response = api_instance.api_v3_alerts_region_id_get(region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->api_v3_alerts_region_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| ID області/регіону/громади | 

### Return type

[**list[AlertRegionModel]**](AlertRegionModel.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_alerts_status_get**
> AlertModification api_v3_alerts_status_get()

Перевірка номеру останньої дії. Використовувати для перевірки необхідності оновлювати дані

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
api_instance = UkraineAlarm.AlertsApi(UkraineAlarm.ApiClient(configuration))

try:
    # Перевірка номеру останньої дії. Використовувати для перевірки необхідності оновлювати дані
    api_response = api_instance.api_v3_alerts_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->api_v3_alerts_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertModification**](AlertModification.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

