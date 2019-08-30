from pytz import all_timezones

TIME_ZONES = all_timezones

TIME_ZONES_CHOICES = [(time_zone, time_zone) for time_zone in TIME_ZONES]
