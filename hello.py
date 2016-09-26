# -*- coding: UTF-8 -*-
import codecs
def app(environ, start_response):

    path = environ['PATH_INFO']

    str=path.split('.',1)
    str1=path.split('/',1)
    routes = ["/a.html", "/hello.html"]
    if len(str) == 2:   #判断是否带.后缀
        if str[1] == "html": #判断后缀是否是html
            if path in routes: #判断是否是已有的文件
                status = '200 OK'
                response_headers = [('Content-Type', 'text/html')]
                start_response(status, response_headers)
                #打开文件并读写
                f = codecs.open(str1[1], "r", "utf-8")
                content = f.read()
                f.close() #关闭文件
                return content #返回文件里的内容
            else:  #如果文件不存在，返回 404 Not Found
                status = '404 Not Found'
                response_headers = [('Content-Type', 'text/plain')]
                start_response(status, response_headers)
                return '404 Not Found!'
        else:
            start_response('200 OK', [('Content-Type', 'text/html')])
            str2=str1[1].split('.',1)
            return '<h1>Hello, %s!</h1>' % (str2[0] or 'web')
    else:
        start_response('200 OK', [('Content-Type', 'text/html')])
        return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

