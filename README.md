# Quickstart
To create a new serverless Flask application really quickly:

1. Install pipenv and AWS SAM local and generate app boilerplate:
```sh
pip install aws-sam-cli pipenv
sam init --location https://github.com/aws-samples/cookiecutter-aws-sam-python
```
2. Add `flask_serverless` dependency
```sh
cd MyApp
make install
pipenv install flask_serverless
```
3. Replace `first_function/app.py` contents with:
```python
from flask_serverless import Serverless, Flask, APIGWProxy

app = Flask(__name__)
Serverless(app)
lambda_handler = APIGWProxy(app)

@app.route('/')
def index():
    return "Hello, friend!"
```
4. You're ready to go! Run `make run`. Read the README it spits out.


### More Coming...
More documentation will be written soon.

### Further Reading
[Serverless Flask applications on AWS lambda.](https://spiegelmock.com/2018/09/06/serverless-python-web-applications-with-aws-lambda-and-flask/)
