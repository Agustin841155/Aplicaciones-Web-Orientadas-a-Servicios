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
        result = requests.get('https://www.googleapis.com/books/v1/volumes?q='+book)
        
        books = result.json()
        print(type(books))

        items = books["items"]

        coded = json.dumps(items)
        decoded = json.loads(coded)

        print(decoded[0]["volumeInfo"]["infoLink"])
        print(decoded[0]["volumeInfo"]["authors"])
        print(decoded[0]["volumeInfo"]["title"])
        print(decoded[0]["volumeInfo"] ["imageLinks"]["thumbnail"])
        
        url = decoded[0]["volumeInfo"]["infoLink"]
        autor = decoded[0]["volumeInfo"]["authors"]
        titu = decoded[0]["volumeInfo"]["title"]
        imagen = decoded[0]["volumeInfo"] ["imageLinks"]["thumbnail"]
        
        a = " ".join(autor)
        t = " ".join(titu)

        titulo = "<a> Titulo: "+t+" </a>"
        autor = "<a> Autor: "+a+" </a>"
        imagen = "<a target='blank' href='"+imagen+"'>Imagen de portada ¡has clik aqui!: "+book+"</a>"
        link = "<a target='blank' href='"+url+"'>Link de compra del libro: "+book+"</br> "+autor +" </br>" +titulo+"</br>"+imagen+"</a>"

        return  link
        
        