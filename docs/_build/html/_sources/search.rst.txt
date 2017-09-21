This module contains all the DocType which are mapped to django models plus all the resuble common field
For instance community/search.py contains community_field as this field is repeated across the community model
Another example is collection/search.py contains collection_filed as it repeated across all the audio, video, document
and other Doctype.

core/abstract_search.py contains abstractdoc type fields that reuse by other doctype class.
