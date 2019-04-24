# CityScore
City of Chelsea City Score


### How to run this app locally?
1. Clone the repo
2. Navigate to the backend directory.
  * Ensure virtualenv is installed:
  ~~~
  python3 -m pip install --user virtualenv
  ~~~
  * Create the venv using the following command:
  ~~~
  python3 -m venv venv
  ~~~
  * Activate the venv using the following command:
  ~~~
  source venv/bin/activate
  ~~~
  * After activating the venv, install the dependencies in requirements.txt
  ~~~
  pip install -r requirements.txt
  ~~~
  * Run the insert_scores.py file.
  * Start the backend by using the following commands:

  ~~~
  export FLASK_APP=backend.py flask
  flask run
  ~~~
3. Navigate to the client directory.
  * Install node modules
  ~~~
  npm install
  ~~~
  * Start the react app!
  ~~~
  npm start
  ~~~

