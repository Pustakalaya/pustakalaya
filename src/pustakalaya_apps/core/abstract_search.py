from elasticsearch_dsl import DocType, Date, Text, Keyword


class ItemDoc(DocType):
    """
    Common superclass for Document, Audio, Video, Wiki, Maps, and Newspaper.
    Don't get index in the index server."""
    id = Text()
    title = Text(fields={'keyword': Keyword()})
    abstract = Text()
    type = Text(fields={'keyword': Keyword()})
    education_levels = Text(multi=True, fields={'keyword': Keyword()})
    communities = Text(multi=True, fields={'keyword': Keyword()})
    collections = Text(multi=True, fields={'keyword': Keyword()})
    languages = Text(multi=True, fields={'keyword': Keyword()})
    description = Text()
    license_type = Text(fields={'keyword': Keyword()})
    year_of_available = Date()
    publication_year = Date()
    created_date = Date()
    updated_date = Date()
    author_list = Text(multi=True)
