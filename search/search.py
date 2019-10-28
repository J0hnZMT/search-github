import requests
import argparse
from datetime import datetime
import csv
import getpass


class Password:

    DEFAULT = 'Prompt if not specified'

    def __init__(self, passwd):
        if passwd == self.DEFAULT:
            passwd = getpass.getpass('Github Password: ')
        self.passwd = passwd

    def __str__(self):
        return self.passwd


def csv_date_time():
    # add date and time to the output
    now = datetime.now()
    datetime_now = now.strftime("%Y-%m-%d-%H-%M")
    csv_filename_now = "output-{}.csv".format(datetime_now)
    return csv_filename_now


def auth(term, user, passwd):
    requests.get('https://api.github.com/user', auth=(user, passwd))
    search(term)


def search(term):
    filename = csv_date_time()
    with open(filename, "a+", newline='', encoding='utf-8') as csv_file:
        # header for the csv file
        field_header = ['Project Name', 'Description', 'Url', 'Programming Language', 'Date Updated']
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_header)
        csv_writer.writeheader()
        try:
            for page in range(1, 12):
                term_to_search = {'q': term, 'per_page': 100, 'page': page}
                search_term = requests.get('https://api.github.com/search/repositories', params=term_to_search)
                json_result = search_term.json()
                items = json_result['items']
                for item in items:
                    result = {'Project Name': item['name'], 'Description': item['description'], 'Url': item['html_url'],
                              'Programming Language': item['language'], 'Date Updated': item['updated_at']}
                    csv_writer.writerow(result)
        except KeyError as e:
            print("Search Done! Search results save in {}".format(filename))


def main():
    """ Main Function of the program """
    parser = argparse.ArgumentParser()
    parser.add_argument("term", nargs='?', help="The term you want to search in Github", type=str)
    parser.add_argument('-u', '--username', nargs='?', help="Your username in Github", type=str)
    parser.add_argument('-p', '--password', type=Password, help='Specify password',
                        default=Password.DEFAULT)
    args = parser.parse_args()
    auth(args.term, args.username, args.password)


if __name__ == '__main__':
    main()