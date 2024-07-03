from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'Salary': 'Rs.16,00,000'
}, {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'Salary': 'Rs.14,00,000'
}, {
    'id': 3,
    'title': 'Data Visualization Analyst',
    'location': 'Gurgaon, India',
}, {
    'id': 2,
    'title': 'Machine Learning Engineer',
    'location': 'Chennai, India',
    'Salary': 'Rs.18,00,000'
}]


@app.route("/")
def hello_R():
    return render_template('home.html', jobs=JOBS, company_name='R')


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


