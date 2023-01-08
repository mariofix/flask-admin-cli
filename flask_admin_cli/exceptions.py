# flask_admin_cli/exceptions.py
"""
Exceptions
"""


class InvalidParamsException(Exception):
    """Some of the parameters are invalid"""

    pass


class InvalidBranchException(Exception):
    """The selected branch cannot be cloned"""

    pass


class NotReadyException(Exception):
    """The selected branch cannot be cloned"""

    pass


class RemoteBranchNotFoundException(Exception):
    """The remote branch does not exist"""

    pass
