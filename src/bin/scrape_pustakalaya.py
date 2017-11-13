#!/usr/bin/env python3

"""
Scrape some old pustakalaya and save in books.json file in root dir
title
abstract
thumbnail
"""
import requests
from lxml import html
import os
import json
import subprocess
import random
import string

HOST = "pustakalaya.org"
BASE_URL = "http://pustakalaya.org/"
URL = "http://pustakalaya.org/list.php?browse=latest"
page = 1
ENDPAGE = 300
NO_OF_ITEM_PER_PAGE = 26
books = "books.json"

BASE_DIR = "uploads/old_pustakalaya"
PDF_DIR = "uploads/old_pustakalaya/pdf"
THUMBNAIL_DIR = "uploads/old_pustakalaya/thumbnail"

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(THUMBNAIL_DIR, exist_ok=True)


def get_book_pdf(pdf_url=None, save_dir=PDF_DIR):
    if pdf_url is None:
        return None

    # Get the thumbnail and save to disk and return thumbnail path.
    """
    method to save an image to disk
    """

    # Create a random image name
    print("Pdf name", pdf_url.split('=')[-1])
    pdf_name = pdf_url.split('=')[-1]

    # Request an image from web
    print("Requesting book pdf", pdf_url)
    raw_pdf = requests.get(pdf_url)
    # Save image to disk or django Media root
    if raw_pdf.status_code != 200:
        print("Can't save pdf")
        return None

        # If directory not exist create dir
        # TODO: move from here.
        os.makedirs(save_dir, exist_ok=True)

    with open(pdf_name, "wb") as pdf:
        for block in raw_pdf.iter_content(1024):
            if not block:
                break

            pdf.write(block)

    subprocess.call("mv {} {}".format(pdf_name, save_dir), shell=True)
    return "{}".format(os.path.join(save_dir, pdf_name))


def get_book_thumbnail(book_thumbnail_url=None, save_dir=THUMBNAIL_DIR):
    if book_thumbnail_url is None:
        return " "

    # Get the thumbnail and save to disk and return thumbnail path.
    """
       method to save an image to disk
    """

    # Create a random image name
    image_name = "".join(
        random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(30))
    # Add extension to image name
    image_name = "{0}.jpg".format(image_name)

    # Create a random image name
    print("Image name", image_name)

    # Request an image from web
    print("Requesting book thumbnail", book_thumbnail_url)
    raw_image = requests.get(book_thumbnail_url)
    # Save image to disk or django Media root
    if raw_image.status_code != 200:
        print("Can't save image")
        return None

        # If directory not exist create dir
        os.makedirs(save_dir, exist_ok=True)

    with open(image_name, "wb") as thumbnail:
        for block in raw_image.iter_content(1024):
            if not block:
                break

            thumbnail.write(block)

    subprocess.call("mv {} {}".format(image_name, save_dir), shell=True)
    return "{}".format(os.path.join(save_dir, image_name))


def get_book_metadata(book_url="http://pustakalaya.org/view.php?pid=Pustakalaya:8014"):
    """
    Scrape book metadata
    :param book_url:
    :return: ()
    """

    book_page = requests.get(book_url)
    # If request not succed continue to next page
    if book_page.status_code != 200:
        print("Unknown error while accessing book page {}  ".format(book_url))
        return

    # create a tree
    tree = html.fromstring(book_page.content)
    # Get metadata.
    place_of_publication = "".join(tree.xpath('//*[@id="metadata"]/table/tbody/tr[2]/td[2]/text()')) or " "
    language = "".join(tree.xpath('//*[@id="metadata"]/table/tbody/tr[6]/td[2]/text()')) or " "
    publication_year = tree.xpath('//*[@id="metadata"]/table/tbody/tr[4]/td[2]/text()') or " "
    pdf_url = tree.xpath('//*[@id="media-content"]/a/@href') or " "
    book_thumbnail_url = "".join(tree.xpath('//*[@id="thumbnail"]/img/@src')) or " "
    total_pages = "".join(tree.xpath('//*[@id="metadata"]/table/tbody/tr[5]/td[2]/text()')).strip() or " "
    abstract = "".join(tree.xpath('//*[@id="data"]/p/text()')) or " "

    if place_of_publication is not None and language is not None and publication_year is not None and pdf_url is \
        not None and book_thumbnail_url is not None and total_pages is not None and abstract is not None:
        # Make some clean up.


        place_of_publication = place_of_publication.strip() or " "
        language = language.strip() or " "
        publication_year = str(publication_year[0][0]).strip() or " "
        book_pdf_url = "{}{}".format(BASE_URL, "".join(pdf_url[0]).strip().lstrip('/')) or " "
        total_pages = total_pages[0].strip() or " "
        abstract = abstract.strip() or " "
        book_thumbnail_url = BASE_URL + "/" + book_thumbnail_url
        print(book_thumbnail_url)
        book_pdf_path = get_book_pdf(book_pdf_url) or " "
        book_thumbnail_path = get_book_thumbnail(book_thumbnail_url) or " "

        metadata = (
            place_of_publication,
            language,
            publication_year,
            book_pdf_path,
            book_thumbnail_path,
            total_pages,
            abstract
        )

        print(place_of_publication, language, publication_year, book_pdf_path, book_thumbnail_path, total_pages,
              abstract)

        return metadata


