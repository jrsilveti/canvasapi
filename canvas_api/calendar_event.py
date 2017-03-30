from canvas_api.canvas_object import CanvasObject
from canvas_api.util import combine_kwargs


class CalendarEvent(CanvasObject):

    def delete(self, **kwargs):
        """
        Delete this calendar event.

        :calls: `DELETE /api/v1/calendar_events/:id \
        <https://canvas.instructure.com/doc/api/calendar_events.html#method.calendar_events_api.destroy>`_

        :rtype: :class:`canvas_api.calendar_event.CalendarEvent`
        """
        response = self._requester.request(
            'DELETE',
            'calendar_events/%s' % (self.id),
            **combine_kwargs(**kwargs)
        )
        return CalendarEvent(self._requester, response.json())

    def edit(self, **kwargs):
        """
        Modify this calendar event.

        :calls: `PUT /api/v1/calendar_events/:id \
        <https://canvas.instructure.com/doc/api/calendar_events.html#method.calendar_events_api.update>`_

        :rtype: :class:`canvas_api.calendar_event.CalendarEvent`
        """
        response = self._requester.request(
            'PUT',
            'calendar_events/%s' % (self.id),
            **combine_kwargs(**kwargs)
        )

        if 'title' in response.json():
            super(CalendarEvent, self).set_attributes(response.json())

        return CalendarEvent(self._requester, response.json())

    def __str__(self):
        return "{} ({})".format(self.title, self.id)
