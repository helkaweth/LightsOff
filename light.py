import requests
import threading
import gc

def turnoff():
	gc.enable()
	threading.Timer(5.0,turnoff).start()
	payload = '{"on": false}'
	r = requests.put("http://192.168.1.110/api/4AwLcVXAZJFY0mGbijjhgHG95PS7J4ROAheG1LO2/lights/8/state",data=payload)
	gc.collect()
	gc.disable()
turnoff()