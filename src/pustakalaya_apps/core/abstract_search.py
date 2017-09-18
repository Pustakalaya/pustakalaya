from elasticsearch_dsl import DocType, Date, Text


class ItemDoc(DocType):
    """
    Common superclass for Document, Audio, Video, Wiki, Maps, and Newspaper.
    Don't get index in the index server."""
    id = Text()
    title = Text()
    abstract = Text()
    type =  Text()
    education_level = Text()
    category = Text(),
    language = Text()
    additional_note = Text()
    description = Text()
    license_type = Text()
    year_of_available = Date()
    date_of_issue = Date()
    place_of_publication = Text()
    created_date = Date()
    updated_date = Date()
    # Common fields in document, audio and video library
    publisher = Text()
    sponsors = Text(multi=True),
    collections = Text(multi=True)
    keywords = Text(multi=True)
