import web
import json
import random

urls = (
    '/horoscopo/(.*)', 'Zodiaco',
)
app = web.application(urls, globals())

class Zodiaco():
  
  def GET(self,fechanac):
    try:
      dia=int(fechanac[0:2])
      mes=int(fechanac[3:5])
      ran = random.randint(0,15) 
      tips = ["Evita el aislamiento",
      "Duerme bien y come bien",
      "Haz ejercicio",
      "Exponte a la risa",
      "Cambia de habitos",
      "Ayuda a los demas y haz el bien",
      "Hechale ganas",
      "Lo lograras",
      "No te rindas",
      "Lucha por tus suenos",
      "Ayuda a quien mas lo necesita sin mirar a quien",
      "Comparte tu felicidad",
      "Ignora los malos comentarios",
      "Alimentate sanamente",
      "Aprecia el tiempo que pasas con tus seres queridos",
      "Mantente informado de tu signo zodiacal"
      ]
      if dia >= 21 and mes == 3 or mes == 4 and dia <= 20:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Aries"
        zodiaco["color"]= "Rojo"
        zodiaco["elemento"]= "Fuego"
        zodiaco["numero_suerte"]= "son el 7, el 17 y el 21"
        zodiaco["horoscopo"]= "Te espera un dia bastante tranquilo, Aries, excepto en algun momento que se te puede plantear una situacion dificil Tal vez discutas con alguien a quien quieres mucho y puede no ser necesariamente tu pareja, Es normal que haya peleas cuando existe mucha confianza o cuando se convive muchas horas a diario, Es solo un bache pasajero, una nube de verano, Toma tu la iniciativa de disculparte y otro dia intenta ponerte en su lugar antes de lanzarte a discutir, En el amor las cosas parece que se te escapan de las manos, decepcionada Aries, pero quiza es solo que tu miedo al compromiso te hace perder a las personas con las que podrias haber tenido una relacion feliz. Es muy importante que hoy empieces a ver el amor como algo maravilloso, que nos cambia la vida a diario y que precisa entrega"
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      
      elif  dia >= 21 and mes == 4 or mes == 5 and dia <= 20:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Tauro"
        zodiaco["color"]= "Verde"
        zodiaco["elemento"]= "Tierra"
        zodiaco["numero_suerte"]= "son el 4, 6 y 11"
        zodiaco["horoscopo"]= "Tu mente se expande y te llega un soplo de tranquilidad, Vuelves a sentir ganas de divertirte y de pasar un rato agradable, Quiza sea un plan casero, sin ninguna cosa especial, pero tambien puede ser muy atractivo si lo sabes organizar bien, Lo conseguiras con facilidad y los que lo compartan contigo, disfrutaran."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 21 and mes == 5 or mes == 6 and dia <= 21:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Geminis"
        zodiaco["color"]= "Amarillo"
        zodiaco["elemento"]= "Aire"
        zodiaco["numero_suerte"]= "son el 3, el 12 y el 18"
        zodiaco["horoscopo"]= "Nunca esta de mas perdonar y perdonarse. No te vas a preocupar demasiado si alguien te da una negativa en un tema economico porque ya tienes en mente otro plan que puede solucionar mucho mejor eso en lo que estas trabajando. Tu energia hoy estara bastante bien potenciada y estable. ... Andar te despejara mente y cuerpo."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 21 and mes == 6 or mes == 7 and dia <= 22:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Cancer"
        zodiaco["color"]= "Blanco, plateado y verde"
        zodiaco["elemento"]= "Agua"
        zodiaco["numero_suerte"]= "son el 2, el 8 y el 12"
        zodiaco["horoscopo"]= "Hoy se abre una esperanza en una preocupacion relacionada con la salud. Si es de algun familiar, ves que todo contribuye a que mejore. Debes estar cerca de el o de ella si puedes para insuflar animos y carino. Seran la mejor medicina en este momento."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 23 and mes == 7 or mes == 8 and dia <= 22:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Leo"
        zodiaco["color"]= "Oro, naranja, dorado, ocasionalmente el amarillo"
        zodiaco["elemento"]= "Fuego"
        zodiaco["numero_suerte"]= "son el 1, el 9 y el 10"
        zodiaco["horoscopo"]= "No te alteres en absoluto, explosiva Leo, si tus jefes no estan cumpliendo a diario con lo que te habian dicho. Son ellos quienes faltan a su palabra y no deberias sentirte mal por ello. Procura hoy recuperar la serenidad y el buen talante porque quiza tengas que batallar para que respeten los acuerdos que concretaste con ellos al principio. Tendras mas exito con mucha mano izquierda y buenas palabras, que con exigencias. Incluso puedes sumar puntos y hacer que te valoren mas. Es muy importante que te propongas estar cada dia mejor y, sobre todo, que no te hagan mella las cosas que a diario no puedes evitar. En el terreno sentimental hoy puedes descubrir algo que no sabias de tu pareja y no necesariamente negativo, nativa de Leo. Puede tratarse de una faceta que desconocias pero que te va a entusiasmar."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 23 and mes == 8 or mes == 9 and dia <= 22:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Virgo"
        zodiaco["color"]= "Marron"
        zodiaco["elemento"]= "Tierra"
        zodiaco["numero_suerte"]= "son el 10, el 15 y el 27"
        zodiaco["horoscopo"]= "No andes pensando a diario que las cosas siempre te salen mal, Virgo. Llevas una temporadita trabajando a tope y de hecho ya han empezado a aparecer los buenos resultados, pero quiza no sabes apreciarlo bastante. Si te dieras cuenta hoy de lo que realmente has conseguido, serias mas feliz. No dejes pasar el exito sin disfrutarlo. Ahora te han entrado muchas ganas de explorar mas el mundo que te rodea y estas pensando en tomar una decision que puede cambiar tu vida de arriba abajo a diario. Esto esta muy bien, pero no seas impulsivo, nativa de Virgo, antes de actuar, has de reflexionar. Y si entre estas decisiones involucras al tema sentimental, piensalo muy bien con mayor motivo. A veces lo nuevo solo es fantastico al principio. Recuerdalo hoy si estas tentada de dar un paso en este sentido en el amor."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 23 and mes == 9 or mes == 10 and dia <= 22:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Libra"
        zodiaco["color"]= "Rosa"
        zodiaco["elemento"]= "Aire"
        zodiaco["numero_suerte"]= "son el 2, el 8 y el 19"
        zodiaco["horoscopo"]= "Te sientes desanimado, luchador Libra, porque haces demasiado caso a diario a personas que te echan por los suelos todo aquello que deseas. Logran quitarte la ilusion haciendote creer que eso a lo que tu aspiras es dificil o incluso imposible. Hoy es un buen momento para librarte de estos lastres y salir adelante con tus ideas y tus suenos. Barre de tu vida a la gente que no te deja crecer personalmente, talentosa Libra. Seguro que no los vas a echar de menos. Una de estas personas incluso puede estar influyendo negativamente en tu felicidad a diario, parece que a veces incluso se atreve a decidir por ti y esto te perjudica. Podria tratarse de alguien con quien has empezado a salir hace poco, planteate hoy muy en serio si seguir con esta relacion. Parece excesivamente autoritario."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 23 and mes == 10 or mes == 11 and dia <= 22:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Escorpion"
        zodiaco["color"]= "Rojo"
        zodiaco["elemento"]= "Agua"
        zodiaco["numero_suerte"]= "son el 4, el 13 y el 21"
        zodiaco["horoscopo"]= "Si hoy se te pasa por la cabeza que has de replantearte tu futuro, Escorpio, adelante con la idea porque siempre sera para mejorar a diario, pero ten en cuenta que este tipo de decisiones no se pueden tomar en un pis pas, necesitan tiempo para madurarlas. Quiza estes impaciente y quieras hacerlo ya. En este caso has de medir muy bien los pros y los contras de cualquier cosa que quieras cambiar en tu vida. Cuando estes convencida, lanzate Y presta atencion a todas las cosas importantes de tu existencia, afortunada Escorpio, no te centres solo en el trabajo o en el amor, contempla tambien los otros aspectos que son primordiales a diario como la salud o la familia.. Si estas dejando un poco de lado a tu pareja, recuerda hoy lo que significa en tu vida, seguro que tiene mucho valor."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 23 and mes == 11 or mes == 12 and dia <= 21:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Sagitario"
        zodiaco["color"]= "Rojo"
        zodiaco["elemento"]= "Agua"
        zodiaco["numero_suerte"]= "son el 4, el 13 y el 21"
        zodiaco["horoscopo"]= "Si hoy se te pasa por la cabeza que has de replantearte tu futuro, Escorpio, adelante con la idea porque siempre sera para mejorar a diario, pero ten en cuenta que este tipo de decisiones no se pueden tomar en un pis pas, necesitan tiempo para madurarlas. Quiza estes impaciente y quieras hacerlo ya. En este caso has de medir muy bien los pros y los contras de cualquier cosa que quieras cambiar en tu vida. Cuando estes convencida, lanzate Y presta atencion a todas las cosas importantes de tu existencia, afortunada Escorpio, no te centres solo en el trabajo o en el amor, contempla tambien los otros aspectos que son primordiales a diario como la salud o la familia.. Si estas dejando un poco de lado a tu pareja, recuerda hoy lo que significa en tu vida, seguro que tiene mucho valor."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 22 and mes == 12 or mes == 1 and dia <= 20:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Capricornio"
        zodiaco["color"]= "Gris"
        zodiaco["elemento"]= "Tierra"
        zodiaco["numero_suerte"]= "son el 3, el 16 y el 25"
        zodiaco["horoscopo"]= "Hoy, Capricornio, vuelves a sentir esa rebeldia que te lleva a discutir por tus convicciones. Te ha dado buenos resultados a diario y es que, de hecho, esta muy bien no ser conformista ni comulgar con ruedas de molino, solo porque lo hace la mayoria. Te ira bien ahora que estas pendiente de tomar algunas decisiones y puede que te esten intentando influenciar. Intenta hablar con alguien que tenga mas experiencia y criterio. En especial en los temas relacionados con el aspecto amoroso mantente firme en tus convicciones, exigente Capricornio, y no dejes que otras personas intenten desanimarte o influir a diario en lo que tu quieres o piensas hacer. Guiate hoy por tu intuicion. No te fallara. Y recuerda que en el amor todo es posible, incluso cuando parece que las cosas se han torcido demasiado."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 21 and mes == 1 or mes == 2 and dia <= 18:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Acuario"
        zodiaco["color"]= "Azul"
        zodiaco["elemento"]= "Aire"
        zodiaco["numero_suerte"]= "Son el 7, 14 y 20"
        zodiaco["horoscopo"]= "Hoy corres riesgo de tener algun fallo en el trabajo, Acuario, y si esto sucediera tendrias que volver a empezar. Pon mucha atencion a lo que tienes entre manos, concentrate. En cambio para el amor, sera un buen dia, siempre y cuando te atrevas a demostrar abiertamente los sentimientos. Estas en un buen momento para hacer alguna locura con tu pareja, piensalo para sorprenderle manana. Puedes contratar un crucero para mas adelante o regalarle una aventura como tirarse en parapente. Tambien valen planes mas tranquilos si el no es tan aventurero. Si tienes un sueno, nativa de Acuario, intenta realizarlo ahora o en el futuro proximo. Pondras chispa en la relacion. Sobre todo, busca a diario el romanticismo y la pasion, dedicale tiempo a diario a tu chico o chica. Lo sabra valorar. Empieza hoy mismo a poner en marcha esa forma de actuar."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
      elif  dia >= 19 and mes == 2 or mes == 3 and dia <= 20:
        zodiaco = {}
        zodiaco["nombre_del_signo"]= "Piscis"
        zodiaco["color"]= "Azul"
        zodiaco["elemento"]= "Aire"
        zodiaco["numero_suerte"]= "son el 19, 2, 5, 9, y 1"
        zodiaco["horoscopo"]= "Estas utilizando a diario una tactica equivocada con los trabajos que se te hacen cuesta arriba, agobiada Piscis. Seguramente los vas dejando para luego y ese luego no llega nunca. Hoy has de hacer un esfuerzo para salir de esta etapa que te esta perjudicando. Empieza por la manana con lo complicado, tendras mas energia para sacartelo de encima y te quedaras muy aliviado. Lo que no puede ser es esperar que los otros hagan tu parte de lo que sea. Has de aprender a volar solo a diario y resolver por ti mismo tus problemas. Cuando veas que puedes te sentiras mejor que nunca. Si hoy tu pareja te dice algo que te molesta, susceptible Piscis, analizalo. Es una critica constructiva. En lugar de enfadarte, reflexiona. Y no te hagas el ofendido o estropearas el día que se avecina manana."
        zodiaco["tip_del_dia"] = tips[ran]
        resultado = json.dumps(zodiaco)
        return resultado
    except:
      catch = {}
      catch ["trata:"] = "ingresa primero el dia de tu nacimiento luego el mes y por ultimo el ano ejemplo 08/09/01" 
      resultado = json.dumps(catch)
      return resultado

if __name__ == "__main__":
    app.run()