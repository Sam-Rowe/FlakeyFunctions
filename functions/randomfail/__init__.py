import logging
import random

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # random fail
    fail = random.randint(0, 1)
    logging.info(f'fail: {fail}')

    # if fail is true, return 500 error
    # otherwise, return 200 success
    if fail:
        logging.info('HTTP request failed.')
        return func.HttpResponse(status_code=500)
    else:
        logging.info('HTTP request succeeded.')
        return func.HttpResponse(status_code=200)
