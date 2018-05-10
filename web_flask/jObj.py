'''
python convert_obj.py -i infile.obj -o outfile.
@author:jiangshanduo
'''

import fileinput
import operator
import os.path
import getopt
import sys
import struct
import math
import glob

TEMPLATE_FILE_ASCII = u"""\
 v=new Float32Array([%(vertices)s]);
 vn=new Float32Array([%(normals)s]);
 f=new Uint16Array([%(faces)s]);
"""

TEMPLATE_VERTEX = "%.5g,%.5g,%.5g"
TEMPLATE_N = "%.4g,%.4g,%.4g"
TEMPLATE_FACE = "%d,%d,%d"

# Utils


def file_exists(filename):
    try:
        f = open(filename, 'r')
        f.close()
        return True
    except IOError:
        return False


def get_name(fname):
    # Create model name based of filename ("path/fname.js" -> "fname").

    return os.path.splitext(os.path.basename(fname))[0]

# OBJ parser


def parse_obj(fname):
    vertices = []
    normals = []
    faces = []
    for line in fileinput.input(fname):
        chunks = line.split()
        if len(chunks) > 0:
            if chunks[0] == "v":  # and len(chunks) == 4:
                x = float(chunks[1])
                y = float(chunks[2])
                z = float(chunks[3])
                vertices.append([x, y, z])
            if chunks[0] == "vn" and len(chunks) == 4:
                x = float(chunks[1])
                y = float(chunks[2])
                z = float(chunks[3])
                l = math.sqrt(x * x + y * y + z * z)
                if l:
                    x /= l
                    y /= l
                    z /= l
                normals.append([x, y, z])
            if chunks[0] == "f" and len(chunks) >= 4:
                x = int(chunks[1].split("/")[0])
                y = int(chunks[2].split("/")[0])
                z = int(chunks[3].split("/")[0])
                faces.append([x - 1, y - 1, z - 1])
    return faces, vertices, normals

# Generator - chunks


def generate_face(f):
    return TEMPLATE_FACE % (f[0], f[1], f[2])


def generate_vertex(v):
    return TEMPLATE_VERTEX % (v[0], v[1], v[2])


def generate_normal(n):
    return TEMPLATE_N % (n[0], n[1], n[2])


if __name__ == '__main__':
    # get parameters from the command line
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hbi:m:c:b:o:a:s:t:d:x:f:", ["help", "bakecolors", "input=", "morphs=",
                                                                              "colors=", "output=", "align=", "shading=", "type=", "dissolve=", "truncatescale=", "framestep="])

    except getopt.GetoptError:
        sys.exit(2)

    infile = outfile = ""
    for o, a in opts:
        if o in ("-i", "--input"):
            infile = a
        elif o in ("-o", "--output"):
            outfile = a
    if infile == "" or outfile == "":
        sys.exit(2)
    print("Converting [%s] into [%s] ..." % (infile, outfile))

    if not file_exists(infile):
        print("Couldn't find [%s]" % infile)
        sys.exit(2)

# parse OBJ
    faces, vertices, normals = parse_obj(infile)

# generate normals string
    nnormal = 0
    normals_string = ""
    normals_string = ",".join(generate_normal(n) for n in normals)

# generate ascii model string

    text = TEMPLATE_FILE_ASCII % {
        "normals": normals_string,
        "vertices": ",".join(generate_vertex(v) for v in vertices),
        "faces": ",".join(generate_face(f) for f in faces)
    }

    out = open(outfile, "w")
    out.write(text)
    out.close()

