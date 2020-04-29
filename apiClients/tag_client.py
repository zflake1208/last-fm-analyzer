from urllib import parse
from apiClients.api_client import ApiClient

class TagClient(ApiClient):
    def get_info(self, tag, lang=None):
        method = "tag.getinfo"
        url_params = {'method': method, 'tag': tag}
        if lang is not None:
            url_params['lang'] = lang
        query = parse.urlencode(url_params)
        return query

    def get_similar(self, tag):
        method = "tag.getsimilar"
        url_params = {'method': method, 'tag': tag}
        query = parse.urlencode(url_params)
        return query

    def get_top_albums(self, tag, limit=10, page=None):
        method = "tag.gettopalbums"
        url_params = {'method': method, 'tag': tag}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_artists(self, tag, limit=10, page=None):
        method = "tag.gettopartists"
        url_params = {'method': method, 'tag': tag}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_top_tags(self):
        method = "tag.gettoptags"
        url_params = {'method': method}
        query = parse.urlencode(url_params)
        return query

    def get_top_tracks(self, tag, limit=10, page=None):
        method = "tag.gettoptracks"
        url_params = {'method': method, 'tag': tag}
        if page is not None:
            url_params['page'] = page
        if limit is not None:
            url_params['limit'] = limit
        query = parse.urlencode(url_params)
        return query

    def get_weekly_chart_list(self, tag):
        method = "tag.getweeklychartlist"
        url_params = {'method': method, 'tag': tag}
        query = parse.urlencode(url_params)
        return query