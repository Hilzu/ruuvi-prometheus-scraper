# Ruuvi Prometheus scraper

Collects weather data from [Ruuvi tags][ruuvi-tag] running the [official
firmware][fw] for consumption by [Prometheus][prometheus].

The python file `main.py` is hardcoded for my tags but can easily be modified
for your own needs.

You can also take a look at the files under `deploy/` that I use to run this
scraper on a Raspberry PI 3. They assume that the scraper is run with an user
called `ruuvi`. You also need to configure Prometheus to scrape data from
the app from the address `http://localhost:8000/metrics`.

## Install

```bash
git clone git@github.com:Hilzu/ruuvi-prometheus-scraper.git
cd ruuvi-prometheus-scraper
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

[ruuvi-tag]: https://tag.ruuvi.com/
[fw]: https://lab.ruuvi.com/ruuvitag-fw/
[prometheus]: https://prometheus.io/
