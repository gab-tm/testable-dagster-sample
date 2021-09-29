from dagster import solid

alpha_numeric_map = {
    "I": 1,
    "Z": 2,
    "E": 3,
    "A": 4,
    "S": 5,
    "T": 7,
    "B": 8,
    "Q": 9,
    "O": 0
}

@solid
def leet(_context, string):
    
    def _get_leet_counterpart(character):
        try:
            return str(alpha_numeric_map[character.upper()])
        except KeyError:
            return character

    leeted = "".join([_get_leet_counterpart(character) for character in string])
    _context.log.info(f"Leet word: {leeted}")
    return leeted