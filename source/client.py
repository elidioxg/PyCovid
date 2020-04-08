# -*- coding: utf-8 -*-

import requests
from requests.exceptions import RequestException

BASE_URL = 'https://corona.lmao.ninja/'

# Default Commands
DEFAULT_ALL = 'all'
DEFAULT_STATES = 'states'
DEFAULT_YESTERDAY = 'yesterday'

# JHU CSSE Commands
JHUCSSE = 'v2/jhucsse'
JHUCSSE_COUNTIES = 'v2/jhucsse/counties'
JHUCSSE_COUNTYNAME = 'v2/jhucsse/counties/countyName'
JHUCSSE_HISTORICAL = 'v2/historical'
JHUCSSE_ALL = 'v2/historical/all'

# Countries Commands
COUNTRIES = 'countries'

# Queries
LAST_DAYS = 'lastdays'
SORT = 'sort'

# Queries Values
CASES = 'cases'
TODAY_CASES = 'todayCases'
DEATHS = 'deaths'
TODAY_DEATHS = 'todayDeaths'
ACTIVE = 'active'
RECOVERED = 'recovered'
CRITICAL = 'critical'
CASES_PER_MILLION = 'casesPerOneMillion'
DEATHS_PER_MILLION = 'deathsPerOneMillion'

class Client:
    ''' Used for retrieving json response from NovelCOVID REST API
    '''

    def _get(self, command, path='', query='', query_value=''):
        ''' Function to send GET requests
        '''
        if type(path) == list:
            for p in path:
                path += '/'+p
            path.replace(' ', '%20')
        else:
            if path.strip() != '':
                path = '/'+path
                path.replace(' ', '%20')

        if str(query_value).strip() != '':
            query = '?'+query+'='+str(query_value)
        else:
            query = ''

        try:
            response = requests.get(BASE_URL+command+path+query)
        except RequestException as e:
            print(e)
        return response

    def get_global_totals(self):
        ''' Get global total cases
        '''
        return self._get(DEFAULT_ALL)

    def get_state_totals(self, state:str='', sort:str=''):
        ''' Get US state totals
        '''
        return self._get(DEFAULT_STATES, path=state, query=SORT, query_value=sort)

    def get_yesterday_totals(self, country:str='', sort:str=''):
        ''' Get country total cases from yesterday
        '''
        return self._get(DEFAULT_YESTERDAY, path=country, query=SORT, query_value=sort)

    def get_jhucsse(self):
        ''' Get all JHU CSSE data
        '''
        return self._get(JHUCSSE)

    def get_jhucsse_counties(self):
        ''' Get all JHU CSSE county data
        '''
        return self._get(JHUCSSE_COUNTIES)

    def get_jhucsse_county(self, county:str):
        ''' Get all JHU CSSE data by county
        '''
        return self._get(JHUCSSE_COUNTIES, path=county)

    def get_jhucsse_historical(self, country:str='', days:str=''):
        ''' Get all JHU CSSE historical data
        '''
        return self._get(JHUCSSE_HISTORICAL, path=country, query=LAST_DAYS, query_value=days)

    def get_countries_totals(self, sort:str=''):
        ''' Get all data from countries
        '''
        return self._get(COUNTRIES, query=SORT, query_value=sort)

    def get_totals_by_country(self, country:str):
        ''' Get all data from specific country
        '''
        return self._get(COUNTRIES, path=country)

    def get_totals_by_countries(self, countries:list):
        ''' Get data from list of countries
        '''
        return self._get(COUNTRIES, path=countries)

