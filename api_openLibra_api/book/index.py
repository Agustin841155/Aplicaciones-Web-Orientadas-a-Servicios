import web
import requests
import json

render = web.template.render('book/')

class Index:

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        book = form.book
        result = requests.get('https://www.etnassoft.com/api/v1/get/?id='+book)
        
        books = result.json()
      
        coded = json.dumps(books)
        decoded = json.loads(coded)

        print(decoded[0]["ID"],)
        print(decoded[0]["title"])
        print(decoded[0]["author"])
        
        ide = decoded[0]["ID"]
        titu = decoded[0]["title"]
        auto = decoded[0]["author"]
        con = decoded[0]["content"]
        
        a = " ".join(auto)
        i = " ".join(ide)

        idee = "<a> ID: "+i+" </a>"
        titulo = "<a> Titulo: "+titu+" </a>"
        autor = "<a> Autor: "+a+" </a>"
        contenido = "<a> Pequeña reseña del contenido: "+con+" </a>"

        link = "<a target='blank'> "+idee+"</br> "+autor+" </br>" +titulo+"</br> "+contenido+"</a>"

        return  link