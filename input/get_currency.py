from iso4217 import Currency


def get_currency() -> str:
    """Gets value from user about currency"""
    while True:
        try:
            currency = input("Enter currency:").lower()
            return Currency[currency].code
        except KeyError:
            print("This is the incorrect currency format")
            continue
