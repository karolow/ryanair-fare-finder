import time
from yaspin import yaspin

from fare_finder.utils import parse_fligths_list, find_dates_to_query, spinner
from fare_finder.api.query import query_ryanair_api


def get_flights(
    origin: str, destination: str, departure_date: str, flex_days_out: int
) -> dict:
    """Queries Ryanair API for flights and returns preprocessed content."""
    try:
        response = query_ryanair_api(
            "https://www.ryanair.com/api/booking/v4/en-gb/availability",
            params=(
                ("ADT", "1"),
                ("DateOut", departure_date),
                ("Destination", destination),
                ("Origin", origin),
                ("FlexDaysOut", flex_days_out),
                ("ToUs", "AGREED"),
            ),
        )
    except Exception as e:
        print(
            f"Some flights might not have been collected due to likely error: {e}"
        )
    else:
        return parse_fligths_list(response)


def get_flight_dates(origin: str, destination: str) -> dict:
    """Queries Ryanair API for available flight days"""
    return query_ryanair_api(
        f"https://www.ryanair.com/api/farfnd/3/oneWayFares/{origin}/{destination}/availabilities"
    )


def get_all_flights(
    origin: str, destination: str, max_days: int, flex_days_out: int
) -> dict:
    """Queries Ryanair API for flights and their fares.

    It returns all results compiled into one collection.
    """
    dates = get_flight_dates(origin, destination)
    dates_to_query = find_dates_to_query(dates, max_days, flex_days_out)

    all_flights = {}
    for date in dates_to_query:
        with yaspin(spinner, text="Querying Ryanair API for flight fares..."):
            flights = get_flights(origin, destination, date, flex_days_out)
            time.sleep(0.25)
            if flights:
                all_flights.update(flights)
    return all_flights


def get_airport_names() -> list:
    """Queries Ryanair API for available airport names."""

    response = query_ryanair_api(
        "https://www.ryanair.com/api/locate/v1/autocomplete/airports",
        params=(("phrase", ""), ("market", "en-gb")),
    )
    return [
        f'{airport["name"]}, {airport["country"]["name"]}, {airport["code"]}'
        for airport in response
    ]


def get_airport_connections(origin: str) -> list:
    """Queries Ryanair API for connections between selected airports."""

    response = query_ryanair_api(
        "https://www.ryanair.com/api/locate/v1/autocomplete/routes",
        params=(("departurePhrase", origin), ("market", "en-gb")),
    )
    return [
        f'{airport["arrivalAirport"]["name"]}, {airport["arrivalAirport"]["country"]["name"]}, {airport["arrivalAirport"]["code"]}'
        for airport in response
    ]
