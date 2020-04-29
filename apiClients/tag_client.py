from urllib import parse
from apiClients.api_client import ApiClient

class TagClient(ApiClient):
    def get_info(self, tag, lang=None):
        """
        Get the metadata for a tag 

        Params:
        lang (Optional) : The language to return the wiki in, expressed as an ISO 639 alpha-2 code.
        tag (Required) : The tag name
        """
        method = "tag.getinfo"
        url_params = {'method': method, 'tag': tag}
        if lang is not None:
            url_params['lang'] = lang
        query = parse.urlencode(url_params)
        return query

    def get_similar(self, tag):
        """
        Search for tags similar to this one. Returns tags ranked by similarity, based on listening data.

        Params:
        tag (Required) : The tag name
        """
        method = "tag.getsimilar"
        url_params = {'method': method, 'tag': tag}
        query = parse.urlencode(url_params)
        return query

    def get_top_albums(self, tag, limit=10, page=None):
        """
        Get the top albums tagged by this tag, ordered by tag count. 

        Params:
        tag (Required) : The tag name
        limit (Optional) : The number of results to fetch per page.
        page (Optional) : The page number to fetch. Defaults to first page.
        """
        method = "tag.gettopalbums"
        url_params = {'method': method, 'tag': tag}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_artists(self, tag, limit=10, page=None):
        """
        Get the top artists tagged by this tag, ordered by tag count. 

        Params:
        tag (Required) : The tag name
        limit (Optional) : The number of results to fetch per page.
        page (Optional) : The page number to fetch. Defaults to first page.
        """
        method = "tag.gettopartists"
        url_params = {'method': method, 'tag': tag}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_tags(self):
        """
        Fetches the top global tags on Last.fm, sorted by popularity (number of times used) 
        """
        method = "tag.gettoptags"
        url_params = {'method': method}
        query = parse.urlencode(url_params)
        return query

    def get_top_tracks(self, tag, limit=10, page=None):
        """
        Get the top tracks tagged by this tag, ordered by tag count. 

        Params:
        tag (Required) : The tag name
        limit (Optional) : The number of results to fetch per page.
        page (Optional) : The page number to fetch. Defaults to first page.
        """
        method = "tag.gettoptracks"
        url_params = {'method': method, 'tag': tag}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_weekly_chart_list(self, tag):
        """
        Get a list of available charts for this tag, expressed as date ranges which can be sent to the chart services. 

        Params:
        tag (Required) : The tag name
        """
        method = "tag.getweeklychartlist"
        url_params = {'method': method, 'tag': tag}
        query = parse.urlencode(url_params)
        return query