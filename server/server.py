import http.server
import socketserver

# Эта переменная нужна для обработки запросов клиента к серверу.

handler = http.server.SimpleHTTPRequestHandler

# Тут мы указываем, что сервер мы хотим запустить на порте 1234. 
# Постарайтесь запомнить эти сведения, так как они нам очень пригодятся в дальнейшем, при работе с docker-compose.

with socketserver.TCPServer(("", 7070), handler) as httpd:

    # Благодаря этой команде сервер будет выполняться постоянно, ожидая запросов от клиента.

   httpd.serve_forever()
