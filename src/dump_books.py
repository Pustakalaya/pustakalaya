"""
Usages:
./manage.py shell --settings=pustakalaya.settings.development
import "var.www
Put this file in file where manage.py file exists
import this file
"""



def dump_data():
    with open('/var/www/html/media_root/uploads/old_pustakalaya/books.json') as f:
        books = f.read()

    import json

    books = json.loads(books)
    from pustakalaya_apps.document.models import Document

    document = Document.objects.first()
    for book in books:
        document.pk = None
        document.title = book['title']
        document.thumbnail = book['thumbnail']
        document.abstract = book['abstract']
        document.save()
        print("Saving book {} to database".format(document.title))



