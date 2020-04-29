from urllib import parse
from apiClients.api_client import ApiClient

class AlbumClient(ApiClient):
    def get_info(self, album, artist, mbid=None, autocorrect=None, username=None, lang=None):
        """
        Get the metadata and tracklist for an album on Last.fm using the album name or a musicbrainz id.

        Params:
        artist (Required (unless mbid)] : The artist name
        album (Required (unless mbid)] : The album name
        mbid (Optional) : The musicbrainz id for the album
        autocorrect[0|1] (Optional) : Transform misspelled artist names into correct artist names, returning the correct version instead. 
                                        The corrected artist name will be returned in the response.
        username (Optional) : The username for the context of the request. 
                                        If supplied, the user's playcount for this album is included in the response.
        lang (Optional) : The language to return the biography in, expressed as an ISO 639 alpha-2 code.
        """
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
        """
        Get the top tags for an album on Last.fm, ordered by popularity.

        Params:
        artist (Required (unless mbid)] : The artist name
        album (Required (unless mbid)] : The album name
        autocorrect[0|1] (Optional) : Transform misspelled artist names into correct artist names, returning the correct version instead. 
                                        The corrected artist name will be returned in the response.
        mbid (Optional) : The musicbrainz id for the album
        """
        method = "album.gettoptags"
        url_params = {'method': method, 'artist': artist, 'album': album}
        if mbid is not None:
            url_params['mbid'] = mbid
        if autocorrect is not None:
            url_params['autocorrect'] = autocorrect
        query = parse.urlencode(url_params)
        return query


    def search(self, album, limit=10, page=None):
        """
        Search for an album by name. Returns album matches sorted by relevance. 

        Params:
        limit (Optional) : The number of results to fetch per page.
        page (Optional) : The page number to fetch. Defaults to first page.
        album (Required) : The album name
        """
        method = "album.search"
        url_params = {'method': method, 'album': album}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query