def scrape():
    for i in range(0, ENDPAGE + 1):
        # Construct a url for each page
        url = "{0}&pager_row={1}".format(URL, i)
        print("Scarping Page {}".format(i))
        print("URL: {}".format(url))

        # Request a page
        page = requests.get(url)

        # If request not succed continue to next page
        if page.status_code != 200:
            print("Unknown Error in page {} while requesting ".format(i))
            continue

        tree = html.fromstring(page.content)

        for book_no in range(1, NO_OF_ITEM_PER_PAGE):
            """
            //*[@id="view_content"]/form/div[3]/li[1]/div/div/div[2]/a/b
            //*[@id="view_content"]/form/div[3]/li[1]/div/div/div[2]/a

            //*[@id="view_content"]/form/div[3]/li[2]/div/div/div[2]/a
            //*[@id="view_content"]/form/div[3]/li[2]/div/div/div[2]/a/b
            """
            title = "".join(
                tree.xpath(
                    ' //*[@id="view_content"]/form/div[3]/li[' + str(book_no) + ']/div/div/div[2]/a/b/text()')) or None
            book_url = BASE_URL + "".join(
                tree.xpath(
                    '//*[@id="view_content"]/form/div[3]/li[' + str(book_no) + ']/div/div/div[2]/a/@href')) or None

            if book_url is None:
                print("Book url is None")
                exit()

            if title is not None and book_url is not None:
                # parse metadata
                print("Scraping metadata of book {}".format(book_no))
                place_of_publication, \
                language, \
                publication_year, \
                book_pdf, \
                book_thumbnail, \
                total_pages, \
                abstract = get_book_metadata(book_url)

                data = {
                    "title": title,
                    "place_of_publication": place_of_publication,
                    "language": language,
                    "publication_year": publication_year,
                    "book_pdf": book_pdf,
                    "thumbnail": book_thumbnail,
                    "total_pages": total_pages,
                    "abstract": abstract
                }

                with open(books, "a+") as json_file:
                    print()
                    print("Saving data.\n", data, end="\n")
                    json_file.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    scrape()

    # Format json file
    with open(books, "a+") as json_file:
        json_file.seek(0)
        json_file.write("[")
        json_file.seek(2)
        json_file.write("]")


class OleScrapper(object):
    """
    Ole scapper which scrape web pages.
    """
    BASE_URL = "http://pustakalaya.org/list.php?browse=latest"
    BASE_DIR = "/var/www/html"

    def __init__(self, page_no):
        self.page_no = page_no
        self.url = "{}&pager_row={}".format(BASE_URL, self.page_no)
        self.data = None
        self.thumbnal_dir = os.path.join("uploads", "{}".format(page_no), "thumbnail_dir")
        self.pdf_dir = os.path.join("uploads", "{}".format(page_no), "pdf_dir")
        # Create a directory save data.
        os.makedirs(os.path.join(BASE_DIR, self.thumbnal_dir), exist_ok=True)
        os.makedirs(os.path.join(BASE_DIR, self.pdf_dir), exist_ok=True)

    def save_pdf(self):
        pass

    def save_thumbnail(self):
        pass

    def export_data(self):
        pass

    def start(self):
        """
        Start scraping and sexport
        :return:
        """
        self.export_data()

        # Create 301 scappers
        # scrappers = [OleScrapper(page_no=page_no) for page_no in range(301)]

        # start scraping
        # for scrapper in scrappers:
        #   scrapper.start()

#
