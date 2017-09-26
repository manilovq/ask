def app(environ, start_response):
    data = ''
    for line in environ['QUERY_STRING'].split("&"):
        data = data + str(line).encode() #+ br'\n'
    start_response(r'200 OK', [('Content-Type', 'text/plain')])
    return [data]
