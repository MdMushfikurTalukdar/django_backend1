from django.db import models

class RoomBooking(models.Model):
    room_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    booked_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.room_name} ({self.start_date} to {self.end_date})"
