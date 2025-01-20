from flask import Flask, jsonify, render_template, request
import random # use for creating application numbers

app = Flask(__name__)
applications = {}


@app.route('/api/submit-application', methods=['POST'])
def submit_application():
    print("application submitting...")

    data = request.get_json()

    name = data.get('name')
    zipcode = data.get('zipcode')

    # generate a random 5 digit application number
    application_number = random.randint(10000, 99999)

    application = {
        'name': name,
        'zipcode': zipcode,
        'status': 'received'
    }

    # to store the application 
    applications[application_number] = application

    return jsonify({
        'message': 'Application successfully submitted',
        'application_number': application_number
        })


# Route to check status of application
@app.route('/api/check-status', methods=['GET'])
def check_status():
    print("checking status...")
    application_number = int(request.args.get('number'))

    if application_number in applications:
        return jsonify({'status': applications[application_number]['status']})
    return jsonify({'status': 'not found'})


# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
