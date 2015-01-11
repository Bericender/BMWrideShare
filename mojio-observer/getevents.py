import json
import zmq

def get_doors_ajar(m):
	out = list()
	da = m.get('DoorsAjar')
	if da:
		parts = da.split(',')
		for part in parts:
			part = part.strip()
			if part == 'None':
				continue
			out.append(part)
	return out

ctx = zmq.Context()
in_sock = ctx.socket(zmq.PULL)
in_sock.connect('ipc:///tmp/mojio-observer')

ajar = False

while True:
	m = json.loads(in_sock.recv())
	print json.dumps(m, indent=4)

	da = get_doors_ajar(m)
	if len(da) > 0 and not ajar:
		ajar = True
		print '** doors open: %s' % ', '.join(da)
	elif len(da) == 0 and ajar:
		ajar = False
		print '** doors closed'
