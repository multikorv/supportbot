from slackclient import SlackClient


class SlackClientProxy():
    MEMBERS = "members"


    class Chat():
        POSTMESSAGE = "chat.postMessage"


    class Users():
        LIST = "users.list"


    def __init__(self, stringtoken):
        self.token = stringtoken


    def handle_command(self):
        pass


    def api_call(self, cmd, channel=None, text=None, as_user=True):
        pass


    def rtm_connect(self):
        pass


    def rtm_read(self):
        pass


    class ApiCallProxy():


        def __init__(self):
            pass


        def get(self):
            pass
