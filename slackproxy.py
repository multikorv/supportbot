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
        if cmd == self.Chat.POSTMESSAGE:
            print "POSTMESSAGE {0}".format(text)
        return ApiCallProxy()


    def rtm_connect(self):
        return True


    def rtm_read(self):
        return [
            {'channel': 'a_channel', 'text': '<@123> some text help i need something something'},
            {'channel': 'a_channel', 'text': '<@123> some text halp i need something something'},
            {'channel': 'a_channel', 'text': '<@123> some text halp something'},
            {'channel': 'a_channel', 'text': '<@123> nothing here'}
        ]


class ApiCallProxy():
    OK = 'ok'

    def __init__(self):
        pass


    def get(self, key):
        if (key == self.OK):
            return True
        if (key == SlackClientProxy.MEMBERS):
            return [{'name':'supportbot'},{'id':1}]
