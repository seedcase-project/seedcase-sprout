from requests import get


def scrape_url(url: str) -> dict:
    """Scrapes a URL with a JSON object.

    Args:
        url: URL with JSON object to scrape.

    Returns:
        A dictionary with the JSON object from the URL.

    Raises:
        JSONDecodeError: If the URL does not contain a JSON object.
        ConnectionError: If the URL is not reachable.
    """
    return get(url).json()
