import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_headers = request.headers


    file_id = request_headers['file_id']
    file_name = request_headers['name']

    result = {}
    result['headers'] = str({key: value for key, value in request_headers.items()})

    result['name'] = 'world'
    result['video_url'] = ''
    result['caption'] = ''
    result['cover_frame'] = str(0)

    return result
