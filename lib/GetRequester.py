import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(URL)
        return response.content
    

    def load_json(self):
        list_of_names = []
        names_data = json.loads(self.get_response_body())
        for person in names_data:
            list_of_names.append(person)

        return list_of_names