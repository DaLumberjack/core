"""Todo list that will track tasks for today, this week, and pastdue."""

import uuid

from homeassistant.components.todo import (
    TodoItem,
    TodoItemStatus,
    TodoListEntity,
    TodoListEntityFeature,
)


class CommunifarmTodoListEntity(TodoListEntity):
    """Representation of a Communifarm To-Do list entity."""

    def __init__(self, name, todo_type, calendar_entity) -> None:
        """Initialize the To-Do list entity."""
        self._name = f"{name} {todo_type} To-Do List"
        self._todo_type = todo_type
        self._calendar_entity = calendar_entity
        self._todo_items = []

    @property
    def name(self):
        """Return the name of the To-Do list."""
        return self._name

    @property
    def state(self):
        """Return the count of incomplete tasks."""
        return len(
            [
                item
                for item in self._todo_items
                if item.status == TodoItemStatus.NEEDS_ACTION
            ]
        )

    @property
    def todo_items(self) -> list[TodoItem]:
        """Return the ordered contents of the To-Do list."""
        return self._todo_items

    @property
    def supported_features(self):
        """Return the supported features for this To-Do list."""
        return (
            TodoListEntityFeature.CREATE_TODO_ITEM
            | TodoListEntityFeature.DELETE_TODO_ITEM
            | TodoListEntityFeature.UPDATE_TODO_ITEM
            | TodoListEntityFeature.MOVE_TODO_ITEM
            | TodoListEntityFeature.DUE_DATETIME
            | TodoListEntityFeature.DESCRIPTION
        )

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Add an item to the To-Do list."""
        item.uid = str(uuid.uuid4())
        self._todo_items.append(item)
        self.async_write_ha_state()

    async def async_delete_todo_items(self, uids: list[str]) -> None:
        """Delete items from the To-Do list."""
        self._todo_items = [item for item in self._todo_items if item.uid not in uids]
        self.async_write_ha_state()

    async def async_update_todo_item(self, item: TodoItem) -> None:
        """Update an item in the To-Do list."""
        for idx, current_item in enumerate(self._todo_items):
            if current_item.uid == item.uid:
                self._todo_items[idx] = item
                break
        self.async_write_ha_state()

    async def async_move_todo_item(
        self, uid: str, previous_uid: str | None = None
    ) -> None:
        """Move an item in the To-Do list."""
        item = next((i for i in self._todo_items if i.uid == uid), None)
        if item:
            self._todo_items.remove(item)
            if previous_uid:
                idx = next(
                    (
                        i
                        for i, it in enumerate(self._todo_items)
                        if it.uid == previous_uid
                    ),
                    0,
                )
                self._todo_items.insert(idx + 1, item)
            else:
                self._todo_items.insert(0, item)
            self.async_write_ha_state()

    async def complete_task(self, uid: str) -> None:
        """Mark a task as complete and update the calendar event."""
        item = next((i for i in self._todo_items if i.uid == uid), None)
        if item:
            item.status = TodoItemStatus.COMPLETE
            if self._calendar_entity:
                await self._calendar_entity.update_event(
                    item.uid, f"Done: {item.description}"
                )
            self.async_write_ha_state()
