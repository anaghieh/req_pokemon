from single_poki import SinglePoki

charmander = SinglePoki("charmander")
pikachu = SinglePoki("pikachu")

print('Charmander stats:', f'base_exp: {charmander.response_data().base_exp}, hp: {charmander.response_data().stats_hp}, attack: {charmander.response_data().stats_attack}, defence: {charmander.response_data().stats_defence} ')
print('Pikachu stats:', f'  base_exp: {pikachu.response_data().base_exp}, hp: {pikachu.response_data().stats_hp}, attack: {pikachu.response_data().stats_attack}, defence: {pikachu.response_data().stats_defence}')

print('Charmander abilities:', f' {charmander.response_data().abilities1}, {charmander.response_data().abilities2}')
print('Pickachu abilities:', f'{pikachu.response_data().abilities1}, {pikachu.response_data().abilities2}')
