from flask import Flask, request, render_template, jsonify
from fetchCurl import FetchCurl
from convertJson import ConvertJson

app = Flask(__name__)

@app.route('/')
def getHomePage():
    url = "https://www.wikipedia.org"
    fetcher = FetchCurl(url)
    headers = fetcher.getHeaders()
    converter = ConvertJson(headers[0], headers[1])
    converter.getHeaders()
    pretty_json = converter.getPrettyJSON()
    return render_template('index.html', results = pretty_json)

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        url = request.form.get('url') 
        if url:
            fetcher = FetchCurl(url)
            headers = fetcher.getHeaders()
            # Create a ConvertJson object and parse headers
            converter = ConvertJson(headers[0], headers[1])
            converter.getHeaders()
            pretty_json = converter.getPrettyJSON()
            return render_template('results.html', results= pretty_json)
        else:
            return "Please provide a URL."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
