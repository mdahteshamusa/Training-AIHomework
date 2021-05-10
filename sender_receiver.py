import json
from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/ping', methods=['POST'])
def req_ping(url):
    # handle the POST request
        resp = request.get(url)
        opt=heal(resp)
        return opt

 
@app.route('/health', methods=['GET'])  
def heal(url):
	resp = req_ping()
	hel=resp.get(url,data='health')
	return hel
	
	
	
@app.route('/api/v1/info', methods=['GET'])
def ur():
	js={'Receiver': 'Cisco is the best!'}
	r = requests.post('https://httpbin.org/post',data = js)
	return json.dumps(r)