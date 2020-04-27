from urllib import parse

def get_top_artists(page=None, limit=None):
    method = "chart.gettopartists"
    url_params = {'method': method}
    if page is not None:
        url_params['page'] = page
    if limit is not None:
        url_params['limit'] = limit
    query = parse.urlencode(url_params)
    return query

def get_top_tags(page=None, limit=None):
    method = "chart.gettoptags"
    url_params = {'method': method}
    if page is not None:
        url_params['page'] = page
    if limit is not None:
        url_params['limit'] = limit
    query = parse.urlencode(url_params)
    return query

def get_top_tracks(page=None, limit=None):
    method = "chart.gettoptracks"
    url_params = {'method': method}
    if page is not None:
        url_params['page'] = page
    if limit is not None:
        url_params['limit'] = limit
    query = parse.urlencode(url_params)
    return query