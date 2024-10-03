meme_dict = {
    "ADMIN":"persona que tiene un cargo administrativo",
    "AGGRO":"ponerse agresivo/enojado",
    "AH RE":"significa que uno dijo una tontería, una exageración o algo que no debe ser tomado con seriedad o en sentido literal",
    "BOLUDO":"quiere decir Necio, Tonto o Estúpido",
    "CHETO":"individuo con una gran cantidad de dinero",
    "CREEPY":"aterrador, siniestro",
    "CRINGE":"Algo excepcionalmente raro o embarazoso",
    "D10S":"referido al idolo del futbol mundial. El astro argentino Diego Armando Maradona",
    "GOAT":"se le dice eso al mejor del mundo (en futbol)",
    "HYPE":"se refiere a la emoción o entusiasmo que se experimenta ante un evento",
    "INTEGILENTE":"alguien bueno en pensar estupideces",
    "K.O.":"es cuando un npc es derrotado",
    "LOL":"Una respuesta común a algo gracioso",
    "NASHE":"hace referencia a algo muy bueno o impresionante",
    "ROFL":"una respuesta a una pregunta",
    "SAPO":"alguien que delata a otro individuo (usada mayormente en Argentina)",
    "SHEESH":"ligera desaprobación",
    "SPOILER":"se refiere a la acción de revelar y anticipar una información",
    "UNBOXING":"Se refiere a la experiencia de «desempacar» y abrir un producto",
            }
print ("hola bienvenido al diccionario de vicente") 
for i in range(5):
  word = input("Escribe la palabra #{i+1} que no entiendas (¡con mayúsculas!): ").upper()
  explanation = meme_dict[word]
  print (explanation)
else:
    input ("la palabra no esta en este diccionario |;")
