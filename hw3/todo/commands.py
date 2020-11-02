"""Commands for CLI."""

from todo.custom_exceptions import UserExitException
from todo.models import BaseItem
from todo.reflection import find_classes


class BaseCommand(object):
    """Base class for commands."""

    label: str

    def perform(self, store):
        """Perform command.

        Args:
            store: storage with todos.

        Raises:
            NotImplementedError: abstract class.
        """
        raise NotImplementedError()


class ListCommand(BaseCommand):
    """List command."""

    label = 'list'

    def perform(self, store):
        """Show all todos.

        Args:
            store: storage with todos.
        """
        if not store.items:
            print('There are no items in the storage.')  # noqa: WPS421
            return

        for index, store_item in enumerate(store.items):
            print('{0}: {1}'.format(index, str(store_item)))  # noqa: WPS421


class NewCommand(BaseCommand):
    """New command."""

    label = 'new'

    def perform(self, store):  # noqa: WPS210 WPS213
        """Add new item.

        Args:
            store: storage with todos.

        Returns:
            new_object: created object.
        """
        classes = self._load_item_classes()

        print('Select item type:')  # noqa: WPS421
        for index, name in enumerate(classes.keys()):
            print('{0}: {1}'.format(index, name))  # noqa: WPS421

        selected_key = None

        while True:
            try:
                selected_key = self._select_item(classes)
            except ValueError:
                print('Bad input, try again.')  # noqa: WPS421
            except IndexError:
                print('Wrong index, try again.')  # noqa: WPS421
            else:
                break

        selected_class = classes[selected_key]
        print('Selected: {0}'.format(selected_class.__name__))  # noqa: WPS421
        print()  # noqa: WPS421

        new_object = selected_class.construct()

        store.items.append(new_object)
        print('Added {0}'.format(str(new_object)))  # noqa: WPS421
        print()  # noqa: WPS421
        return new_object

    def _load_item_classes(self) -> dict:
        # Dynamic load:
        return dict(find_classes(BaseItem))

    def _select_item(self, classes):
        selection = int(input('Input number: '))  # noqa: S322 WPS421
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return list(classes.keys())[selection]


class ExitCommand(BaseCommand):
    """Exit command."""

    label = 'exit'

    def perform(self, _store):
        """Exit from app.

        Args:
            _store: storage with todos.

        Raises:
            UserExitException: exception to close app.
        """
        raise UserExitException('See you next time!')


class DoneCommand(BaseCommand):
    """Done command."""

    label = 'done'
    value_to_set = True

    def perform(self, store):
        """Mark command as done.

        Args:
            store: storage with todos.
        """
        try:
            change_status(store, self.value_to_set)
        except IndexError as ex:
            print(ex)  # noqa: WPS421


class UndoneCommand(BaseCommand):
    """Undone command."""

    label = 'undone'
    value_to_set = False

    def perform(self, store):
        """Mark command as undone.

        Args:
            store: storage with todos.
        """
        try:
            change_status(store, self.value_to_set)
        except IndexError as ex:
            print(ex)  # noqa: WPS421


def change_status(store, status_to_set):
    """Set status for item.

    Args:
        store: storage with todos.
        status_to_set: status which would be setted.

    Raises:
        IndexError: if user input wrong ID.
    """
    todo_id = int(input('Enter Todo ID: '))  # noqa: S322 WPS421

    if todo_id > len(store.items) - 1:
        raise IndexError('ID needs to be in list')

    store.items[todo_id].done = status_to_set
