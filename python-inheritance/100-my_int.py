class MyInt(int):
    """MyInt class inherits from int and inverts the == and != operators."""

    def __eq__(self, other):
        """
        Overrides the equality operator to invert its logic.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator to invert its logic.
        """
        return super().__eq__(other)
