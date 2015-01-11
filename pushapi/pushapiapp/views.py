import json
import hashlib
from django.http import HttpResponse, HttpResponseNotModified, HttpResponseBadRequest, HttpResponseNotAllowed
import redis
from django_grip import set_hold_longpoll

r = redis.Redis()

# return (data, hash)
def _get_door_status():
	da = r.get('doors-ajar')
	if da:
		da = json.loads(da)
	else:
		da = []
	hash = hashlib.md5(json.dumps(da)).hexdigest()[:8]
	return (da, hash)

def door_status(req):
	if req.method == 'GET':
		ds, hash = _get_door_status()
		etag = '"' + hash + '"'

		inm = req.META.get('HTTP_IF_NONE_MATCH')

		wait = req.META.get('HTTP_WAIT')
		if wait:
			try:
				wait = int(wait)
			except:
				return HttpResponseBadRequest()
			if wait < 1:
				wait = None

		if inm == etag:
			resp = HttpResponseNotModified()
			if wait:
				set_hold_longpoll(resp, 'door-status', timeout=wait)
		else:
			resp = HttpResponse(json.dumps(ds) + '\n', content_type='application/json')

		return resp
	else:
		return HttpResponseNotAllowed(['GET'])
