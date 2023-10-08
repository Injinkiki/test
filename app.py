import http.server
import socketserver
import subprocess

# 웹 서버를 시작할 포트 번호 설정 (예: 8080)
port = 8080

# 현재 디렉토리를 웹 서버의 경로로 설정
handler = http.server.SimpleHTTPRequestHandler

# 웹 서버 시작
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
