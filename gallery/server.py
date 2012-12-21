import SimpleHTTPServer
import SocketServer ,sys,os

handler = SimpleHTTPServer.SimpleHTTPRequestHandler 
httpd = SocketServer.TCPServer(("",8012),handler)

print "server on port 8012..."

httpd.serve_forever()

