# -*- coding: utf-8 -*-

import pandas as pd
import json
from pandas.io.json import json_normalize # deprecated
#from pandas import json_normalize
from client import Client

class DataClient(Client):

    def _return(self, response):
        if response.ok:
            return json_normalize(json.loads(response.text))
        else:
            return pd.DataFrame({
                'Status Code':response.status_code,
                'Reason': response.reason}, 
                index=[0])

    def get_global_totals(self):
        return self._return(super().get_global_totals())

    def get_state_totals(self, state='', sort=''):
        return self._return(super().get_state_totals(state, sort))

    def get_yesterday_totals(self, country='', sort=''):
        return self._return(super().get_yesterday_totals(country, sort))

    def get_jhucsse(self):
        return self._return(super().get_jhucsse())

    def get_jhucsse_counties(self):
        return self._return(super().get_jhucsse_counties())

    def get_jhucsse_county(self, county):
        return self._return(super().get_jhucsse_county(county))

    def get_jhucsse_historical(self, country='', days=''):
        return self._return(super().get_jhucsse_historical(country, days))

    def get_countries_totals(self, sort=''):
        return self._return(super().get_countries_totals(sort))

    def get_totals_by_country(self, country):
        return self._return(super().get_totals_by_country(country))

    def get_totals_by_countries(countries):
        return self._return(super().get_totals_by_countries(countries))

