from slackclient import SlackClient


class SlackClientProxy():
    MEMBERS = "members"


    class Chat():
        POSTMESSAGE = "chat.postMessage"


    class Users():
        LIST = "users.list"


    def __init__(self, stringtoken):
        self.token = stringtoken
        self.slack = SlackClient(self.token)


    def api_call(self, cmd, channel=None, text=None, as_user=True):
        return self.slack.api_call(cmd, channel=channel, text=text, as_user=as_user)


    def rtm_connect(self):
        return self.slack.rtm_connect()


    def rtm_read(self):
        return self.slack.rtm_read()

class ApiCallProxy():
    OK = 'ok'

    def __init__(self):
        pass


    def get(self, key):
        if (key == self.OK):
            return True
        if (key == SlackClientProxy.MEMBERS):
            return [{'name':'supportbot'},{'id':1}]
