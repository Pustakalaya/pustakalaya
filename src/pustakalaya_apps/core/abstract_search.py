from elasticsearch_dsl import DocType, Date, Text


class ItemDoc(DocType):
    """
    Common superclass for Document, Audio, Video, Wiki, Maps, and Newspaper.
    Don't get index in the index server."""
    id = Text()
    title = Text()
    abstract = Text()
    type = Text()
    education_levels = Text(multi=True)
    communities = Text(multi=True)
    collections = Text(multi=True)
    languages = Text(multi=True)
    description = Text()
    license_type = Text()
    year_of_available = Date()
    publication_year = Date()
    created_date = Date()
    updated_date = Date()
