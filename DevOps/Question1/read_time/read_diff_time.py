from datetime import datetime
from flask import Flask
app = Flask(__name__)

format = "%Y-%m-%dT%H:%M:%S.%f"

@app.route('/')
def diff():
    with open("/app/time.txt", "r") as f:
        times = f.readlines()
    first_time = datetime.strptime(times[0].strip(' \t\r\n'), format)
    last_time = datetime.strptime(times[-1].strip(' \t\r\n'), format)
    diff = last_time - first_time
    duration_in_s = diff.total_seconds()
    days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
    hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
    seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
    return "Time between first and last time: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')