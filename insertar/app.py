import web
import json
urls = (
    '/agenda?', 'Agenda'
)
app = web.application(urls, globals())

class Agenda():
  json_file={}
  def GET(self):
      agenda = web.input() 
      action = agenda.action
      if action == "get":
        return self.read()
      elif action == "put":
        nombre = agenda.nombre
        fecha_nacimiento = agenda.fecha_nacimiento
        result={}
        result["resultado"]="registro almacenado"
        show = json.dumps(result)
        return show, self.write(nombre, fecha_nacimiento)
  def read(self):
        with open("datos.json") as file:
            self.json_file = json.load(file)
            return json.dumps(self.json_file)
  def write(self, nombre,fecha_nacimiento):
    try:
      fecha = fecha_nacimiento
      año = int(fecha_nacimiento[6:10])
      actual = 2021
      edad= actual - año
      datos = {
      "nombre" : nombre,
      "fecha_nacimiento" : fecha,
      "edad" : edad
      }
      with open("datos.json") as file:
        self.json_file = json.load(file)
        self.json_file["edades"].append(datos)
        with open("datos.json","w") as file:
          json.dump(self.json_file, file)
          return json.dumps(datos)
    except  Exception as error:
      print("Error {}".format(error.args[0]))              
if __name__ == "__main__":
    app.run()