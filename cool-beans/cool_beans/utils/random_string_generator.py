from essential_generators import DocumentGenerator


class RandomStringGenerator:
    def get_random_string(self):
        document_generator = DocumentGenerator()
        random_string = document_generator.word()

        return random_string


class MockRandomStringGenerator:
    def get_random_string(self):
        return "a_very_long_string_with_no_spaces_and_special_characters_considered_as_one_word"
