# from ._invisible_module_in_subpackage import *


def foo(name):
    """

    Parameters
    ----------
    name : str
        Your name.
    Returns
    -------
    str:
        This is a submodule, `name`.
    """
    return f"This is a submodule, {name}."