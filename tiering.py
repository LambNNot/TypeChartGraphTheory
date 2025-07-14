from typechart_data import PKMN_TYPES as types, PKMN_RESISTANCES as resistances, PKMN_WEAKNESSES as weaknesses, PKMN_IMMUNITIES as immunities
from helpers import display_tierlist

def validate_data(data: dict, source: list) -> bool:
    if not(isinstance(data, dict) and isinstance(source, list)):
        return False
    
    for value in source:
        if value in source and all([element in source for element in data[value]]):
            continue
        else:
            return False
    return True

def get_basic_tierlist(resistances: dict, weaknesses: dict, immunities: dict):
    
    score_result = {}

    for r in resistances.keys():
        for t in resistances.get(r, []):
            score_result.update({
                r : score_result.get(r, 0) + 1,
                t : score_result.get(t, 0) - 1
            })

    return score_result

    
if __name__ == "__main__":
    print("" or "Hello")
    print(len(set(types)) == 18)
    print(validate_data(resistances, types))
    print(validate_data(weaknesses, types))
    print(validate_data(immunities, types))
    basic_tierlist = get_basic_tierlist(resistances, weaknesses, immunities)
    display_tierlist(basic_tierlist)

