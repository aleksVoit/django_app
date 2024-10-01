"""
This is test module
"""


def test_function(a: str) -> None:
    """
    Does nothing return either

    Args:
        a: dummy string

    Returns:
        Literally nothing

    Raises:
        ValueError: something meaningful in a

    """
    if a == 'word':
        raise ValueError("It's something interesting")
