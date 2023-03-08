from flask import Flask, render_template, jsonify #jsonify converts to JSON for us

app = Flask(__name__)
#This is a Python dictionary:
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 1,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'San Francisco, USA',
  'salary': '$150,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': '$120,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Remote',
}]


@app.route("/")
def render_home():
  return render_template('home.html', jobs=JOBS, company_name='Jamie')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',
          debug=True)  #Lets us run it locally on local host 0.0.0.0
