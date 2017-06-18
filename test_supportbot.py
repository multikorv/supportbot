import unittest
from supportbot import SupportBot
from mockito import when, mock, unstub, verify, ANY

class TestSupportBot(unittest.TestCase):


    def test_halptextmsg_correctresponse(self):
        KNOWN_RESPONSE = "You'll get halp!"
        KNOWN_CHANNEL = "a_channel"
        # mock entire class

        bot = SupportBot()

        when(bot).post_message(channel=ANY(str), text=ANY(str))

        bot.try_support_response(KNOWN_CHANNEL, "halp")

        verify(bot, times=1).post_message(channel=KNOWN_CHANNEL, text=KNOWN_RESPONSE)

        # clean up
        unstub()


    def test_simpletextmsg_correctresponse(self):
        KNOWN_RESPONSE = "Sorry?"
        KNOWN_CHANNEL = "a_channel"
        # mock entire class

        bot = SupportBot()

        when(bot).post_message(channel=ANY(str), text=ANY(str))

        bot.try_support_response(KNOWN_CHANNEL, "hej")

        verify(bot, times=1).post_message(channel=KNOWN_CHANNEL, text=KNOWN_RESPONSE)

        # clean up
        unstub()


if __name__ == '__main__':
    unittest.main()
