import logging
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    testsecret = os.getenv("TESTSECRET")
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function was deployed using terraform. The secret is {testsecret}")
    else:
        return func.HttpResponse(
             f"I'm deployed using terraform! Pass a name in the query string or in the request body for a personalized response. The secret is {testsecret}",
             status_code=200
        )
