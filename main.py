from flask import escape
import functions_framework

import telegrambot


@functions_framework.http
def tv_telegram_bot(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    if request.method == 'POST':
        telegrambot.sendMessage(request.data.decode('utf-8'))
        return 'done'
    else:
        return 'Unknown request type'
