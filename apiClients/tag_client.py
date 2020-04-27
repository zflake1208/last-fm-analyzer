from urllib import parse

def get_info(tag, lang=None):
    method = "tag.getinfo"
    url_params = {'method': method, 'tag': tag}
    if lang is not None:
        url_params['lang'] = lang
    query = parse.urlencode(url_params)
    return query

def get_similar(tag):
    method = "tag.getsimilar"
    url_params = {'method': method, 'tag': tag}
    query = parse.urlencode(url_params)
    return query

def get_top_albums(tag, limit=None, page=None):
    method = "tag.gettopalbums"
    url_params = {'method': method, 'tag': tag}
    if limit is not None:
        url_params['limit'] = limit
    if page is not None:
        url_params['page'] = page
    query = parse.urlencode(url_params)
    return query

def get_top_artists(tag, limit=None, page=None):
    method = "tag.gettopartists"
    url_params = {'method': method, 'tag': tag}
    if limit is not None:
        url_params['limit'] = limit
    if page is not None:
        url_params['page'] = page
    query = parse.urlencode(url_params)
    return query

def get_top_tags():
    method = "tag.gettoptags"
    url_params = {'method': method}
    query = parse.urlencode(url_params)
    return query

def get_top_tracks(tag, limit=None, page=None):
    method = "tag.gettoptracks"
    url_params = {'method': method, 'tag': tag}
    if limit is not None:
        url_params['limit'] = limit
    if page is not None:
        url_params['page'] = page
    query = parse.urlencode(url_params)
    return query

def get_weekly_chart_list(tag):
    method = "tag.getweeklychartlist"
    url_params = {'method': method, 'tag': tag}
    query = parse.urlencode(url_params)
    return query