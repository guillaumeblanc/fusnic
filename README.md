# FusionSolar Northbound Interface Client

Provides a Python API to access Huawei FusionSolar web service to download SmartPVMS data.
To login you need account on Huawei FusionSolar https://intl.fusionsolar.huawei.com.
Queried data are return as-is. Please refer to Huawei SmartPVMS [Northbound Interface Reference V6](https://support.huawei.com/enterprise/en/doc/EDOC1100261860) documentation for more details about data format.

# Usage

```python
import fusnic

try:
    with fusnic.ClientSession(user='user', password='password') as client:
        plants = client.get_plant_list()
        print(plants)
except fusnic.LoginFailed:
    logging.error(
        'Login failed. Verify user and password of Northbound API account.')
```

For more details about how to use the API, please check [how_to.py](how_to.py).

# Running tests

Testing requires a valid Northbound API account. Tests will look for two environment variables to get user account (FUSIONSOLAR_USER) and password (FUSIONSOLAR_PASSWORD).

Use the following command from directory root to run the tests:
```console
python3 -m unittest discover
```

# Using CI

In case of a fork, these same variables (FUSIONSOLAR_USER and FUSIONSOLAR_PASSWORD) shall be added to github secrets in order for the CI to work.
