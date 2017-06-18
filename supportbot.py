import os
import time
from slackproxy import SlackClientProxy, ApiCallProxy
from responseai import ResponseAiDupe

import json

class SupportBot():
    BOT_NAME = 'supportbot'
    SLACK_BOT_TOKEN = 'SLACK_BOT_TOKEN'


    def __init__(self):
        self.slack_client_proxy = SlackClientProxy(self.SLACK_BOT_TOKEN)


    def handle_command(self, command, channel):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.

            command (str): command
            channel (str): channel
        """
        response = "Command: {0}, channel, {1}".format(command, channel)
        self.try_support_response(channel=channel, text=response)


    def try_support_response(self, channel, text):
        try:
            response = self.ai.get_response(text)
            self.post_message(channel=channel, text=response)
        except Exception as e:
            print 'Could not find a response: {0}'.format(e)



    def post_message(self, channel, text):
        self.slack_client_proxy.api_call(SlackClientProxy.Chat.POSTMESSAGE, channel=channel,
                              text=text, as_user=True)


    def parse_slack_output(self, slack_rtm_output):
        """
            The Slack Real Time Messaging API is an events firehose.
            this parsing function returns None unless a message is
            directed at the Bot, based on its ID.
        """
        # TODO remove when ready
        return "Some command", "a_channel"
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and self.at_bot in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(self.at_bot)[1].strip().lower(), \
                           output['channel']
        return None, None


    def init(self):
        api_call = self.slack_client_proxy.api_call(SlackClientProxy.Users.LIST)
        if api_call.get(ApiCallProxy.OK):
            # retrieve all users so we can find our bot
            users = api_call.get(SlackProxy.MEMBERS)
            for user in users:
                if 'name' in user and user.get('name') == self.BOT_NAME:
                    self.botid = user.get('id')
                    self.at_bot = "<@" + self.botid + ">"
                    print("Bot ID for '" + user['name'] + "' is " + self.botid)
        else:
            print("could not find bot user with the name " + self.BOT_NAME)


    def start(self):
        READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
        if self.slack_client_proxy.rtm_connect():
            print("StarterBot connected and running!")
            while True:
                command, channel = self.parse_slack_output(self.slack_client_proxy.rtm_read())
                if command and channel:
                    self.handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")


def main():
    supportbot = SupportBot()

    supportbot.ai = ResponseAiDupe()
    supportbot.ai.load()

    supportbot.init()
    supportbot.start()


if __name__ == "__main__":
    main()
