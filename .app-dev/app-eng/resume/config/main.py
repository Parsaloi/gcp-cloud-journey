# program code
from flask import request, current_app, Flask
from google.cloud import storage
import google.cloud.logging
import logging

BUCKET_NAME = "parsa-bucket-1"
DEFAULT_TEMPLATE_NAME = "english.html"

app = Flask(__name__)
app.debug = False
app.testing = False

# COnfigure logging
if not app.testing:
    logging.basicConfig(level=logging.INFO)
    client = google.cloud.logging.Client()
    # Attaches a Cloud Logging handler to the root logger
    client.setup_logging()

DEFAULT_TEMPLATE = "english.html"
@app.route('/')
def get():
    template = request.args.get('template', DEFAULT_TEMPLATE)
    name = request.args.get('name', None)
    company = request.args.get('company', None)
    resume_html = return_resume(template, name, company)
    return resume_html

# This is only used when running locally. When running live, gunicorn runs the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
