"""Items which user can add."""


class BaseItem(object):
    """Base class for item."""

    def __init__(self, heading):
        """Init class.

        Args:
            heading: heading of item.
        """
        self.heading = heading
        self.done = False

    def __repr__(self):
        """Representation of class.

        Returns:
            repr: class name.
        """
        return self.__class__.__name__

    @classmethod
    def construct(cls):
        """Construct item.

        Raises:
            NotImplementedError: abstract class.
        """
        raise NotImplementedError()


class ToDoItem(BaseItem):
    """Item for todos."""

    def __str__(self):
        """Representation of item.

        Returns:
            str: representation.
        """
        status = '+' if self.done else '-'
        return '{0} {1}: {2}'.format(
            status,
            'ToDo',
            self.heading,
        )

    @classmethod
    def construct(cls):
        """Construct item.

        Returns:
            obj: constructed item.
        """
        heading = input('Input heading: ')  # noqa: S322 WPS421
        return cls(heading)


class ToBuyItem(BaseItem):
    """Item to buy."""

    def __init__(self, heading, price):
        """Init class.

        Args:
            heading: heading of item.
            price: price of the item.
        """
        super().__init__(heading)
        self.price = price

    def __str__(self):
        """Representation of item.

        Returns:
            str: representation.
        """
        status = '+' if self.done else '-'
        return '{0} {1}: {2} for {3}'.format(
            status,
            'ToBuy',
            self.heading,
            self.price,
        )

    @classmethod
    def construct(cls):
        """Construct item.

        Returns:
            obj: constructed item.
        """
        heading = input('Input heading: ')  # noqa: S322 WPS421
        price = input('Input price: ')  # noqa: S322 WPS421
        return cls(heading, price)


class ToReadItem(BaseItem):
    """Item to read."""

    def __init__(self, heading, url):
        """Init class.

        Args:
            heading: heading of item.
            url: url where item stores.
        """
        super().__init__(heading)
        self.url = url

    def __str__(self):
        """Representation of item.

        Returns:
            str: representation.
        """
        status = '+' if self.done else '-'
        return '{0} {1}: {2} {3}'.format(
            status,
            'ToRead',
            self.heading,
            self.url,
        )

    @classmethod
    def construct(cls):
        """Construct item.

        Returns:
            obj: constructed item.
        """
        heading = input('Input heading: ')  # noqa: S322 WPS421
        url = input('Input url: ')  # noqa: S322 WPS421
        return cls(heading, url)
