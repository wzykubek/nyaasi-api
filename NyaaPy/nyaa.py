import requests

from NyaaPy import utils


class Nyaa:

    def __init__(self):
        self.SITE = utils.TorrentSite.NYAASI
        self.URL = "https://nyaa.si"

    def last_uploads(self, number_of_results):
        r = requests.get(self.URL)

        # If anything up with nyaa servers let the user know.
        r.raise_for_status()

        json_data = utils.parse_nyaa(
            request_text=r.text,
            limit=number_of_results + 1,
            site=self.SITE
        )
        return json_data

    def search(self, keyword, **kwargs):
        url = self.URL

        user = kwargs.get('user', None)
        category = kwargs.get('category', 0)
        subcategory = kwargs.get('subcategory', 0)
        filters = kwargs.get('filters', 0)
        page = kwargs.get('page', 0)
        sort = kwargs.get('sort', 'id')
        order = kwargs.get('order', 'desc')

        if user:
            user_uri = f"user/{user}"
        else:
            user_uri = ""

        if page > 0:
            r = requests.get(
                f"{url}/{user_uri}?f={filters}&c={category}_{subcategory}&q={keyword}&p={page}&s={sort}&o={order}")
        else:
            r = requests.get(
                f"{url}/{user_uri}?f={filters}&c={category}_{subcategory}&q={keyword}&p={page}&s={sort}&o={order}")

        r.raise_for_status()

        json_data = utils.parse_nyaa(
            request_text=r.text,
            limit=None,
            site=self.SITE
        )

        return json_data

    def get(self, view_id):
        r = requests.get(f'{self.URL}/view/{view_id}')
        r.raise_for_status()

        json_data = utils.parse_single(request_text=r.text, site=self.SITE)

        return json_data

    def get_user(self, username):
        r = requests.get(f'{self.URL}/user/{username}')
        r.raise_for_status()

        json_data = utils.parse_nyaa(
            request_text=r.text,
            limit=None,
            site=self.SITE
        )
        return json_data
