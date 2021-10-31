from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        
#        with open("./Website/_site/index.html") as htmlFile:
#            self.wfile.write(htmlFile.read().encode())

        self.wfile.write('<html><body><h>Hello World!</h></body></html>'.encode())

    def log_message(self, format, *args):
        print(format % args)

httpd = HTTPServer(('', 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()
