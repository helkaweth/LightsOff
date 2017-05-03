import requests
import threading
import gc

def turnoff():
	gc.enable()
	threading.Timer(5.0,turnoff).start()
	payload = '{"on": false}'
	r = requests.put("http://x.x.x.x/api/x/lights/8/state",data=payload)
	gc.collect()
	gc.disable()
turnoff()
