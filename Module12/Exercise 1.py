
import requests
import json

class Joke:
    def __init__(self,url):
        self.url = url
        self.joke_data = None

    def get_jokes(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            #return json.dumps(data,indent=4)
            self.joke_data = data['value']
            return self.joke_data
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    def format_joke(self):
        width = len(self.joke_data)
        title_line = "*" * width
        formated_joke = f"{title_line}\nThis is a random joke:\n{title_line}\n{self.joke_data: ^20}"
        return formated_joke

api_address = 'https://api.chucknorris.io/jokes/random'
joke_output = Joke(api_address)
joke_output.get_jokes()
print(joke_output.format_joke())