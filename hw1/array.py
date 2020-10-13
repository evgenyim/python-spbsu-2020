"""This is class for storing objects."""


class Array(object):  # noqa: WPS214
    """Class for storing objects."""

    def __init__(self, *elements):
        """
        Create storage for objects.

        Args:
            elements: objects to store.
        """
        self._data = elements  # noqa: WPS110

    def append(self, elem):
        """
        Add element to storage.

        Args:
            elem: element to add.
        """
        self._data = self._data + (elem,)  # noqa: WPS110

    def __len__(self):
        """
        Return amount of elements in storage.

        # noqa: DAR201
        """
        return len(self._data)  # noqa: WPS110

    def __add__(self, other):
        """
        Add element to storage.

        Args:
            other: element to add.

        Returns:
            array_sum: sum of input arrays.

        Raises:
            TypeError: if other is not of Array type.
        """
        if not isinstance(other, Array):
            raise TypeError
        elements_sum = self._data + other.get_data()  # noqa: WPS110
        return Array(*elements_sum)

    def index(self, elem):
        """
        Find position of element in storage.

        Args:
            elem: element to find.

        Returns:
            index: index of element in storage or -1.
        """
        if elem not in self._data:  # noqa: WPS110
            return -1
        return self._data.index(elem)

    def pop(self, index):
        """
        Remove element by index.

        Args:
            index: index of element to remove.
        """
        if index != -1:  # noqa: WPS504
            self._data = self._data[:index] + self._data[index + 1:]  # noqa: WPS110 E501
        else:
            self._data = self._data[:index]  # noqa: WPS110

    def remove(self, elem):
        """
        Remove element by value.

        Args:
            elem: value of element to remove.
        """
        index = self.index(elem)
        if index != -1:
            self.pop(index)

    def __getitem__(self, index):
        """
        Remove element by index.

        Args:
            index: index of element to remove.

        Returns:
            value: element from storage
        """
        return self._data[index]

    def __eq__(self, other):
        """
        Remove element by index.

        Args:
            other: Array to compare.

        Returns:
            equal: True if Arrays are equal, else False.
        """
        if not isinstance(other, Array):
            return False
        return self._data == other.get_data()

    def get_data(self):
        """
        Return storage.

        Returns:
            data: storage.
        """
        return self._data
