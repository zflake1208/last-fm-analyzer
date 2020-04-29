from urllib import parse
from apiClients.api_client import ApiClient

class TrackClient(ApiClient):
    def get_correction(self, track, artist):
        """
        Use the last.fm corrections data to check whether the supplied track has a correction to a canonical track 

        Params:
        artist (Required) : The artist name to correct.
        track (Required) : The track name to correct.
        """
        method = "track.getcorrection"
        url_params = {'method': method, 'track': track, 'artist': artist}
        query = parse.urlencode(url_params)
        return query

    def get_info(self, track, artist, mbid=None, username=None, autocorrect=None):
        """
        Get the metadata for a track on Last.fm using the artist/track name or a musicbrainz id. 

        Params:
        mbid (Optional) : The musicbrainz id for the track
        track (Required (unless mbid)] : The track name
        artist (Required (unless mbid)] : The artist name
        username (Optional) : The username for the context of the request. 
                                If supplied, the user's playcount for this track and whether they have loved the track is included in the response.
        autocorrect[0|1] (Optional) : Transform misspelled artist and track names into correct artist and track names, returning the correct version instead. 
                                        The corrected artist and track name will be returned in the response.
        """
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

    def get_similar(self, track, artist, mbid=None, autocorrect=None, limit=10):
        """
        Get the similar tracks for this track on Last.fm, based on listening data. 

        Params:
        track (Required (unless mbid)] : The track name
        artist (Required (unless mbid)] : The artist name
        mbid (Optional) : The musicbrainz id for the track
        autocorrect[0|1] (Optional) : Transform misspelled artist and track names into correct artist and track names, returning the correct version instead. 
                                        The corrected artist and track name will be returned in the response.
        limit (Optional) : Maximum number of similar tracks to return
        """
        method = "track.getsimilar"
        url_params = {'method': method, 'track': track, 'artist': artist}
        if mbid is not None:
            url_params['mbid'] = mbid
        if autocorrect is not None:
            url_params['autocorrect'] = autocorrect
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_tags(self, track, artist, mbid=None, autocorrect=None):
        """
        Get the top tags for this track on Last.fm, ordered by tag count. Supply either track & artist name or mbid. 

        Params:
        track (Required (unless mbid)] : The track name
        artist (Required (unless mbid)] : The artist name
        mbid (Optional) : The musicbrainz id for the track
        autocorrect[0|1] (Optional) : Transform misspelled artist and track names into correct artist and track names, returning the correct version instead. 
                                        The corrected artist and track name will be returned in the response.
        """
        method = "track.gettoptags"
        url_params = {'method': method, 'track': track, 'artist': artist}
        if mbid is not None:
            url_params['mbid'] = mbid
        if autocorrect is not None:
            url_params['autocorrect'] = autocorrect
        query = parse.urlencode(url_params)
        return query

    def search(self, track, artist=None, limit=10, page=None):
        """
        Search for a track by track name. Returns track matches sorted by relevance. 

        Params:
        limit (Optional) : The number of results to fetch per page.
        page (Optional) : The page number to fetch. Defaults to first page.
        track (Required) : The track name
        artist (Optional) : Narrow your search by specifying an artist.
        """
        method = "track.search"
        url_params = {'method': method, 'track': track}
        if artist is not None:
            url_params['artist'] = artist
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query
