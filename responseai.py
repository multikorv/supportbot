import json
import re

class ResponseAiDupe():

    def load(self):
        self.read_responses_config()


    def read_responses_config(self):
        with open('responses.json', 'r') as infile:
            self.data = json.load(infile)


    def get_response(self, text):
        response = None
        found_response = False

        for maybe_response in self.data['responses']:
            is_regexp = maybe_response['is_regexp']
            value = maybe_response['value']
            if (is_regexp and re.match(value, text)):
                found_response = True
            elif value == text:
                found_response = True
            if found_response:
                response = maybe_response['response']
                break

        if not found_response:
            raise Exception("No response found in responses.json")
        else:
             return response
