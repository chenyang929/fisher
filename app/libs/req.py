import requests


class Http:
    @classmethod
    def get(cls, url, return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            result = r.json() if return_json else r.text
        else:
            result = {} if return_json else ''
        return result



