# ruleid: command-injection-os-system
image = request.POST['image']
os.system("./face-recognize %s --N 24" % image)

import json
from json import load, loads

def lambda_handler(event, context):

    tainted = event['exploit_code']
    s = "encoded-data"
    b = bytearray().extend(map(ord,string))

    # ruleid: tainted-json-aws-lambda
    json.load(tainted)
    # # ruleid: tainted-json-aws-lambda
    # json.load(tainted, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)
    # # ruleid: tainted-json-aws-lambda
    # json.loads(tainted)
