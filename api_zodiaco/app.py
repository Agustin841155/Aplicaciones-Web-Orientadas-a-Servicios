import web
#import json

urls = (
    '/aries(.*)', 'Aries',
    '/tauro', 'Tauro',
    '/geminis', 'Geminis',
    '/cancer', 'Cancer',
    '/leo', 'Leo',
)
app = web.application(urls, globals())

class Aries():
    def GET(self,zodiaco):
        zo=[]
        zodiaco = {}

        zodiaco["aries"]= "Te espera un día bastante tranquilo, Aries, excepto en algún momento que se te puede plantear una situación difícil, Tal vez discutas con alguien a quien quieres mucho y puede no ser necesariamente tu pareja, Es normal que haya peleas cuando existe mucha confianza o cuando se convive muchas horas a diario, Es sólo un bache pasajero, una nube de verano, Toma tú la iniciativa de disculparte y otro día intenta ponerte en su lugar antes de lanzarte a discutir, En el amor las cosas parece que se te escapan de las manos, decepcionada Aries, pero quizá es sólo que tu miedo al compromiso te hace perder a las personas con las que podrías haber tenido una relación feliz. Es muy importante que hoy empieces a ver el amor como algo maravilloso, que nos cambia la vida a diario y que precisa entrega"
        zodiaco["color"]= "rojo"
        zodiaco["elemento"]= "fuego"
        zodiaco["numero_suerte"]= "son el 7, el 17 y el 21"
        zo.append(zodiaco)
        
        for row in zodiaco:
          print(zodiaco[row])
        return zo
class Tauro():
    def GET(tauro):
        ta=[]
        tauro = {}

        tauro["tauro"]= "Tu mente se expande y te llega un soplo de tranquilidad, Vuelves a sentir ganas de divertirte y de pasar un rato agradable, Quizá sea un plan casero, sin ninguna cosa especial, pero también puede ser muy atractivo si lo sabes organizar bien, Lo conseguirás con facilidad y los que lo compartan contigo, disfrutarán."
        tauro["color"]= "verde"
        tauro["elemento"]= "tierra"
        tauro["numero_suerte"]= "son 4, 6 y 11"
        ta.append(tauro)
        
        for row in tauro:
          print(tauro[row])
        return ta
class Geminis():
    def GET(geminis):
        ge=[]
        geminis = {}

        geminis["geminis"]= "Nunca está de más perdonar y perdonarse. No te vas a preocupar demasiado si alguien te da una negativa en un tema económico porque ya tienes en mente otro plan que puede solucionar mucho mejor eso en lo que estás trabajando. Tu energía hoy estará bastante bien potenciada y estable. ... Andar te despejará mente y cuerpo."
        geminis["color"]= "amarillo"
        geminis["elemento"]= "aire"
        geminis["numero_suerte"]= "son el 3, el 12 y el 18"
        ge.append(geminis)
        
        for row in geminis:
          print(geminis[row])
        return ge
class Cancer():
    def GET(cancer):
        ca=[]
        cancer= {}

        cancer["cancer"]= "Hoy se abre una esperanza en una preocupación relacionada con la salud. Si es de algún familiar, ves que todo contribuye a que mejore. Debes estar cerca de él o de ella si puedes para insuflar ánimos y cariño. Serán la mejor medicina en este momento."
        cancer["color"]= "Blanco, plateado y verde"
        cancer["elemento"]= "agua"
        cancer["numero_suerte"]= "son el 2, el 8 y el 12"
        ca.append(cancer)
        
        for row in cancer:
          print(cancer[row])
        return ca
class Leo():
    def GET(Leo):
        le=[]
        leo= {}

        leo["leo"]= "No te alteres en absoluto, explosiva Leo, si tus jefes no están cumpliendo a diario con lo que te habían dicho. Son ellos quienes faltan a su palabra y no deberías sentirte mal por ello. Procura hoy recuperar la serenidad y el buen talante porque quizá tengas que batallar para que respeten los acuerdos que concretaste con ellos al principio. Tendrás más éxito con mucha mano izquierda y buenas palabras, que con exigencias. Incluso puedes sumar puntos y hacer que te valoren más. Es muy importante que te propongas estar cada día mejor y, sobre todo, que no te hagan mella las cosas que a diario no puedes evitar. En el terreno sentimental hoy puedes descubrir algo que no sabías de tu pareja y no necesariamente negativo, nativa de Leo. Puede tratarse de una faceta que desconocías pero que te va a entusiasmar."
        leo["color"]= "Oro, naranja, dorado, ocasionalmente el amarillo "
        leo["elemento"]= "fuego"
        leo["numero_suerte"]= "son el 1, el 9 y el 10"
        le.append(leo)
        
        for row in leo:
          print(leo[row])
        return le

if __name__ == "__main__":
    app.run()