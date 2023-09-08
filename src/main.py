from csv import writer
from pandas import read_csv
import requests
from requests_html import HTMLSession

from constants import chat_id, headers, idealista_search_url, path_to_file, telegram_token


def notify_telegram(link):
    msg = f"There is a new apartment {link}"
    requests.get(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={msg}")


def check_new_apartments(apartments):
    apartments_sent = read_csv(path_to_file)["ID"].to_list()

    with open(path_to_file, "a") as csv_file:
        writer_object = writer(csv_file)

        for apartment in apartments:
            info = apartment.find("div.item-info-container", first=True)
            direct = info.find("a.item-link", first=True) if info else None

            if direct:
                link = list(direct.absolute_links)[0]
                floor_id = link.split("/")[4]

                if int(floor_id) not in apartments_sent:
                    notify_telegram(link)
                    writer_object.writerow([floor_id])

        csv_file.close()


def get_last_apartments():
    session = HTMLSession()
    request = session.get(idealista_search_url, headers=headers)

    last_apartments = request.html.find("article")
    last_apartments.pop(0)

    check_new_apartments(last_apartments)


get_last_apartments()
