gatom
========

A simple static gallery website auto generator 

python 2.6 is required .

Manual:

    python gatom.py
    python gatom.py --src SRC  [--dst DST] [--port PORT] [--server]

    required arguments:

    --src SRC    Source directory for the gallery

    optional arguments:

    -h, --help   show this help message and exit
    --dst DST    Destination where the gallery site will be generated
    --port PORT  Web server listening port. Default value  is 8012
    --server     Whether or not to run web server for newly generated gallery 


