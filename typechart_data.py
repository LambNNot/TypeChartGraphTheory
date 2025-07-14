PKMN_TYPES =[
    "grass",
    "water",
    "fire",
    "electric",
    "ground",
    "rock",
    "bug",
    "normal",
    "fighting",
    "ghost",
    "psychic",
    "dark",
    "steel",
    "dragon",
    "ice",
    "fairy",
    "flying",
    "poison"
]


PKMN_RESISTANCES = {
    "grass": ["ground", "water", "grass", "electric"],
    "water": ["steel", "fire", "water", "ice"],
    "fire": ["bug", "steel", "fire", "grass"],
    "electric": ["flying", "electric", "steel"],
    "ground": ["poison", "rock"],
    "rock": ["normal", "flying", "poison", "fire"],
    "bug": ["fighting", "ground", "grass"],
    "normal": [],
    "fighting": ["rock", "bug", "dark"],
    "ghost": ["poison", "bug"],
    "psychic": ["fighting", "psychic"],
    "dark": ["ghost", "dark"],
    "steel": ["normal", "flying", "rock", "bug", "steel", "grass", "psychic", "ice", "dragon", "fairy"],
    "dragon": ["water", "fire", "grass", "electric"],
    "ice": ["ice"],
    "fairy": ["fighting", "bug", "dark"],
    "flying": ["fighting", "bug", "grass"],
    "poison": ["fighting", "poison", "bug", "grass", "fairy"]

}

PKMN_WEAKNESSES = {
    "grass": ["flying", "poison", "bug", "fire", "ice"],
    "water": ["grass", "electric"],
    "fire": ["ground", "rock", "water"],
    "electric": ["ground"],
    "ground": ["water", "grass", "ice"],
    "rock": ["fighting", "ground", "steel", "water", "grass"],
    "bug": ["flying", "rock", "fire"],
    "normal": ["fighting"],
    "fighting": ["flying", "psychic", "fairy"],
    "ghost": ["ghost", "dark"],
    "psychic": ["bug", "ghost", "dark"],
    "dark": ["fighting", "bug", "fairy"],
    "steel": ["fighting", "ground", "fire"],
    "dragon": ["ice", "dragon", "fairy"],
    "ice": ["fighting", "rock", "steel", "fire"],
    "fairy": ["poison", "steel"],
    "flying": ["rock", "electric", "ice"],
    "poison": ["ground", "psychic"]
}

PKMN_IMMUNITIES = {
    "grass": [],
    "water": [],
    "fire": [],
    "electric": [],
    "ground": ["electric"],
    "rock": [],
    "bug": [],
    "normal": ["ghost"],
    "fighting": [],
    "psychic": [],
    "dark": ["psychic"],
    "ghost": ["normal", "ghost"],
    "steel": ["poison"],
    "dragon": [],
    "ice": [],
    "fairy": ["dragon"],
    "flying": ["ground"],
    "poison": []
}