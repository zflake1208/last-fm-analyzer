from urllib import parse

def get_info(artist, album, mbid=None, autocorrect=None, username=None, lang=None):
    method = "album.getinfo"
    url_params = {'method': method, 'artist': artist, 'album': album}
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    if username is not None:
        url_params['username'] = username
    if lang is not None:
        url_params['lang'] = lang
    query = parse.urlencode(url_params)
    return query


def get_tags(artist, album, mbid=None, autocorrect=None, user=None):
    method = "album.gettags"
    url_params = {'method': method, 'artist': artist, 'album': album}
    if mbid is not None:
        url_params['mbid'] = mbid
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    if user is not None:
        url_params['user'] = user
    query = parse.urlencode(url_params)
    return query


def get_top_tags(artist, album, autocorrect=None, mbid=None):
    method = "album.gettoptags"
    url_params = {'method': method, 'artist': artist, 'album': album}
    if mbid is not None:
        url_params['mbid'] = mbid
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    query = parse.urlencode(url_params)
    return query


def search(album, limit=None, page=None):
    method = "album.search"
    url_params = {'method': method, 'album': album}
    if limit is not None:
        url_params['limit'] = limit
    if page is not None:
        url_params['page'] = page
    query = parse.urlencode(url_params)
    return query
