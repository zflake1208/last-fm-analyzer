from urllib import parse

def get_correction(track, artist):
    method = "track.getcorrection"
    url_params = {'method': method, 'track': track, 'artist': artist}
    query = parse.urlencode(url_params)
    return query

def get_info(track, artist, mbid=None, username=None, autocorrect=None):
    method = "track.getinfo"
    url_params = {'method': method, 'track': track, 'artist': artist}
    if mbid is not None:
        url_params['mbid'] = mbid
    if username is not None:
        url_params['username'] = username
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    query = parse.urlencode(url_params)
    return query

def get_similar(track, artist, mbid=None, autocorrect=None, limit=None):
    method = "track.getsimilar"
    url_params = {'method': method, 'track': track, 'artist': artist}
    if mbid is not None:
        url_params['mbid'] = mbid
    if limit is not None:
        url_params['limit'] = limit
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    query = parse.urlencode(url_params)
    return query

def get_tags(track, artist, mbid=None, autocorrect=None, user=None):
    method = "track.gettags"
    url_params = {'method': method, 'track': track, 'artist': artist}
    if mbid is not None:
        url_params['mbid'] = mbid
    if user is not None:
        url_params['user'] = user
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    query = parse.urlencode(url_params)
    return query

def get_top_tags(track, artist, mbid=None, autocorrect=None):
    method = "track.gettoptags"
    url_params = {'method': method, 'track': track, 'artist': artist}
    if mbid is not None:
        url_params['mbid'] = mbid
    if autocorrect is not None:
        url_params['autocorrect'] = autocorrect
    query = parse.urlencode(url_params)
    return query

def search(track, artist=None, limit=None, page=None):
    method = "track.search"
    url_params = {'method': method, 'track': track}
    if artist is not None:
        url_params['artist'] = artist
    if limit is not None:
        url_params['limit'] = limit
    if page is not None:
        url_params['page'] = page
    query = parse.urlencode(url_params)
    return query
