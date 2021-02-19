import web
import json
urls = (
    '/parametros?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros():
    def _init_(self):
        pass
    def resta(self,actual,fecha):
        return actual - fecha
    def escribir(self,archivo,texto):
        file=open(archivo,'w')
        texto = texto + "\n"
        file.write(texto)
        file.close
        objeto= Parametros()
        objeto.escribir("archivo","hola")

    def GET(self):
        try:
            parametros = web.input() 
            fecha = int(parametros["fecha_nacimiento"])
            actual = 2021
            resultado= self.resta(actual,fecha)
            nombre = parametros.nombre

            data = {}
            data["ano_de_nacimiento"] = fecha
            data["nombre"] = nombre
            data["edad_actual"] = resultado
            data["ano_actual"] = actual

            result = json.dumps(data)
            file=open('archivo.txt','a')
            texto = result + "\n"
            file.write(texto)
            file.close 
            return result
        except:
            data = {}
            data["mensaje"] = "verifica los datos ingresados"
            return json.dumps(data)
if __name__ == "__main__":
    app.run()