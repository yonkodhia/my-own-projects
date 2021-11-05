from http.server import HTTPServer , BaseHTTPRequestHandler


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_response('content-type' , 'text/html')
        self.end_headers()
        self.wfile.write('Hello Dhia !'.encode())



def main():
   PORT = 8000
   server = HTTPServer(('' , PORT) , helloHandler)
   print('server running on port %s' % PORT)
   server.serve_forever()


if __name__ == '_main_':
    main()