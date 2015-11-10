#! /usr/bin/env python

import json
import athletemodel
import yate
import sys

names = athletemodel.get_namesID_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))