import logging
import random

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    failprecent = req.params.get('percent')
    if not failprecent:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            failprecent = req_body.get('percent')

    if failprecent:
        logging.info('Percent: %s', failprecent)

        # choose a random number between 0 and 100 and put in variable selection
        selection = random.randint(0, 100)
        logging.info(f'Random number generated: {selection}')

        # if selection is greater than the failpercent return a http 500 error 
        # else return a success http 200 response
        if int(failprecent) >= selection:
            logging.info('Returning HTTP 500 error.')
            return func.HttpResponse(status_code=500)
        else:
            return func.HttpResponse(status_code=200)

    else:
        return func.HttpResponse(
             "Try again with a percentage chance of failure by passing in 'percent' as a query string or as a message body of the request",
             status_code=418
        )
