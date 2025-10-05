# Data_Science_Project

A small collection of web-scraping scripts, data files, and Jupyter notebooks used to collect and explore hotel/listing data (Agoda, Trivago, TripAdvisor, Hotels, Sweetwater, AP News briefs, etc.).

This repository contains Python scraper scripts, helper shells, example JSON/HTML outputs, and notebooks that document the data exploration and visualizations.

## Repository layout (selected)

- `AgodaJSON.py`, `AgodaShell.py` - helpers for Agoda scraping
- `HotelsJSON.py`, `HotelsShell.py` - helpers for Hotels scraping
- `TrivagoJSON.py`, `TrivagoShell.py` - Trivago scraping utilities
- `ScrapeWithRequests.py`, `ScrapeWithSelenium.py`, `ScrapeParseSendToJSON.py` - scraping driver scripts
- `APNewsBriefsToJSON.py`, `APNewsBriefsShell.py` - AP News briefs scraping
- `*.json`, `*.html` files in the repo root - example outputs captured during scraping (e.g. `2017-02-13.Trivago.json`)
- Notebooks: `CreatingADataProject.ipynb`, `Visualizations.ipynb`, `Sweetwater.ipynb` - analysis and visualization notebooks


## Quick start

1. (Optional) Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install common dependencies

```bash
pip install requests beautifulsoup4 lxml pandas jupyter matplotlib selenium
```

There is no `requirements.txt` in this repo; add one if you want reproducible installs.

3. Run a scraper (example)

```bash
python ScrapeWithRequests.py
```

4. Open the notebooks

```bash
jupyter notebook
```

Then open `CreatingADataProject.ipynb` or `Visualizations.ipynb` in the browser.


## Notes and caveats

- Python 3.7+ is recommended. Some scripts may use older idioms and selectors that depend on the site structure in 2017. The scraping selectors may need updates.
- Selenium scripts require a matching webdriver (chromedriver/geckodriver) available in PATH.
- The repo contains sample JSON/HTML output recorded in 2017; exercise caution if the site terms of service disallow scraping.


## License

This project is for educational purposes.
