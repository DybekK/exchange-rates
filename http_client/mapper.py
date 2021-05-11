from exception.InvalidJsonSchemaException import InvalidJsonSchemaException


def mapper(result: dict) -> list[str]:
    """
    Maps dictionary to array of strings.

    Args:
         result (dict): Dictionary to map.

    Raises:
        InvalidJsonSchemaException

    Returns:
         Array of strings.
    """
    try:
        return list(map(lambda x: f"Stawka: {x['mid']}, Data: {x['effectiveDate']}", result["rates"]))
    except KeyError:
        raise InvalidJsonSchemaException()
