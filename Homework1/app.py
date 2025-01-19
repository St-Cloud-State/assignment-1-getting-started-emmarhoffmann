from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
applications = []


@app.route('/api/submit-application', methods=['POST'])
def submit_application():
    print("application submitting...")

    data = request.get_json()

    name = data.get('name')
    zipcode = data.get('zipcode')

    application = {
        'name': name,
        'zipcode': zipcode
    }

    applications.append(application)
    return jsonify({'message': 'Application successfully submitted'})



# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
