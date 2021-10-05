from essential_generators import DocumentGenerator


class RandomStringGenerator:
    def get_random_string(self):
        document_generator = DocumentGenerator()
        random_string = document_generator.sentence()

        return random_string


class MockRandomStringGenerator:
    def get_random_string(self):
        return "A very long string with no spaces and special characters considered as one word."
