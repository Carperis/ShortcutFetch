# https://flask-json.readthedocs.io/en/latest/

from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from fetchBalance import fetchBalance
from fetchSeat import fetchSeat

app = Flask(__name__)
FlaskJSON(app)


@app.route('/balance/<cookie>', methods=['GET', 'POST'])
def getBalance(cookie):
    url = 'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1675459615?ModuleName=current_balance_meal_and_pt.pl'
    # cookie = "f5_cspm=1234; f5avraaaaaaaaaaaaaaaa_session_=AMKFJCMAABAGNNLAAGEDCMOJHCFNCHBJGFGIOPGFLFJNBNPFPJBGGPNIOGFELDJEIJEDEEFEGMDHPLLMGMJAANFHDLGEINJHLJAJIGOEMIBNFADGPMIGMFOLLEAGIKDC; BIGipServerist-uiscgi-content-prod-443-pool=2315708170.47873.0000; uiscgi_prod=6969c54808a90dff5e353c9e37054afe:prod; BIGipServerist-uiscgi-app-prod-443-pool=1288029568.47873.0000"
    cookie = cookie.replace("[space]", " ").replace("[dot]", ".").replace(
        "[slash]", "/").replace("[backslash]", "\\").replace("[question]", "?")
    try:
        mylist = fetchBalance(url, cookie)
        msg = ""
        plan = mylist[2]
        meal = mylist[3]
        g_meal = mylist[4]
        din_points = mylist[5]
        con_points = mylist[6]
    except:
        msg = "Error!"
        return json_response(msg=msg)
    return json_response(msg=msg, plan=plan, meal=meal, g_meal=g_meal, din_points=din_points, con_points=con_points)


@app.route('/seat/<course>/<semester>', methods=['GET', 'POST'])
def getSeat(course, semester):
    course = course.replace("[space]", " ").replace("[dot]", ".").replace(
        "[slash]", "/").replace("[backslash]", "\\").replace("[question]", "?")
    try:
        result = fetchSeat(course, semester)
        msg = ""
    except:
        msg = "Error!"
        return json_response(msg=msg)
    return json_response(msg=msg, seat=result[1])


@app.route('/input/<input>', methods=['GET', 'POST'])
def getInput(input):
    input = input.replace("[space]", " ").replace("[dot]", ".").replace(
        "[slash]", "/").replace("[backslash]", "\\").replace("[question]", "?")
    return json_response(input=input)


if __name__ == '__main__':
    app.run(debug=True, port="1234")
