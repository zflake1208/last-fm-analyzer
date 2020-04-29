from urllib import parse
from apiClients.api_client import ApiClient

class AlbumClient(ApiClient):
    def get_info(self, album, artist, mbid=None, autocorrect=None, username=None, lang=None):
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


    def get_top_tags(self, album, artist, autocorrect=None, mbid=None):
        method = "album.gettoptags"
        url_params = {'method': method, 'artist': artist, 'album': album}
        if mbid is not None:
            url_params['mbid'] = mbid
        if autocorrect is not None:
            url_params['autocorrect'] = autocorrect
        query = parse.urlencode(url_params)
        return query


    def search(self, album, limit=10, page=None):
        method = "album.search"
        url_params = {'method': method, 'album': album}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query
