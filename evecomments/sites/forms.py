

from flask_wtf import Form
from wtforms   import StringField
from wtforms.validators import DataRequired, InputRequired, Length

from evecomments.validators.site import unique_site_id


class AddSiteForm(Form):
    """ Form for adding new sites to the comments system. """

    id   = StringField('Unique ID', validators=[DataRequired(), InputRequired(), Length(min=3, max=50), unique_site_id])
    name = StringField('Site Name', validators=[DataRequired(), InputRequired(), Length(min=3, max=50)])