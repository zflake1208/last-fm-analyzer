from urllib import parse
from apiClients.api_client import ApiClient

class GeoClient(ApiClient):
    def get_top_artists(self, country, limit=10, page=None):
        """
        Get the most popular artists on Last.fm by country 

        Params:
        country (Required) : A country name, as defined by the ISO 3166-1 country names standard
        limit (Optional) : The number of results to fetch per page.
        page (Optional) : The page number to fetch. Defaults to first page.
        """
        method = "geo.gettopartists"
        url_params = {'method': method, 'country': country}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_tracks(self, country, location=None, limit=10, page=None):
        """
        Get the most popular tracks on Last.fm last week by country 

        Params:
        country (Required) : A country name, as defined by the ISO 3166-1 country names standard
        location (Optional) : A metro name, to fetch the charts for (must be within the country specified)
        limit (Optional) : The number of results to fetch per page. Defaults to 50.
        page (Optional) : The page number to fetch. Defaults to first page.
        """
        method = "geo.gettoptracks"
        url_params = {'method': method, 'country': country}
        if location is not None:
            url_params['location'] = location
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query
