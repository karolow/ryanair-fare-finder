# ryanair fare finder

Don't get ripped off by Ryan! Query Ryanair's API to reveal long-term flight prices between your desired locations.

### Installation

```shell
git clone https://github.com/karolow/ryanair-fare-finder.git
cd ryanair-fare-finder

pip install . -r requirements.txt
```

### Features & usage

* use `fare-finder` command to run the cli app 
* select the origin location from the list (use "/" to search)
* select a destination from available choices
* the resulting chart will pop up in your browser

### Optional arguments

* pass a valid path to `--html_path` argument to save a Plotly chart to a local file
* by using `--days` you can change the time span of your analysis (between 7 and 120 days)
* don't care about picking locations? – just hit `fare-finder --explore` to randomly select one of the available flights 

### Disclaimer

Please note that the terminal based interactive menu to pick airports may not work properly on Windows (it's not supported by the relevant simple-term-menu package). In case you'd like to run the app on Widnows anyway, please, use the --explore argument to bypass the origin/destination selection.

The ryanair-fare-finder package has been tested on Python 3.9–3.10, and Ubuntu 22.04 / macOS.

### Example queries:

```shell
fare-finder
fare-finder --explore
fare-finder --days 120
fare-finder --days 14 --explore --html_path existing_dir/chart_name.html
```

The last command will randomly pick a connection pair and generate a chart with fares covering the nearest 14 days. It will also save an html file to the requested path.

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


