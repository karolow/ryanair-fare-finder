import click
import random

from simple_term_menu import TerminalMenu


from fare_finder.finder.fares import (
    get_airport_connections,
    get_airport_names,
    get_all_flights,
)

from fare_finder.dataviz.chart import generate_chart
from fare_finder.utils import calculate_stats, example_connections


@click.command()
@click.option(
    "--days",
    default=31,
    show_default=True,
    type=click.IntRange(min=7, max=120),
    help="Max number of days to query",
)
@click.option(
    "--explore",
    is_flag=True,
    default=False,
    show_default=True,
    help="Explore random connections",
)
@click.option(
    "--html_path",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to export your chart to an html file",
)
def check_flights(days, explore, html_path):

    if not explore:
        ### pick origin airport ###
        options = get_airport_names()
        terminal_menu = TerminalMenu(
            options, title="Pick the origin location (use '/' to search)"
        )
        menu_entry_index = terminal_menu.show()
        origin, _, origin_code = options[menu_entry_index].split(",")
        origin_code = origin_code.strip()
        print(f"You are traveling from: {origin}, {origin_code}.")

        #### pick destination airport ###
        options = get_airport_connections(origin_code.strip())
        terminal_menu = TerminalMenu(
            options, title="Pick your destination (use '/' to search)"
        )
        menu_entry_index = terminal_menu.show()
        destination, _, dest_code = options[menu_entry_index].split(",")
        dest_code = dest_code.strip()
        print(f"You are traveling to: {destination}, {dest_code}")

    else:
        origin_code, dest_code = random.choice(example_connections)
        print(f"Exploring Ryanair fares between {origin_code} and {dest_code}")

    flight_data = get_all_flights(
        origin_code,
        dest_code,
        max_days=days,
        flex_days_out=6,  # Ryanair API can return flights for up to 6 following days
    )
    data = calculate_stats(flight_data)
    generate_chart(data, origin_code, dest_code, html_path)


def cli():
    check_flights()
