from dagster import solid


@solid
def mock_spongebob(_context, string):

    def _change_case(index, letter):
        if index % 2 == 0:
            return letter.lower()

        return letter.upper()

    mocked = "".join([_change_case(index, character) for index, character in enumerate(string)])
    _context.log.info(f"Spongebob Mocked word: {mocked}")
    
    return mocked
