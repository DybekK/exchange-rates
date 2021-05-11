from iso4217 import Currency


def get_currency(test_loop_count=None) -> str:
    """
    Gets value from user about currency.

    Args:
         test_loop_count (int): Used for testing purposes to count calls of this method.

    Returns:
         Accurate currency code as a string.
    """
    loop_count = 0
    while True:
        try:
            currency = input("Enter currency:").lower()
            return Currency[currency].code
        except KeyError:
            loop_count += 1
            if test_loop_count == loop_count:
                break
            print("This is the incorrect currency format")
            continue
