import requests
from requests.exceptions import RequestException
import json
from json import JSONDecodeError
from datetime import datetime
from pytz import timezone


def get_midnighters(attempt):
    midnight_hour_limit = 3

    users = set()

    for attempt in attempts:
        user_time = datetime.fromtimestamp(
            attempt['timestamp'],
            tz=timezone(attempt['timezone'])
        )

        if user_time.hour < midnight_hour_limit:
            users.add(attempt['username'])

    return users


def get_response_from_page(page_number):
    api_address = 'https://devman.org/api/challenges/solution_attempts'
    response = requests.get(api_address, params={'page': page_number})
    return {
        'status_code': response.status_code,
        'text': response.text
    }


def load_attempts():
    current_page_number = 1

    while True:
        try:
            current_page_response = get_response_from_page(current_page_number)
        except RequestException:
            raise StopIteration()

        if current_page_response.get('status_code') != 200:
            raise StopIteration()

        try:
            page_data = json.loads(current_page_response.get('text'))
        except JSONDecodeError:
            raise StopIteration()

        for record in page_data['records']:
            yield record

        if current_page_number == page_data['number_of_pages']:
            raise StopIteration()

        current_page_number = current_page_number + 1


if __name__ == '__main__':
    attempts = load_attempts()

    midnighters = get_midnighters(attempts)

    for _index, midnighter in enumerate(midnighters):
        print("{}: {}".format(_index, midnighter))
