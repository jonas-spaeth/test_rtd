class MyClass:
    """
    This is the class description.
    """
    age = None

    def __init__(self, age):
        """
        This is the initialzer for MyClass.
        Parameters
        ----------
        age : int
            This is the age

        """
        self.age = age

    def some_method(self, some_parameter):
        """
        Says Helloe to the `some_paramater`.
        Parameters
        ----------
        some_parameter : str

        Returns
        -------
        str:
            Hello `some_parameter`

        Warnings
        --------
        This is an important warning.
        """
        return f"Hello {some_parameter}!"
