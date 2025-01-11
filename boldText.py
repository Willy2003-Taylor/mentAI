# Description: Contains a function to format text in bold for console output.
def boldText(text: str) -> str:
    """
    Returns the given text formatted in bold for console output.
    Uses ANSI escape codes for bold formatting.

    :param text: The text to be bolded.
    :return: The bolded text as a string.
    """
    return f"\033[1m{text}\033[0m"