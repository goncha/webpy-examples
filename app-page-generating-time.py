# -*- coding: utf-8 -*-


##############################
# Reqirement:
#  pip install web.py
##############################


import web


urls = (
    r'/', 'index',
    r'/notime', 'notime'
)

app = web.application(urls, globals())


class index:
    def GET(self):
        web.header('Content-Type', 'text/html')
        return '''
<!DOCTYPE html>
<html lang="en">
<head>
<title>Web.py page generating time</title>
</head>
<body>
<h1>Hello, click page source menu to get page generating time!</h1>
</body>
</html>
'''

class notime:
    def GET(self):
        return '''
<!DOCTYPE html>
<html lang="en">
<head>
<title>Web.py page generating time</title>
</head>
<body>
<h1>Hello, there is no page generating time with wrong content-type!</h1>
</body>
</html>
'''


def is_html():
    headers = [(k, v) for k, v in web.ctx.headers if 'content-type'==k.lower()]
    if headers:
        ctype = headers[0][1]
        return ctype.startswith('text/html') or ctype.startswith('application/xhtml+xml')


import time
def page_generating_time(handler):
    stime = time.time()
    resp = handler()
    stime = time.time() - stime
    if is_html():
        return resp + '\n\r<!-- generating time: %s seconds -->\n\r' % (str(stime),)
    else:
        return resp


app.add_processor(page_generating_time)



if __name__ == '__main__':
    app.run()


# Local Variables: **
# comment-column: 56 **
# indent-tabs-mode: nil **
# python-indent: 4 **
# End: **
