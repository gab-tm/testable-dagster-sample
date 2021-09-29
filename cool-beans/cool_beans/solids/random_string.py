from dagster import solid, SolidExecutionContext


@solid(required_resource_keys={"random_string_generator"})
def spew_random_string(_context: SolidExecutionContext):
    random_string_generator = _context.resources.random_string_generator
    random_string = random_string_generator.get_random_string()

    _context.log.info(f"Generated random string: {random_string}")
    return random_string
