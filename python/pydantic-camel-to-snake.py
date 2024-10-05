import re
camel_to_snake = re.compile(
    r"""
        (?<=[a-z])      # preceded by lowercase
        (?=[A-Z])       # followed by uppercase
    """,
    re.X,
)
def to_snake(string: str) -> str:
    """Convert camelCase string to snake_case."""
    return camel_to_snake.sub('_', string).lower()

def to_camel(string: str) -> str:
    """Convert snake_case string to camelCase."""
    return ''.join(word.capitalize() for word in string.split('_'))


class ClassName(BaseModel):
  model_config = ConfigDict(alias_generator=to_snake)


# References:

# https://docs.pydantic.dev/2.0/usage/model_config/ (Pydantic/model specific)
# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case (regex)
# 
