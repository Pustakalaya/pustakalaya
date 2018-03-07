from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_number(value):
    number_lists = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '०', '१', '२', '३', '४', '५', '६', '७', '८', '९')

    value = value.strip()

    for val in value:
        if val not in number_lists:
            raise ValidationError(
                _('%(value)s is not a number'),
                params={'value': value},
            )

