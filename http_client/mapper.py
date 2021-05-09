from exception.InvalidJsonSchemaException import InvalidJsonSchemaException


def mapper(result: dict) -> list[str]:
    try:
        return list(map(lambda x: f"Stawka: {x['mid']}, Data: {x['effectiveDate']}", result["rates"]))
    except KeyError:
        raise InvalidJsonSchemaException()
