# -*- coding: utf-8 -*-

##############################
# Reqirement:
#  pip install web.py
#  pip install python-openid
##############################


import web
import web.webopenid


urls = (
    r'/openid', 'web.webopenid.host',
    r'/', 'index'
)

app = web.application(urls, globals())


class index:
    def GET(self):
        return '''
<!DOCTYPE html>
<html lang="en">
<head>
<title>Web.py OpenID</title>
</head>
<body>
%s
</body>
</html>
''' % (web.webopenid.form('/openid'),)

if __name__ == '__main__':
    app.run()



# Local Variables: **
# comment-column: 56 **
# indent-tabs-mode: nil **
# python-indent: 4 **
# End: **
