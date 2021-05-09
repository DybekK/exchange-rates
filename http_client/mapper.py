from exception.InvalidJsonSchemaException import InvalidJsonSchemaException


def mapper(result: dict) -> list[str]:
    print(result)
    if "rates" in result and isinstance(result["rates"], list):
        return list(map(lambda x: f"Stawka: {x['mid']}, Data: {x['effectiveDate']}", result["rates"]))
    else:
        raise InvalidJsonSchemaException()
