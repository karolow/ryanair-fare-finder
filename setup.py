from setuptools import setup, find_packages

setup(
    name="ryanair-fare-finder",
    version="0.1.0",
    description="Query Ryanair's API to reveal flight prices between your desired locations.",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["fare-finder=fare_finder.cli:cli"],
    },
)
