"""Calednar for tracking things to do in a communifarm."""

from typing import Any

from homeassistant.components.calendar import CalendarEntity


class CommunifarmCalendar(CalendarEntity):
    """Representation of a Communifarm calendar."""

    def __init__(self, name, calendar_type) -> None:
        """Initialize the calendar."""
        self._name = name
        self._calendar_type = calendar_type
        self._events = []

    @property
    def name(self):
        """Return the name of the calendar."""
        return f"{self._name} {self._calendar_type} Calendar"

    @property
    def event(self):
        """Return the next upcoming event."""
        if not self._events:
            return None
        return self._events[0]

    @property
    def event_description(self):
        """Return the description of the next event."""
        if self._events:
            return self._events[0].get("description")

    def add_event(self, title, start_time, end_time, description=""):
        """Add an event to the calendar."""
        event = {
            "title": title,
            "start": start_time,
            "end": end_time,
            "description": description,
        }
        self._events.append(event)
        # Sort events by start time
        self._events.sort(key=lambda x: x["start"])

    def remove_event(self, event_id):
        """Remove an event from the calendar."""
        self._events = [event for event in self._events if event["id"] != event_id]

    def async_get_events(self, hass, start_date, end_date):
        """Get events in a specific date range."""
        return [
            event
            for event in self._events
            if event["start"] >= start_date and event["end"] <= end_date
        ]

    async def async_update_event(
        self,
        uid: str,
        event: dict[str, Any],
        description: str,
        recurrence_id: str | None = None,
        recurrence_range: str | None = None,
    ) -> None:
        """Update the event description in the calendar."""
        for evnt in self._events:
            if evnt["id"] == uid:
                evnt["description"] = description
                break
