# https://flask-json.readthedocs.io/en/latest/

from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from fetch import urlFetch

app = Flask(__name__)
FlaskJSON(app)


@app.route('/<url>/<cookie>', methods=['GET, POST'])
def getInfo(url, cookie):
    # url = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1675459615?ModuleName=current_balance_meal_and_pt.pl'
    # cookie = "f5_cspm=1234; f5avraaaaaaaaaaaaaaaa_session_=HNJFMCMCABAGNNLAIAJKCMOJHCFNCHBJGFGIOPGFLFJNBNPFPJBGGPNIOGFELDJEIJEDEEFEHADHMHLMGMJAANFHHIGEMOJHLJAJIGOEMIBNFAPHPMIGMFOLLEAGIKNM; uiscgi_prod=e8510be2c65c31c1ed824b65ddbf0345:prod; BIGipServerist-uiscgi-app-prod-443-pool=1254475136.47873.0000; BIGipServerwww-prod-crc-443-pool=659366669.47873.0000"
    with open('log.txt', 'w') as f:
        f.write(url + "/n" + cookie)
    mylist = urlFetch(url, cookie)
    return json_response(plan=mylist[2], meal=mylist[3], g_meal=mylist[4], din_points=mylist[5], con_points=mylist[6])


if __name__ == '__main__':
    app.run(debug=True, port="1234")
