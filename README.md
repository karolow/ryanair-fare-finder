# Ryanair fare finder

Don't get rip off by Ryan! Query Ryanair's API to reveal flight prices between your desired locations.

Installation instructions to be found [below](https://github.com/karolow/ryanair-fare-finder#installation).

### Features & usage

* use `fare-finder` command to run the command line app 
* you can pass additional [arguments](https://github.com/karolow/ryanair-fare-finder#installation like dates or html chart export
* select the origin location from the list (use "/" to search)
* select destination from available choices
* check out the result in your browser or open the exported html file with a Plotly chart

### Example queries:

```shell
fare-finder --days 30 --explore --html_path existing_dir/chart_name.html
```

This command will randomly pick a connection pair and generate a chart with fares covering the nearest 30 days. It will also save an html file to the requested path.

![random_query](https://karolpiekar.ski/images/screens/ryanair-fare-finder/dub_stn_ryanair_fares_1.png)

### CLI documentation:

```shell
Usage: fare-finder [OPTIONS]

Options:
  --days INTEGER RANGE  Max number of days to query  [default: 31;7<=x<=120]
  --explore             Explore random connections  [default: False]
  --html_path TEXT      Path to export your chart to an html file  [default:
                        False]
  --help                Show this message and exit.
```

### Installation

```shell
git clone https://github.com/karolow/ryanair-fare-finder.git
cd ryanair-fare-finder

pip install . -r requirements.txt
```

