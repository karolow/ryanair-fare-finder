import requests


def query_ryanair_api(
    api_url: str, params: tuple = None, max_retries: int = 3, timeout: int = 30
) -> dict:
    """Queries Ryanair API.

    The requests Session has been used to limit the number of server
    connections and automatically repeat requests if necessary.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0)\
        Gecko/20100101 Firefox/105.0"
    }
    adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
    session = requests.Session()
    session.mount("https://www.ryanair.com/api", adapter)
    response = session.get(
        api_url, headers=headers, params=params, timeout=timeout
    )
    response.raise_for_status()
    return response.json()
