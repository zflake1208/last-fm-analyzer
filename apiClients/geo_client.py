from urllib import parse

def get_top_artists(country, limit=10, page=None):
    method = "geo.gettopartists"
    url_params = {'method': method, 'country': country}
    if page is not None:
        url_params['page'] = page
    query = parse.urlencode(url_params)
    return query

def get_top_tracks(country, location=None, limit=10, page=None):
    method = "geo.gettoptracks"
    url_params = {'method': method, 'country': country}
    if location is not None:
        url_params['location'] = location
    if page is not None:
        url_params['page'] = page
    query = parse.urlencode(url_params)
    return query
