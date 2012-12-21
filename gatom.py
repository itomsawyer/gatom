import argparse
from jinja2 import  PackageLoader , Environment
from PIL import Image
import sys,os
import imghdr
import shutil

sys.path.append(os.path.join(os.path.dirname(__file__),os.path.pardir))

env = Environment(loader = PackageLoader('gatom','templates'))


class album:
    name = 'gallery'
    url = '/gallery'
    cover = ''
    totalPhoto = 0
    totalSubAlbum = 0

class photo:
    name = 'photo'
    url = '/'
    

def runHttpServer(documentRoot,port):
    os.chdir(documentRoot)
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler 
    httpd = SocketServer.TCPServer(("",port),handler)

    print "server on port 8012..."

    httpd.serve_forever()

def prepare_image(src,dst):
    if not os.path.exists(dst) :
        im = Image.open(src)
        im.save(dst)

def generator_html(path,template_name ,args):
    template = env.get_template(template_name)
    template_content = template.render(**args)
    # save static file
    new_file = file(path, 'w')
    new_file.write(template_content)
    new_file.close()


def createAlbums(srcPath,dstPath,urlPath):
    images_list = list()
    albums_list = list()
    album_item = album()


    album_item.name =os.path.basename(dstPath)
    album_item.url = urlPath

    print "Processing Album " + album_item.name + " in " +dstPath + " ..."
    

    for obj in  os.listdir(srcPath):
        src_obj_path = os.path.join(srcPath,obj)
        dst_obj_path = os.path.join(dstPath,obj)
        
        if os.path.isfile(src_obj_path) and ( imghdr.what(src_obj_path) is not None ):
            image = photo()
            album_item.totalPhoto +=1

            prepare_image(src_obj_path,dst_obj_path)

            image.name = obj
            image.url = os.path.join(urlPath ,obj)
            if album_item.cover is '':
                album_item.cover = image.url 

            images_list.append(image)

        if os.path.isdir(src_obj_path):
            if not os.path.exists(dst_obj_path):
                os.mkdir(dst_obj_path)
            album_item.totalSubAlbum += 1
            albums_list.append(createAlbums(src_obj_path,os.path.join(dstPath,obj),os.path.join(urlPath,obj)) )


    """if albums_list or  image_list is not none"""
    generator_html(dstPath + '/index.html','gallery.jinja2', { 
                    'title' : 'Gatom'    ,
                    'images' : images_list,
                    'albums' : albums_list, })

    return album_item


def createStatic(dstPath):
    if not os.path.exists(os.path.join(dstPath,'css')):
        shutil.copytree('css',os.path.join(dstPath,'css'))
    if not os.path.exists(os.path.join(dstPath,'js')):
        shutil.copytree('js',os.path.join(dstPath,'js'))
    if not os.path.exists(os.path.join(dstPath,'fonts')):
        shutil.copytree('fonts',os.path.join(dstPath,'fonts'))
    if not os.path.exists(os.path.join(dstPath,'images')):
        shutil.copytree('images',os.path.join(dstPath,'images'))
            

def buildGallery(srcPath,dstPath):
    if not os.path.exists(dstPath):
        os.mkdir(dstPath)
    urlPath = '/'

    if not os.path.exists(dstPath):
        os.mkdir(dstPath)

    createStatic(dstPath)

    createAlbums(srcPath,dstPath,os.path.join(urlPath))
    

def process(args):
    "Initialize arguments"
    src_gallery_path = args.src or "photo"
    dst_gallery_path = args.dst or "gallery"
    if args.port is not None:
        serverPort = int(args.port)
    else:
        serverPort = 8012
    """TODO create menu architecture """
    gallery = buildGallery(src_gallery_path,dst_gallery_path)
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

