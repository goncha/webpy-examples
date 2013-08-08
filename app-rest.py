# -*- coding: utf-8 -*-

#
# Refers http://www.johnpaulett.com/2008/09/20/getting-restful-with-webpy/
#


##############################
# Reqirement:
#  pip install web.py
##############################

import web
import re
import uuid

VALID_KEY = re.compile('[a-zA-Z0-9_-]{1,255}')
def is_valid_key(key):
    return VALID_KEY.match(key)

def validate_key(fn):
    def new(*args):
        if not is_valid_key(args[1]):
            web.badrequest()
        return fn(*args)
    return new

KEYS_TEMPLATE = web.template.Template('''$def with(keys)
<html>
<head><title>Keys in MemoryDB</title></head>
<body>
<b>Keys:</b><br>
$for k in keys:
  <a href="$k">$k</a><br>
</body>
</html>
''', 'keys.html')

class AbstractDB(object):
    def GET(self, name):
        if len(name) <= 0:
            return KEYS_TEMPLATE(keys=self.keys())
        else:
            return self.get_resource(name)

    @validate_key
    def POST(self, name):
        data = web.data()
        name = str(name)
        self.put_key(name, data)
        return name

    @validate_key
    def DELETE(self, name):
        self.delete_key(str(name))

    def PUT(self, name=None):
        name = str(uuid.uuid4())
        self.POST(name)

    @validate_key
    def get_resource(self, name):
        return self.get_key(str(name))

class MemoryDB(AbstractDB):
    database = {}

    def get_key(self, key):
        try:
            return self.database[key]
        except KeyError:
            web.notfound()

    def put_key(self, key, value):
        self.database[key] = value

    def delete_key(self, key):
        try:
            del(self.database[key])
        except KeyError:
            web.notfound()

    def keys(self):
        return self.database.iterkeys()


urls = (
    r'/memory/(.*)', 'MemoryDB'
)
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()


# Local Variables: **
# comment-column: 56 **
# indent-tabs-mode: nil **
# python-indent: 4 **
# End: **
