"""
Create and host an endpoint with Flask.
The endpoint takes two GET request query parameters and return specific
information in JSON format.

Requirements
The information required includes:
- Slack name
- Current day of the week
- Current UTC time (with validation of +/- 2)
- Track
- The GitHub URL of the file being run
- The GitHub URL of the full source code
- A Status Code of Success
"""
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from pytz import utc


app = Flask(__name__)


def get_current_day():
    """
    Function to get the current day of the week.

    Return:
        str: the name of the current day
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday']

    return days[datetime.now().weekday()]


def get_utc_time():
    """
    Function to get the current UTC time with validation of +/- 2 hours.

    Return:
        str: the current UTC time in the format `%Y-%m-%dT%H:%M:%SZ`
    """
    utc_now = datetime.now(utc)
    utc_range = utc_now - timedelta(hours=2), utc_now + timedelta(hours=2)

    if utc_range[0] <= utc_now <= utc_range[1]:
        return utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    return 'Invalid UTC time'


@app.route('/api')
def infos():
    """
    Handle two GET request query paramaters to the '/api' endpoint

    Return:
        dict: JSON response containing the given information
    """
    slack_name = request.args.get('slack_name', 'tonybnya')
    track = request.args.get('track', 'backend')
    current_day = get_current_day()
    utc_time = get_utc_time()
    github_repo_url = 'https://github.com/tonybnya/HNGx'
    github_file_url = 'https://github.com/tonybnya/HNGx/blob/main/api.py'
    status_code = 200

    response = {
        'slack_name': slack_name,
        'track': track,
        'current_day': current_day,
        'utc_time': utc_time,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': status_code
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
