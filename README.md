# UkraineAlarm - the Python library for the [Ukraine Alert API](https://api.ukrainealarm.com/)

- API version: 3.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import UkraineAlarm 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import UkraineAlarm
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertsApi* | [**api_v3_alerts_get**](docs/AlertsApi.md#api_v3_alerts_get) | **GET** /api/v3/alerts | Області, регіони та громади з тривогами
*AlertsApi* | [**api_v3_alerts_region_history_get**](docs/AlertsApi.md#api_v3_alerts_region_history_get) | **GET** /api/v3/alerts/regionHistory | Отримати останніх 25 тривог регіону
*AlertsApi* | [**api_v3_alerts_region_id_get**](docs/AlertsApi.md#api_v3_alerts_region_id_get) | **GET** /api/v3/alerts/{regionId} | Статус області/регіону/громади
*AlertsApi* | [**api_v3_alerts_status_get**](docs/AlertsApi.md#api_v3_alerts_status_get) | **GET** /api/v3/alerts/status | Перевірка номеру останньої дії. Використовувати для перевірки необхідності оновлювати дані
*RegionsApi* | [**api_v3_regions_get**](docs/RegionsApi.md#api_v3_regions_get) | **GET** /api/v3/regions | Повертає список усіх областей, регіонів та міст
*WebHookApi* | [**api_v3_webhook_delete**](docs/WebHookApi.md#api_v3_webhook_delete) | **DELETE** /api/v3/webhook | Відписка на WebHook про нові сирени та їх відбій
*WebHookApi* | [**api_v3_webhook_patch**](docs/WebHookApi.md#api_v3_webhook_patch) | **PATCH** /api/v3/webhook | Оновлення WebHook посилання про нові сирени та їх відбій
*WebHookApi* | [**api_v3_webhook_post**](docs/WebHookApi.md#api_v3_webhook_post) | **POST** /api/v3/webhook | Підписка на WebHook про нові сирени та їх відбій. У вебхукі відпрявляється подія тривоги/відбою (приклад в відповіді \&quot;200\&quot;)

## Documentation For Models

 - [Alert](docs/Alert.md)
 - [AlertModification](docs/AlertModification.md)
 - [AlertRegionModel](docs/AlertRegionModel.md)
 - [AlertType](docs/AlertType.md)
 - [RegionAlarmModel](docs/RegionAlarmModel.md)
 - [RegionAlarmsHistory](docs/RegionAlarmsHistory.md)
 - [RegionViewModel](docs/RegionViewModel.md)
 - [RegionsViewModel](docs/RegionsViewModel.md)
 - [TimeSpan](docs/TimeSpan.md)
 - [V2RegionType](docs/V2RegionType.md)
 - [WebHookModel](docs/WebHookModel.md)

## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@stfalcon.com
