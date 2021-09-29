from dagster import solid
import re

ALPHA_NUMERIC_PATTERN = r'[^a-zA-Z0-9_]'


@solid
def remove_non_alphanumeric(_context, string):
    cleaned = re.sub(ALPHA_NUMERIC_PATTERN, "", string)
    _context.log.info(f"Got cleaned string: {cleaned}")

    return cleaned