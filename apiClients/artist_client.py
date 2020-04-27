from urllib import parse

def get_correction(artist):
    method = "artist.getcorrection&"
    url_params = {'method': method, 'artist': artist}
    query = parse.urlencode(url_params)
    return query


def get_info(artist, mbid=None, lang=None, autocorrect=None, username=None):
    method = "artist.getinfo"
    url_params = {'method': method, 'artist': artist}
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    if username is not None:
        url_params['username'] = username
    if lang is not None:
        url_params['lang'] = lang
    if mbid is not None:
        url_params['mbid'] = mbid
    query = parse.urlencode(url_params)
    return query


def get_similar(artist, limit=None, autocorrect=None, mbid=None):
    method = "artist.getsimilar"
    url_params = {'method': method, 'artist': artist}
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    if limit is not None:
        url_params['limit'] = limit
    if mbid is not None:
        url_params['mbid'] = mbid
    query = parse.urlencode(url_params)
    return query


def get_top_albums(artist, mbid=None, autocorrect=None, page=None, limit=None):
    method = "artist.gettopalbums"
    url_params = {'method': method, 'artist': artist}
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    if page is not None:
        url_params['page'] = page
    if limit is not None:
        url_params['limit'] = limit
    if mbid is not None:
        url_params['mbid'] = mbid
    query = parse.urlencode(url_params)
    return query


def get_top_tags(artist, mbid=None, autocorrect=None):
    method = "artist.gettoptags"
    url_params = {'method': method, 'artist': artist}
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    if mbid is not None:
        url_params['mbid'] = mbid
    query = parse.urlencode(url_params)
    return query


def get_top_tracks(artist, mbid=None, autocorrect=None, page=None, limit=None):
    method = "artist.gettoptracks"
    url_params = {'method': method, 'artist': artist}
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    if page is not None:
        url_params['page'] = page
    if limit is not None:
        url_params['limit'] = limit
    if mbid is not None:
        url_params['mbid'] = mbid
    query = parse.urlencode(url_params)
    return query


def search(artist, limit=None, page=None):
    method = "artist.search"
    url_params = {'method': method, 'artist': artist}
    if page is not None:
        url_params['page'] = page
    if limit is not None:
        url_params['limit'] = limit
    query = parse.urlencode(url_params)
    return query