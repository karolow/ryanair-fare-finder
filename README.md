# ryanair fare finder

Don't get ripped off by Ryan! Query Ryanair's API to reveal flight prices between your desired locations.

### Installation

```shell
git clone https://github.com/karolow/ryanair-fare-finder.git
cd ryanair-fare-finder

pip install . -r requirements.txt
```

### Features & usage

* use `fare-finder` command to run the command line app 
* you can pass additional like dates or html chart export (see below or use `fare-finder --help`)
* select the origin location from the list (use "/" to search)
* select destination from available choices
* check out the result in your browser or open the exported html file with a Plotly chart

### Disclaimer

Please note that the terminal based interactive menu to pick airports may not work properly on Windows OS (it's not supported by the relevant simple-term-menu package). In case you'd like to run the app on Widnows anyway, please, use the --explore argument to bypass the origin/destination selection.

### Example queries:

```shell
fare-finder --days 14 --explore --html_path existing_dir/chart_name.html
```

This command will randomly pick a connection pair and generate a chart with fares covering the nearest 14 days. It will also save an html file to the requested path.

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


