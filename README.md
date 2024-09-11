# in_stock_inator

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

A web-scraping framework to help you check if a specific product is in stock.

# A Note about Ethical Webscraping
As with any web scraping, please make sure that you are following ethical and legal guidelines. If unsure 
what these are, you can read blog posts like https://blog.apify.com/is-web-scraping-legal/ which provide
an introduction to the topic. Please always read the terms of services of any website you wish to scrape
to ensure they do not have policies against web scraping. 

# Installation
Create a python environment: 
``` bash
# UNIX
python3 -m venv venv
```

Install the dependencies: 
```bash
# UNIX
pip install -r requirements.txt
```

Ensure you have a browser and webdriver well installed. The code currently supports Geckodriver with 
Firefox. Install geckodriver: https://github.com/mozilla/geckodriver/releases

Note that on Ubuntu 22.04LTS, I had to install Firefox by following the official Mozilla `.deb` installation
guidelines. Otherwise, I would get [an issue with the profiles](https://github.com/jubiiz/in_stock_inator/issues/9)

Install [Firefox](https://support.mozilla.org/en-US/kb/install-firefox-linux?utm_source=www.mozilla.org&utm_medium=referral&utm_campaign=firefox-download-thanks&_gl=1*ykxs4r*_ga*OTk5MTA1MTcyLjE3MjQ4NDc5MjQ.*_ga_MQ7767QQQW*MTcyNTg0MTA2NC4xLjEuMTcyNTg0MTA3MC4wLjAuMA..#w_install-firefox-deb-package-for-debian-based-distributions)


# Usage

### Avoid Scraping too Often
Do not run your scraping function too often, as this would put an unnecessary strain on the target websites. 

### Creating an Availability Function
These are functions located in `./availability_functions/`. Given a webdriver and a URL, they scrape the target webpage and return wether a product is in stock.

A sample function is already present in the directory.

### Creating an Alerting Function
These are functions located in `./alerting_functions/`. Given the response from the selected availability function, they alert the user 
of the result, or choose not to, for example if the product is not in
stock. 

A sample function is already present in the directory.

### Creating a Shopping List
This is a configuration file located in `./shopping_lists/`. It specifies
a list of target products to check for availability. For each product, 
a corresponding [availability function](#creating-an-availability-function) will check if the product is in stock, pass that result to an [alerting function](#creating-an-alerting-function), which will decide how to alert the user. 

### Running the Checks
The items can be checked for availability by running the main file: 
``` bash
python3 src/stock_checker.py
```

It will go through every

