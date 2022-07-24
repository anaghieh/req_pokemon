from single_poki_model import SinglePokiModel
import requests

class SinglePoki():

    def __init__(self, s_poki):
        self.url = "https://pokeapi.co/api/v2/pokemon/"+s_poki
        self.request = requests.get(self.url)
        self.resp_json = self.request.json()

    def response_data(self):
        return SinglePokiModel(self.resp_json)
