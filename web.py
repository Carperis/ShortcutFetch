# https://flask-json.readthedocs.io/en/latest/

from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from fetch import urlFetch

app = Flask(__name__)
FlaskJSON(app)


@app.route('/balance/<cookie>', methods=['GET', 'POST'])
def getBalance(cookie):
    url = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1675459615?ModuleName=current_balance_meal_and_pt.pl'
    # cookie = "f5_cspm=1234; f5avraaaaaaaaaaaaaaaa_session_=AMKFJCMAABAGNNLAAGEDCMOJHCFNCHBJGFGIOPGFLFJNBNPFPJBGGPNIOGFELDJEIJEDEEFEGMDHPLLMGMJAANFHDLGEINJHLJAJIGOEMIBNFADGPMIGMFOLLEAGIKDC; BIGipServerist-uiscgi-content-prod-443-pool=2315708170.47873.0000; uiscgi_prod=6969c54808a90dff5e353c9e37054afe:prod; BIGipServerist-uiscgi-app-prod-443-pool=1288029568.47873.0000"
    cookie = cookie.replace("[space]", " ").replace("[dot]", ".").replace(
        "[slash]", "/").replace("[backslash]", "\\").replace("[question]", "?")
    mylist = urlFetch(url, cookie)
    return json_response(plan=mylist[2], meal=mylist[3], g_meal=mylist[4], din_points=mylist[5], con_points=mylist[6])


@app.route('/input/<input>', methods=['GET', 'POST'])
def testInput(input):
    # print(input)
    input = input.replace("[space]", " ").replace("[dot]", ".").replace(
        "[slash]", "/").replace("[backslash]", "\\").replace("[question]", "?")
    # print(input)
    return json_response(input=input)


if __name__ == '__main__':
    app.run(debug=True, port="1234")
