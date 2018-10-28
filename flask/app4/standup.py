import datetime
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for, make_response
import pdb
import json

app = Flask(__name__)





@app.route('/')
def get_status_yesterday():
    render_template('index.html')
    menu_item = 0
    lines = []
    while True:
        line
        if line:
            lines.append(line)
        else:
            break
    yesterday = '\n'.join(lines)
    return (yesterday)



# def get_status_today():
#     menu_item = 0
#     lines = []
#     count = 1
#     while True:
#         line = input("*what did yo do today:\n")
#         if line:
#             lines.append(str(count) + "." + line)
#             count += 1
#         else:
#             break
#     today = '\n'.join(lines)
#
#     return today

#
# def any_blocker():
#     menu_item = 0
#     lines = []
#     while True:
#         line = input("*Any blcoker: \n")
#         if line:
#             lines.append(line)
#         else:
#             break
#     any_blocker = '\n'.join(lines)
#     return any_blocker


# def my_status():
#     yesterday = Stand_up.get_status_yesterday()
#     today = Stand_up.get_status_today()
#     blocker = Stand_up.any_blocker()
#     today_date = datetime.date.today()
#     print("-------------------------------------")
#     print("*Status Update*:{} ".format(today_date))
#     print("*Worked on yesterday:*")
#     print(yesterday)
#     print("*Working on today:*")
#     print(today)
#     print("*Any blockers:* --", blocker)
#     print("-------------------------------------")

#
# def main():
#     call = Stand_up()
#     call.my_status()


# if __name__ == '__main__': main()
app.run(debug = True)