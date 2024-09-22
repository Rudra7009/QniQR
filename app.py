from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    with open('scanned_data.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')  # Add a newline for better readability
    return {"message": "Data stored successfully!"}, 200

if __name__ == '__main__':
    app.run(debug=True)
