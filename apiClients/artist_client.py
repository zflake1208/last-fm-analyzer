from urllib import parse
from apiClients.api_client import ApiClient

class ArtistClient(ApiClient):
    def get_correction(self, artist):
        """
        Use the last.fm corrections data to check whether the supplied artist has a correction to a canonical artist

        Params:
        artist (Required) : The artist name to correct.
        """
        method = "artist.getcorrection&"
        url_params = {'method': method, 'artist': artist}
        query = parse.urlencode(url_params)
        return query


    def get_info(self, artist, mbid=None, lang=None, autocorrect=None, username=None):
        """
        Get the metadata for an artist. Includes biography, truncated at 300 characters.

        Params:
        artist (Required (unless mbid)] : The artist name
        mbid (Optional) : The musicbrainz id for the artist
        lang (Optional) : The language to return the biography in, expressed as an ISO 639 alpha-2 code.
        autocorrect[0|1] (Optional) : Transform misspelled artist names into correct artist names, returning the correct version instead. 
                                        The corrected artist name will be returned in the response.
        username (Optional) : The username for the context of the request. 
                                        If supplied, the user's playcount for this artist is included in the response.
        """
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


    def get_similar(self, artist, limit=10, autocorrect=None, mbid=None):
        """
        Get all the artists similar to this artist 

        Params:
        limit (Optional) : Limit the number of similar artists returned
        artist (Required (unless mbid)] : The artist name
        autocorrect[0|1] (Optional) : Transform misspelled artist names into correct artist names, returning the correct version instead. 
                                        The corrected artist name will be returned in the response.
        mbid (Optional) : The musicbrainz id for the artist
        """
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


    def get_top_albums(self, artist, mbid=None, autocorrect=None, page=None, limit=10):
        """
        Get the top albums for an artist on Last.fm, ordered by popularity. 

        Params:
        artist (Required (unless mbid)] : The artist name
        mbid (Optional) : The musicbrainz id for the artist
        autocorrect[0|1] (Optional) : Transform misspelled artist names into correct artist names, returning the correct version instead.
                                         The corrected artist name will be returned in the response.
        page (Optional) : The page number to fetch. Defaults to first page.
        limit (Optional) : The number of results to fetch per page.
        """
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


    def get_top_tags(self, artist, mbid=None, autocorrect=None):
        """
        Get the top tags for an artist on Last.fm, ordered by popularity. 

        Params:
        artist (Required (unless mbid)] : The artist name
        mbid (Optional) : The musicbrainz id for the artist
        autocorrect[0|1] (Optional) : Transform misspelled artist names into correct artist names, returning the correct version instead. 
                                        The corrected artist name will be returned in the response.
        """
        method = "artist.gettoptags"
        url_params = {'method': method, 'artist': artist}
        if autocorrect is not None:
            url_params['autocorrect'] = autocorrect
        if mbid is not None:
            url_params['mbid'] = mbid
        query = parse.urlencode(url_params)
        return query


    def get_top_tracks(self, artist, mbid=None, autocorrect=None, page=None, limit=10):
        """
        Get the top tracks by an artist on Last.fm, ordered by popularity 

        Params:
        artist (Required (unless mbid)] : The artist name
        mbid (Optional) : The musicbrainz id for the artist
        autocorrect[0|1] (Optional) : Transform misspelled artist names into correct artist names, returning the correct version instead. 
                                        The corrected artist name will be returned in the response.
        page (Optional) : The page number to fetch. Defaults to first page.
        limit (Optional) : The number of results to fetch per page.
        """
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


    def search(self, artist, limit=10, page=None):
        """
        Search for an artist by name. Returns artist matches sorted by relevance. 

        Params:
        limit (Optional) : The number of results to fetch per page.
        limit (Optional) : The number of results to fetch per page.
        page (Optional) : The page number to fetch. Defaults to first page.
        artist (Required) : The artist name
        """
        method = "artist.search"
        url_params = {'method': method, 'artist': artist}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query