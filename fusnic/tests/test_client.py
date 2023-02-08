
import os
import sys
import datetime
import logging
import unittest

from fusnic.tests.utils import *
import fusnic


class TestClient(unittest.TestCase):

    @classmethod
    @frequency_limit
    def setUpClass(cls):

        cls.invalid = 'Invalid93#!'
        cls.user, cls.password = credentials()

        # Create session and login
        cls.session = fusnic.Session(user=cls.user, password=cls.password)
        cls.session.login()

    @classmethod
    @frequency_limit
    def tearDownClass(cls):
        cls.session.logout()

    def test_login_failed_request(self):
        with self.assertRaises(fusnic.LoginFailed) as context:
            session = fusnic.Session(user=self.invalid, password=self.invalid)
            with fusnic.Client(session=session) as client:
                plants = client.get_plant_list()

    @frequency_limit
    def test_request(self):
        with fusnic.Client(session=self.session) as client:
            now = datetime.datetime.now()
            plants = client.get_plant_list()

            # Extract the list of plants code
            plants_code = [plant['stationCode'] for plant in plants]

            # Query realtime KPIs
            realtime = client.get_plant_realtime_data(plants_code)
            self.assertGreaterEqual(len(plants_code), len(realtime))

            # Hourly data, with non existing
            hourly = client.get_plant_hourly_data(
                plants_code + ['do_not_exist'], now)

            # Daily data, with a plants list bigger than 100
            daily = client.get_plant_daily_data(
                list(map(str, range(46))) + plants_code + list(map(str, range(88))), now)

            # Monthly data
            monthly = client.get_plant_monthly_data(plants_code, now)

            # Yearly data
            yearly = client.get_plant_yearly_data(plants_code, now)


if __name__ == '__main__':
    unittest.main()
