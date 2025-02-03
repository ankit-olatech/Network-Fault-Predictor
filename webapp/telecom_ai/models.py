from django.db import models

# Create your models here.
class NetworkLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    latency = models.FloatField()
    packet_loss = models.FloatField()
    jitter = models.FloatField()
    label = models.CharField(max_length=20, choices=[('Normal', 'Normal'), ('Faulty', 'Faulty')])

    def __str__(self):
        return f"Log at {self.timestamp} - {self.label}"