"""Serverless flask app setup."""
# load vendor path for the app
import logging
import os
import sys
vendor_path = os.path.abspath(os.path.join(__file__, '..', '..', 'vendor'))
lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(lib_path)
sys.path.append(vendor_path)

from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields
from flask import current_app, _app_ctx_stack, Flask, jsonify
from flask_cors import CORS
import aws_lambda_wsgi
from flask_apispec import use_kwargs, marshal_with


# APIGW proxy / AWSGI bridge method
def APIGWProxy(app: Flask):
    """Use like `lambda_handler = APIGWProxy(app)` in your app entry point"""
    return lambda event, context: aws_lambda_wsgi.response(app, event, context)

class Serverless(object):
    def __init__(self, app: Flask=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Set up serverless flask app configuration."""
        # load config
        app.config.from_pyfile('config.py', silent=True)

        # optional local config
        app.config.from_pyfile('local.cfg', silent=True)
        app.teardown_appcontext(self.teardown)

        ctx = _app_ctx_stack.top

        CORS(app)

        self.boto_setup()
        self.log_setup(app)
        self.swagger_setup(app)

    def teardown(self, exception):
        """App context being released."""
        ctx = _app_ctx_stack.top

    def boto_setup(self):
        import boto3
        # boto_session = boto3.session.Session()
        # print(f"REGION: {boto_session.region_name}")
        # boto3.setup_default_session(region_name=os.getenv('TEST_REGION', 'eu-central-1'))
        boto3.set_stream_logger('botocore', level=logging.INFO)

    def log_setup(self, app):
        slack_log_endpoint = app.config.get('SLACK_LOG_ENDPOINT')
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        handlers = [ch]

        # enable logging to slack?
        if slack_log_endpoint:
            from slack_logger import SlackHandler, SlackFormatter
            sh = SlackHandler(slack_log_endpoint)
            sh.setFormatter(SlackFormatter())
            sh.setLevel(logging.WARN)
            handlers.append(sh)

        logging.basicConfig(handlers=handlers)
        logging.getLogger('botocore.vendored.requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
        logging.getLogger('botocore.credentials').setLevel(logging.WARNING)

    def swagger_setup(self, app, title: str='Serverless App', version: str='v1'):
        """Add swagger documentation."""
        from flask_apispec.extension import FlaskApiSpec
        from apispec import APISpec
        # swagger
        app.config.update({
            'APISPEC_SPEC': APISpec(
                title=title,
                version=version,
                plugins=[MarshmallowPlugin()],
            ),
            'APISPEC_SWAGGER_URL': '/swagger/',
        })
        FlaskApiSpec(app)
