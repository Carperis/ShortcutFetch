from bs4 import BeautifulSoup  # 获取数据
import urllib.request
import urllib.error


def fetchSeat(section, semesterNew):  # e.g. section="ENG ME 460 A1", semesterNew="2023-FALL"
    year = int(semesterNew.split("-")[0])
    sem = semesterNew.split("-")[1]
    if (sem == "FALL"):
        sem = "Fall"
        y = str(year + 1)
        num = "3"
    elif (sem == "SPRG"):
        sem = "Spring"
        y = str(year)
        num = "4"
    elif (sem == "SUMM_1"):
        sem = "Summer"
        y = str(year+1)
        num = "1"
    elif (sem == "SUMM_2"):
        sem = "Summer"
        y = str(year+1)
        num = "2"
    A = section.split(" ")[0]
    B = section.split(" ")[1]
    C = section.split(" ")[2]
    D = section.split(" ")[3]
    url = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1650761430?College=" + A + \
        "&Dept="+B+"&Course="+C+"&Section="+D+"&ModuleName=univschr.pl&KeySem="+y+num+"&ViewSem=" + \
        sem+"+" + \
            str(year)+"&SearchOptionCd=S&SearchOptionDesc=Class+Number&MainCampusInd="
    html = askURL(url)
    # print(url)
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    alltd = soup.find_all("td")  # 41,26
    result = 0
    try:
        td1 = alltd[26].find_all("font")[0].contents[0]
        try:
            td1 = int(td1.strip())
        except:
            td1 = "can't be int"
    except:
        td1 = "can't find"
    try:
        td2 = alltd[41].find_all("font")[0].contents[0]
        try:
            td2 = int(td2.strip())
        except:
            td2 = "can't be int"
    except:
        td2 = "can't find"
    if (td1 != "can't find" and td1 != "can't be int"):
        result = td1
    elif (td2 != "can't find" and td2 != "can't be int"):
        result = td2
    else:
        result = 0
    keyName = A + " " + B + " " + C + "-" + D
    data = [keyName, result]
    return data


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request, timeout=5)
        html = response.read().decode("utf-8")
    except Exception as e:
        print(e)
    return html


if __name__ == '__main__':
    section = "CAS RN 100 A1"
    # section = "ENG ME 460 A1"
    semesterNew = "2023-FALL"
    result = fetchSeat(section, semesterNew)
    print(result)
