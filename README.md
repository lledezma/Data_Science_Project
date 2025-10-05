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

2. Install dependencies

The repository now includes a `requirements.txt` with conservative, Python 3.7+ compatible pins. Install them with:

```bash
pip install -r requirements.txt
```

If you prefer to install the latest versions without pins, you can install the common packages directly:

```bash
pip install requests beautifulsoup4 lxml pandas jupyter matplotlib selenium
```

Notes:
- `requirements.txt` contains pinned versions to improve reproducibility. If you want looser constraints, replace exact pins with `>=` or remove exact versions.
- If you use Selenium, see the webdriver note below for installing a matching driver.

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
