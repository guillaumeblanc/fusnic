import fusnic
import os
import logging
from datetime import datetime, timezone


user = os.environ.get('FUSIONSOLAR_USER', 'unknown_user')
password = os.environ.get('FUSIONSOLAR_PASSWORD', 'unknown_password')

'''
Demonstrates how to log in FusionSolar and query plants list.
'''

try:
    with fusnic.ClientSession(user=user, password=password) as client:
        plants = client.get_plant_list()
        print('Plants list:\n' + str(plants))

        # Extract list of plant codes
        plants_code = [plant['stationCode'] for plant in plants]

        # Query latest hourly data for all plants
        hourly = client.get_plant_hourly_data(
            plants_code, datetime.now(timezone.utc))
        print('Hourly KPIs:\n' + str(hourly))

except fusnic.LoginFailed:
    logging.error(
        'Login failed. Verify user and password of Northbound API account.')
except fusnic.FrequencyLimit:
    logging.error('FusionSolar interface access frequency is too high.')
