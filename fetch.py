import requests
from bs4 import BeautifulSoup


def urlFetch(url, cookie):
    # Define the URL of the website you want to fetch
    # url = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1675459615?ModuleName=current_balance_meal_and_pt.pl'

    # Define the cookie you want to use
    # cookie = "f5_cspm=1234; f5avraaaaaaaaaaaaaaaa_session_=HNJFMCMCABAGNNLAIAJKCMOJHCFNCHBJGFGIOPGFLFJNBNPFPJBGGPNIOGFELDJEIJEDEEFEHADHMHLMGMJAANFHHIGEMOJHLJAJIGOEMIBNFAPHPMIGMFOLLEAGIKNM; uiscgi_prod=e8510be2c65c31c1ed824b65ddbf0345:prod; BIGipServerist-uiscgi-app-prod-443-pool=1254475136.47873.0000; BIGipServerwww-prod-crc-443-pool=659366669.47873.0000"
    head = {"Cookie": cookie}

    # Send a GET request to the website, including the cookie
    response = requests.get(url, headers=head)

    # Use Beautiful Soup to parse the HTML content of the website
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <font> tags with size attribute value of +1 and containing a <b> tag
    fonts = soup.find_all('font', attrs={'size': '+1'}, recursive=True)

    result = []
    # Loop through the fonts and store their text values
    for font in fonts:
        bold = font.find('b')
        if bold:
            result.append(bold.text.strip())
    return result


if __name__ == '__main__':
    url = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1675459615?ModuleName=current_balance_meal_and_pt.pl'
    cookie = "f5_cspm=1234; f5avraaaaaaaaaaaaaaaa_session_=HNJFMCMCABAGNNLAIAJKCMOJHCFNCHBJGFGIOPGFLFJNBNPFPJBGGPNIOGFELDJEIJEDEEFEHADHMHLMGMJAANFHHIGEMOJHLJAJIGOEMIBNFAPHPMIGMFOLLEAGIKNM; uiscgi_prod=e8510be2c65c31c1ed824b65ddbf0345:prod; BIGipServerist-uiscgi-app-prod-443-pool=1254475136.47873.0000; BIGipServerwww-prod-crc-443-pool=659366669.47873.0000"
    mylist = urlFetch(url, cookie)
    print(mylist)
