import sys
import re
import zipfile
import io

for epub in sys.argv[1:]:
    with zipfile.ZipFile(epub) as zfile:
        htmls = [n for n in zfile.namelist() if n.lower().endswith('.html')]
        for html in htmls:
            with zfile.open(html) as readfile:
                for line in io.TextIOWrapper(readfile, 'utf-8'):
                    for block in re.findall(ur'[\u0900-\u097F]+', line):
                        backup = block
                        m = re.match(ur'[\u0904-\u0914][\u0900-\u0903]?|[\u0915-\u0939\u0958-\u095F](\u094D[\u0915-\u0939\u0958-\u095F])*[\u093A-\u094C]?[\u0900-\u0903]?|\u0964', block)
                        while m:
                            print m.group(0).encode('utf-8'),
                            block = block[len(m.group(0)):]
                            m = re.match(ur'[\u0904-\u0914][\u0900-\u0903]?|[\u0915-\u0939\u0958-\u095F](\u094D[\u0915-\u0939\u0958-\u095F])*[\u093A-\u094C]?[\u0900-\u0903]?|\u0964', block)
                        if len(block):    
                            print block.encode('utf-8') + '[',
                            for c in block:
                                print hex(ord(c)),
                            print ']'
