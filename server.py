from http.server import BaseHTTPRequestHandler,HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

 def do_GET(self):
  print(self.path)
  
  p=self.path[1:]
  print(p)
  if self.path=="/task1.html":
   self.send_response(200)
   self.send_header("Content-type","text/html")
   self.end_headers()
   self.wfile.write(open('task1.html').read().encode())
  elif self.path=="/favicon.ico":
   print("huyu")
  elif self.path=="/three.js":
   self.send_response(200)
   self.send_header("Content-type","text/javascript")
   self.end_headers()

   self.wfile.write(open("three.js").read().encode())
  else:
   
   self.send_response(200)
   self.send_header("Content-type","text/javascript")
   self.end_headers()

   self.wfile.write(open(p).read().encode())
   
   
 def do_POST(self):
   print(self.path)
   print(self.headers)
   ctype, pdict = parse_header(self.headers['content-type'])
   pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
   if ctype == 'multipart/form-data':
     print(pdict)
     fields = parse_multipart(self.rfile, pdict)
      
     open('f6.png','wb').write(fields['file'][0])
     face_cascade = cv2.CascadeClassifier("/root/opencv-3.4.3/data/haarcascades/haarcascade_frontalface_default.xml")

     img = cv2.imread("/root/ceg/f6.png")
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces=face_cascade.detectMultiScale(gray)

     self.send_response(200)
     self.send_header("Content-type","text/html")
     self.end_headers()
     print(faces) 

     self.wfile.write(str.encode('{"x1":'+str(faces[0][0])+',"y1":'+str(faces[0][1])+',"x2":'+str(faces[0][2])+',"y2":'+str(faces[0][3])+'}'))
     

httpd=HTTPServer(('localhost',8000),RequestHandler)

httpd.serve_forever()
  
