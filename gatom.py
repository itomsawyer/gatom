import argparse
from jinja2 import  PackageLoader , Environment
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__),os.path.pardir))

env = Environment(loader = PackageLoader('gatom','templates'))

"""
template = env.get_template('menu.jinja2')
print template.render()
"""

class album:
    name = 'gallery'
    path = ''
    cover = ''
    totalPhoto = 0
    totalSubAlbum = 0
    subAlbum = list()
    photo = list()
    

def runHttpServer(documentRoot,port):
    os.chdir(documentRoot)
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler 
    httpd = SocketServer.TCPServer(("",port),handler)

    print "server on port 8012..."

    httpd.serve_forever()

def analyseGalleryStruct(srcPath):
    
    print os.walk(srcPath).

def process(args):
    "Initialize arguments"
    src_gallery_path = args.src or "photo"
    dst_gallery_path = args.dst or "gallery"
    if args.port is not None:
        serverPort = int(args.port)
    else:
        serverPort = 8012
    """TODO create menu architecture """
    gallery = analyseGalleryStruct(src_gallery_path)
    """TODO prepare photoes """
    """TODO create gallery"""

    if args.server:
        runHttpServer(dst_gallery_path,serverPort)


def main():
    parser = argparse.ArgumentParser(description='Gatom static gallery auto generator.')
    parser.add_argument('--src', help='Source directory for the gallery')
    parser.add_argument('--dst', help='Destination where the gallery site will be generated')
    parser.add_argument('--port', help='Web server listening port.Default is 8012')
    parser.add_argument('--server',action='store_true',help='Run web server for generated gallery')
    args = parser.parse_args()
    process(args)

if __name__ == '__main__' :
    main()

