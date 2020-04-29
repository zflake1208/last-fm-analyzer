from urllib import parse
from apiClients.api_client import ApiClient

class ChartClient(ApiClient):
    def get_top_artists(self, page=None, limit=10):
        method = "chart.gettopartists"
        url_params = {'method': method}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_tags(self, page=None, limit=10):
        method = "chart.gettoptags"
        url_params = {'method': method}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_tracks(self, page=None, limit=10):
        method = "chart.gettoptracks"
        url_params = {'method': method}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query