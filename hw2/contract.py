"""Contract decorator for second python homework."""


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object


def check_args_types(arg_types, args):
    """
    Check that all arguments match types from contract.

    Args:
        arg_types: argument types from contract.
        args: arguments.

    Raises:
        ContractError: if argument types doesn't match types from contract.

    """
    if len(arg_types) != len(args):
        raise ContractError()
    zip_args = zip(args, arg_types)
    isinstances = [isinstance(zipped[0], zipped[1]) for zipped in zip_args]
    res = all(isinstances)
    if not res:
        raise ContractError()


def check_raises(function, raises, args):
    """Check that function raises exception that match contract.

    If raises is empty tuple, then function shouldn't throw exceptions.

    Args:
        function: function to process.
        raises: allowed exception types.
        args: args for the function.

    Returns:
        returned_value: value that returns function with args parameters.

    Raises:
        ContractError: if returned value types differs from type from contract.
        Exception: exception that was raised by function.
    """
    try:
        returned_value = function(*args)
    except Exception as ex:
        if raises == () or not isinstance(ex, raises):  # noqa: WPS520
            raise ContractError() from ex
        raise ex
    return returned_value


def check_return_type(return_type, returned_value):
    """
    Check that returned value match type from contract.

    Args:
        return_type: type for return value from contract.
        returned_value: value returned from function.

    Raises:
        ContractError: if returned value types differs from type from contract.

    """
    returned_res = isinstance(returned_value, return_type)
    if not returned_res:
        raise ContractError()


def contract(arg_types=None, return_type=None, raises=None):
    """
    Create decorator, that checks function to match contract.

    Args:
        arg_types: argument types, that function can use.
        return_type: type of function returned value.
        raises: allowed exception types.

    Returns:
        decorator: decorator that could be applied to functions.
    """
    def decorator(function):
        def wrapped(*args):  # noqa: WPS430
            if arg_types is not None:
                check_args_types(arg_types, args)
            if raises is not None:
                returned_value = check_raises(function, raises, args)
            else:
                returned_value = function(*args)
            if return_type is not None:
                check_return_type(return_type, returned_value)
            return returned_value
        return wrapped
    return decorator
