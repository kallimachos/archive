#! /usr/bin/env python

import cgi
import athletemodel
import yate
import json
import cgitb

#cgitb.enable()

form_data = cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)
print(yate.start_response('application/json'))
print(json.dumps(athlete))