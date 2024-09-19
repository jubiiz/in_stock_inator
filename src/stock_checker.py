import importlib
import json
import sys
from typing import Callable

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

SHOPPING_LIST_PATH = (
    "/home/jubiiz/documents/code/in_stock_inator/shopping_lists/my_shopping_list.json"
)


def main():
    groups = get_shopping_list_groups(SHOPPING_LIST_PATH)

    for group in groups:
        availability_function_path_to_file = group["availabilityFunction"]["pathToFile"]
        availability_function_module_name = group["availabilityFunction"]["moduleName"]
        availability_function_name = group["availabilityFunction"]["functionName"]
        availability_function = import_custom_function(
            availability_function_path_to_file,
            availability_function_module_name,
            availability_function_name,
        )

        alerting_function_path_to_file = group["alertingFunction"]["pathToFile"]
        alerting_function_module_name = group["alertingFunction"]["moduleName"]
        alerting_function_name = group["alertingFunction"]["functionName"]
        alerting_function = import_custom_function(
            alerting_function_path_to_file,
            alerting_function_module_name ,
            alerting_function_name ,
        )

        for item in group["items"]:
            url = item["url"]
            driver = get_web_driver()
            result = availability_function(driver, url)
            alerting_function(result)


def get_web_driver() -> WebDriver:
    gecko_driver_path = "/usr/local/bin/geckodriver"  # Adjust if necessary
    service = Service(gecko_driver_path)
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(service=service, options=options)


def import_custom_function(
    path_to_file: str, module_name: str, function_name: str
) -> Callable:
    spec = importlib.util.spec_from_file_location(module_name, path_to_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return getattr(module, function_name)


def get_shopping_list_groups(path_to_shopping_list: str):
    with open(path_to_shopping_list, "r") as f:
        groups = json.loads(f.read())["groups"]
    return groups


if __name__ == "__main__":
    main()
