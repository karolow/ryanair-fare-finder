from datetime import datetime, timedelta
from statistics import median

from yaspin import Spinner


example_connections = (("DUB", "STN"), ("KTW", "STN"), ("DUB", "AMS"), ("TLL", "BVA"))
spinner = Spinner(
    ["✈_____", "_✈____", "__✈___", "___✈__", "____✈_", "_____✈"], 200
)


def calculate_stats(data: dict) -> dict:
    """Calculates min, median and max fares for each date."""
    return {
        date: [min(values), median(values), max(values)]
        for date, values in data.items()
    }


def find_dates_to_query(dates: list, max_days: int, frequency=None) -> list:
    """Selects dates to be queried.

    It helps limit the number of Ryanair API queries, considering
    both data availability in time and the fact that an individual
    API call can return flights for up to 7 days.
    """
    dates = [datetime.strptime(date, "%Y-%m-%d").date() for date in dates]
    start_date = min(dates)
    end_date = min([start_date + timedelta(days=max_days), max(dates)])
    actual_max_days = (end_date - start_date).days
    return [
        (start_date + timedelta(days=x)).strftime("%Y-%m-%d")
        for x in range(0, actual_max_days)
    ][::frequency]


def parse_fligths_list(api_response: dict) -> dict:
    """Parses values from a JSON API response and removes
    empty values/dates with empty values.
    """
    parsed_data = {
        date["dateOut"]: [
            flight.get("regularFare")["fares"][0]["amount"]
            for flight in date["flights"]
            if flight.get("regularFare") is not None
        ]
        for date in api_response["trips"][0]["dates"]
    }
    non_empty_vals = {
        date: [val for val in values if val is not None]
        for date, values in parsed_data.items()
        if values
    }
    return non_empty_vals
