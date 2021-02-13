import web
import requests
import json

render = web.template.render("zodi/")

class Index():

    def GET(self):
        datos = None
        return render.index(datos)

    def POST(self):
        form = web.input()
        book_name = form["book_name"]
        result =requests.get('https://aplicaciones-web-orientadas-a-servicios.agustinespindol.repl.co/hola')
        books = result.json()
        items = books["items"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded)

        url = decoded[0]["volumeInfo"]["infoLink"]

        datos = {
          "book_name":book_name,
          "url":url
        }

        return render.index(datos)
        