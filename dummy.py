"""Dummy module to test CI workflows
"""

def say_hi(name: str) -> None:
    """Dummy Function to say Hi

    Args:
        name (str): Name to say Hi to.
    """
    print(f"Hello {name}!!")

if __name__ == '__main__':
    say_hi("World")
