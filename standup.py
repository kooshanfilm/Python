import datetime


class Stand_up:


    def get_status_yesterday(self):

        menu_item = 0
        lines = []
        while True:
            line = input("*what did yo do yesterday:\n")
            if line:
                lines.append(line)
            else:
                break
        yesterday = '\n'.join(lines)
        return(yesterday)

    def get_status_today(self):

        menu_item = 0
        lines = []
        while True:
            line = input("*what did yo do today:\n")
            if line:
                lines.append(line)
            else:
                break
        today = '\n'.join(lines)
        return today

    def any_blocker(self):

        menu_item = 0
        lines = []
        while True:
            line = input("*Any blcoker: \n")
            if line:
                lines.append(line)
            else:
                break
        any_blocker = '\n'.join(lines)
        return any_blocker


    def my_status(self):
        yesterday =Stand_up.get_status_yesterday(self)
        today = Stand_up.get_status_today(self)
        blocker = Stand_up.any_blocker(self)
        today_date = datetime.date.today()
        print("-------------------------------------")
        print("*Status Update*:{} ".format(today_date))
        print("*Worked on yesterday:*")
        print(yesterday)
        print("*Working on today:*")
        print(today)
        print("*Any blockers:* --",blocker)
        print("-------------------------------------")


    def post_into_slac(self):


        slack_token = os.environ["xoxp-313550114231-313550114855-436592439875-68f32c3d8a26d7c47ae255408661543d"]
        sc = SlackClient(slack_token)

        sc.api_call(
            "chat.postMessage",
            channel="C9TRBLB3K",
            text="Hello from Python! :tada:"
        )

def main():

    call = Stand_up()
    call.my_status()
    #call.post_into_slac()




if __name__ == '__main__':main()


