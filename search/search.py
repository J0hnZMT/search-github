import requests
import argparse
from datetime import datetime
import csv
import getpass


def csv_date_time():
    # add date and time to the output
    now = datetime.now()
    datetime_now = now.strftime("%Y-%m-%d-%H-%M")
    csv_filename_now = "output-{}.csv".format(datetime_now)
    return csv_filename_now


def auth(user, passwd, term):
    requests.get('https://api.github.com/user', auth=(user, passwd))
    r = requests.get('https://api.github.com/rate_limit')
    print(r.content)
    search(term)


def search(term):
    filename = csv_date_time()
    with open(filename, "a+", newline='', encoding='utf-8') as csv_file:
        # header for the csv file
        field_header = ['Project Name', 'Description', 'Url', 'Programming Language', 'Date Updated']
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_header)
        csv_writer.writeheader()
        for page in range(1, 15):
            term_to_search = {'q': term, 'page': page}
            search_term = requests.get('https://api.github.com/search/repositories', params=term_to_search)
            print(search_term.url)
            json_result = search_term.json()
            items = json_result['items']
            for item in items:
                result = {'Project Name': item['name'], 'Description': item['description'], 'Url': item['html_url'],
                          'Programming Language': item['language'], 'Date Updated': item['updated_at']}
                csv_writer.writerow(result)
    print("Search Successful!")


def main():
    """ Main Function of the program """
    parser = argparse.ArgumentParser()
    parser.add_argument("user", nargs='?', help="Your username in Github", type=str)
    parser.add_argument("passwd", nargs='?', help="Your Password in Github", type=str)
    parser.add_argument("term", nargs='?', help="The term you want to search in Github", type=str)
    args = parser.parse_args()
    auth(args.user, args.passwd, args.term)


if __name__ == '__main__':
    main()