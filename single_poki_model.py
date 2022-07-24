class SinglePokiModel:

    def __init__(self, single_poki):
        self.abilities = single_poki['abilities']
        self.abilities1 = self.abilities[0]['ability']['name']
        self.abilities2 = self.abilities[1]['ability']['name']
        self.base_exp = single_poki['base_experience']
        self.stats = single_poki['stats']
        self.stats_hp = self.stats[0]['base_stat']
        self.stats_attack = self.stats[1]['base_stat']
        self.stats_defence = self.stats[2]['base_stat']


