import requests
from bs4 import BeautifulSoup

def check_stocks():
    #URL = "https://realpython.github.io/fake-jobs/"
    # URL = "https://www.facetofacegames.com/the-one-ring-451-borderless-bundle-the-lord-of-the-rings-tales-of-middle-earth/"
    URL = "https://www.facetofacegames.com/emrakul-the-world-anew-6-modern-horizons-3/"
    page = requests.get(URL)
    #print(page.text)
    
    soup = BeautifulSoup(page.content, "html.parser")


    # result = soup.find(id="data-product-stock")
    # print(result)

    card_name = soup.find_all("h1", class_="productView-title")[0].contents[0]
    # print(card_name)

    result = soup.find_all("div", class_="form-field--stock")[0]
    result = result.find("span").contents[0]
    res_as_int = int(result)

    # print(res_as_int > 0)



if __name__ == "__main__":
    check_stocks()
