import pgzrun
from pgzhelper import *
import os
import random
from random import randrange
pygame.display.set_caption("HERMES")
WIDTH = 774
HEIGHT = 774

sonido=True
listanum = list(range(27))
fondo = Actor('fondo1', (387, 387))
botonaprender = Actor('botonaprender', (387, 290))
botonaQUIZZ = Actor('botonquizz', (387, 440))
botontraductor= Actor('botontraductor', (387, 590))
botonregresar = Actor('regresar', (-100, -100))
bx = Actor('x', (-100, -100))
by = Actor('y', (-100, -100))
bz = Actor('z', (-100, -100))
lolp = Actor('boton', (-100, -100))
BtRegresarAbc= Actor('regresarabc', (-100,-100))
puntos= Actor('puntos', (-100,-100))
sonidoIm=Actor('sonido',(700,70))
sonidoNOIm=Actor('sonidono',(-100,-100))

botonTraductor= Actor("botontraducir", (-100, -100))
aaa= Actor('regresartraductor', (-100, -100))

Cangrejo =Actor('pesv2')
Cangrejo.images = ['pesv2','pesv3','pesv4','pesv5','pesv6','pesv7','pesv8', 'pesv9','pesv10','pesv11','pesv12','pesv13']
Cangrejo.fps = 6
confeti=Actor ('pes1')
confeti.images= ['pes1','pes2','pes3','pes4','pes5','pes6']
confeti.fps= 6

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']
listapregun = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

listacorrecto =    ['amano', 'bmano', 'cmano', 'dmano', 'emano', 'fmano', 'gmano', 'hmano', 'imano', 'jmano', 'kmano', 'lmano', 'mmano', 'nmano', 'ñmano', 'omano', 'pmano', 'qmano', 'rmano', 'smano', 'tmano', 'umano', 'vmano', 'wmano', 'xmano', 'ymano', 'zmano']
listaincorrecto1 = ['zmano', 'ymano', 'xmano', 'wmano', 'vmano', 'umano', 'tmano', 'smano', 'rmano', 'qmano', 'pmano', 'omano', 'nmano', 'ñmano', 'mmano', 'lmano', 'kmano', 'jmano', 'imano', 'hmano', 'gmano', 'fmano', 'emano', 'dmano', 'cmano', 'bmano', 'amano']
listaincorrecto2 = ['ñmano', 'omano', 'pmano', 'qmano', 'rmano', 'tmano', 'smano', 'umano', 'vmano', 'wmano', 'xmano', 'ymano', 'zmano', 'amano', 'bmano', 'cmano', 'dmano', 'emano', 'fmano', 'gmano', 'hmano', 'imano', 'jmano', 'kmano', 'lmano', 'mmano', 'nmano']

diccionarioletras = {
    'a': 'amano', 'b': 'bmano', 'c': 'cmano', 'd': 'dmano', 'e': 'emano', 'f': 'fmano',
    'g': 'gmano', 'h': 'hmano', 'i': 'imano', 'j': 'jmano', 'k': 'kmano', 'l': 'lmano',
    'm': 'mmano', 'n': 'nmano', 'o': 'omano', 'p': 'pmano', 'q': 'qmano', 'r': 'rmano',
    's': 'smano', 't': 'tmano', 'u': 'umano', 'v': 'vmano', 'w': 'wmano', 'x': 'xmano',
    'y': 'ymano', 'z': 'zmano', ' ': 'espacio'
}

lmao = []
input_text = ""
keyboard_active = False
yyy=True
xxx= False
vantanaaaa=(900, 900)


pos33=0
contador = 0
pos22 = 0
place1 = (-100,-100)
place2 = (-100,-100)
block = False
botones_abc = []
fotomanoLista = []
correctomLista = []
incorrecto1Lista = []
incorrecto2Lista = []
pess=0

for letra in abc:
    boton = Actor(letra)
    boton.pos = -200, -200
    botones_abc.append(boton)

for fotomano in listapregun:
    fotomano1 = Actor(fotomano)
    fotomano1.pos = -200, -200
    fotomanoLista.append(fotomano1)

for jisus in listacorrecto:
    correctom1 = Actor(jisus)
    correctom1.pos = -200, -200
    correctomLista.append(correctom1)

for incorrecto1 in listaincorrecto1:
    incorrecto11 = Actor(incorrecto1)
    incorrecto11.pos = -200, -200
    incorrecto1Lista.append(incorrecto11)

for incorrecto2 in listaincorrecto2:
    incorrecto22 = Actor(incorrecto2)
    incorrecto22.pos = -200, -200
    incorrecto2Lista.append(incorrecto22)

key_to_image = {
    keys.A: 'afondo', keys.B: 'bfondo', keys.C: 'cfondo', keys.D: 'dfondo', keys.E: 'efondo', keys.F: 'ffondo',
    keys.G: 'gfondo', keys.H: 'hfondo', keys.I: 'ifondo', keys.J: 'jfondo', keys.K: 'kfondo', keys.L: 'lfondo',
    keys.M: 'mfondo', keys.N: 'nfondo', keys.O: 'ofondo', keys.P: 'pfondo', keys.Q: 'qfondo',
    keys.R: 'rfondo', keys.S: 'sfondo', keys.T: 'tfondo', keys.U: 'ufondo', keys.V: 'vfondo', keys.W: 'wfondo',
    keys.X: 'xfondo', keys.Y: 'yfondo', keys.Z: 'zfondo'
}

sounds.quizz.play()

def draw():
    screen.clear()
    fondo.draw()
    Cangrejo.draw()
    confeti.draw()
    botonaprender.draw()
    botonaQUIZZ.draw()
    botontraductor.draw()
    botonregresar.draw()
    BtRegresarAbc.draw()
    lolp.draw()
    bx.draw()
    by.draw()
    bz.draw()
    puntos.draw()
    sonidoIm.draw()
    sonidoNOIm.draw()
    screen.draw.text(str(contador),place1, fontsize=25, fontname="century", color=(0, 0, 0))
    screen.draw.text("pregunta "+ str(pos33), place2, fontsize=30, fontname="century", color=(0, 0, 0))
    for boton in botones_abc:
        boton.draw()
    for fotomano1 in fotomanoLista:
        fotomano1.draw()
    for correctom1 in correctomLista:
        correctom1.draw()
    for incorrecto11 in incorrecto1Lista:
        incorrecto11.draw()
    for incorrecto22 in incorrecto2Lista:
        incorrecto22.draw()
    botonTraductor.draw()
    aaa.draw()
    for boton in lmao:
        boton.draw()
    screen.draw.text(input_text, vantanaaaa, color=(0,0,0), fontsize=40)
    # movimiento_chico()


def update():
    movimiento_chico()
    movimiento_confeti()
    if yyy:
        chicover()
    else:
        chiconover()
    if xxx:
        confetimov()
    else:
        confetieso()

def movimiento_chico():
    Cangrejo.animate()
def chicover():
    Cangrejo.x=387
    Cangrejo.y=387
def chiconover():
    Cangrejo.x=-600
    Cangrejo.y=-684
def movimiento_confeti():
    confeti.animate()
def confetimov():
    confeti.x=387
    confeti.y=387
def confetieso():
    confeti.x=-600
    confeti.y=-684

def show_aprender():
    global pess, block, yyy, xxx
    fondo.image = 'aprender'
    pess=1
    sonidoIm.pos=-100,-100
    sonidoNOIm.pos=-100,-100
    BtRegresarAbc.pos=-100,-100
    botonaprender.pos = -600, 0
    botonaQUIZZ.pos = -600, 0
    botontraductor.pos=-600,0
    yyy=False
    # botontraductor.pos= -600,0
    bx.pos = 287, 600
    by.pos = 387, 600
    bz.pos = 487, 600
    botonregresar.pos = 150, 695
    block = True
    for x, boton in enumerate(botones_abc):
        ye = x // 6
        equiz = x % 6
        boton.pos = 135 + equiz * 100, 200 + ye * 100

def show_quizz():
    global place1, place2, pess, pos33, yyy
    pos33 = pos33 +1
    for p, fotomano1 in enumerate(fotomanoLista):
        fotomano1.pos = -100, 100
    puntos.pos= 400, 695
    place1=(430, 678)
    place2 = (550,40)
    fondo.image = 'preguntaquizz'
    pess=2
    botonregresar.pos=-100,-100
    lolp.pos = -100,-100
    botonaprender.pos = -600, 0
    botonaQUIZZ.pos = -600, 0
    botontraductor.pos=-600,0
    sonidoIm.pos=-100,-100
    sonidoNOIm.pos=-100,-100
    yyy=False x
    # botontraductor.pos = -600,0
    botonregresar.pos = 150, 695
    global pos22, opcionmultii
    pos22 = random.choice(listanum)
    listanum.remove(pos22)
    fotomanoLista[pos22].pos = 600, 170

    opcionmultii = randrange(3)
    if opcionmultii == 0:
        correctomLista[pos22].pos = 203, 440
        incorrecto2Lista[pos22].pos = 590, 440
        incorrecto1Lista[pos22].pos = 395, 440
    elif opcionmultii == 1:
        correctomLista[pos22].pos = 395, 440
        incorrecto2Lista[pos22].pos = 203, 440
        incorrecto1Lista[pos22].pos = 590, 440
    else:
        correctomLista[pos22].pos = 590, 440
        incorrecto2Lista[pos22].pos = 395, 440
        incorrecto1Lista[pos22].pos = 203, 440

def check_answer(pos):
    global contador, place1, place2, xxx
    if correctomLista[pos22].collidepoint(pos):
        update_display('correcto', 100)
        sounds.kahoot.stop()
        sounds.yippee.play()
        sounds.confetti.play()
        xxx= True
        lolp.pos=155, 695
        botonregresar.pos=635,695
        place1=(430, 678)
        place2 = (550,40)
        contador = contador +100

    elif incorrecto2Lista[pos22].collidepoint(pos) or incorrecto1Lista[pos22].collidepoint(pos):
        update_display('incorrecto', 0)
        sounds.kahoot.stop()
        sounds.incorrecto.play()
        lolp.pos=155, 695
        botonregresar.pos=635,695
        place1=(430, 678)
        place2 = (550,40)


def update_display(image, score):
    fotomanoLista[pos22].pos = -100, -100
    correctomLista[pos22].pos = -100, -100
    incorrecto2Lista[pos22].pos = -100, -100
    incorrecto1Lista[pos22].pos = -100, -100
    fondo.image = image

def reset_to_initial_screen():
    sounds.quizz.stop()
    global place1, block, listanum, contador,pos33, place2, pess, yyy, vantanaaaa, xxx
    block = False
    xxx= False
    vantanaaaa=(900, 900)
    pess=0
    fondo.image = 'fondo1'
    listanum = list(range(27))
    contador=0
    pos33=0
    botonTraductor.pos=-100,-100
    puntos.pos= -100,-100
    place1=(-100,-100)
    place2=(-100,-100)
    botonaprender.pos = 387, 290
    botonaQUIZZ.pos = 387, 440
    botontraductor.pos= 387,590
    if sonido:
        sonidoIm.pos=700,70
    if sonido==False:
        sonidoNOIm.pos=700,70
    yyy= True
     
    botonregresar.pos = -100, -100
    lolp.pos = -100, -100
    bx.pos = -100, -100
    by.pos = -100, -100
    bz.pos = -100, -100
    for boton in botones_abc:
        boton.pos = -200, -200
    for fotomano1 in fotomanoLista:
        fotomano1.pos = -200, -200
    for correctom1 in correctomLista:
        correctom1.pos = -200, -200
    for incorrecto11 in incorrecto1Lista:
        incorrecto11.pos = -200, -200
    for incorrecto22 in incorrecto2Lista:
        incorrecto22.pos = -200, -200

def on_mouse_down(pos):
    global keyboard_active, xxx, sonido
    if botonaprender.collidepoint(pos):
        show_aprender()
        # sounds.soamerican.play()
        # sounds.fornite.stop()
        # sounds.lunch.stop()
    elif BtRegresarAbc.collidepoint(pos):
        show_aprender()

    elif botonaQUIZZ.collidepoint(pos):
        show_quizz()
        if sonido:
            sounds.quizz.stop()
            sounds.kahoot.play()
    elif lolp.collidepoint(pos):
        xxx= False
        show_quizz()
        if sonido:
            sounds.kahoot.play()
    elif botonregresar.collidepoint(pos):
        reset_to_initial_screen()
        if sonido:
            sounds.kahoot.stop()
            sounds.quizz.play()
    elif botontraductor.collidepoint(pos):
        keyboard_active=True
        regresoo()
    elif botonTraductor.collidepoint(pos):
        pamntayaTraducida()

    elif aaa.collidepoint(pos):
        keyboard_active= True
        regresoo()
        for boton in lmao:
            boton.pos=-100,-100
    elif sonidoIm.collidepoint(pos):
        if fondo.image=='fondo1':
            sounds.quizz.stop()
        sonidoIm.pos=-100,-100
        sonidoNOIm.pos=700,70
        sonido=False
    elif sonidoNOIm.collidepoint(pos):
        if fondo.image=='fondo1':
            sounds.quizz.play()
        sonidoIm.pos=700,70
        sonidoNOIm.pos=-100,-100
        sonido=True
    else:
        check_answer(pos)
def regresoo():
    global input_text, keyboard_active, vantanaaaa, yyy
    vantanaaaa=(213, 360)
    keyboard_active= True
    botonaprender.pos = -600, 0
    botonaQUIZZ.pos = -600, 0
    botontraductor.pos=-600,0
    sonidoIm.pos=-100,-100
    sonidoNOIm.pos=-100,-100
    yyy=False
    Cangrejo.x=-100
    Cangrejo.y=-100
    botonTraductor.pos=387,500
    fondo.image='fondotraductor'
    input_text = ""
    botonTraductor.pos=387,500
    aaa.pos=-100,-100
    botonregresar.pos = 150, 695
    screen.draw.text(input_text, vantanaaaa, color=(0,0,0), fontsize=40)
    fondo.image='fondotraductor'

def pamntayaTraducida():
    botonregresar.pos = -100,-100
    fondo.image = 'fondotraductorfin'
    global keyboard_active, input_text,lmao, vantanaaaa
    vantanaaaa=(900,900)
    keyboard_active = False
    botonTraductor.pos=-100,-100
    aaa.pos=387,650
    lmao=[]
    for i, char in enumerate(input_text):
        if char in diccionarioletras:
            boton = Actor(diccionarioletras[char])
            row  = i // 5
            col = i % 5
            boton.pos = 150 + col * 120, 150 + row * 120
            lmao.append(boton)

def on_key_down(key):
    global block
    if block:
        if key in key_to_image:
            fondo.image = key_to_image[key]
            botonregresar.pos= -100,-100
            bx.pos = -100, -100
            by.pos = -100, -100
            bz.pos = -100, -100
            for boton in botones_abc:
                boton.pos = -100, -100
            BtRegresarAbc.pos=200,690
    global input_text, keyboard_active
    if keyboard_active:
        if key.name == 'BACKSPACE':
            input_text = input_text[:-1]
        elif key.name == 'RETURN':
            if fondo.image=='fondotraductor':
                pamntayaTraducida()
        elif key.name == 'SPACE':
            input_text += ' '
        elif key.name.isalpha():
            input_text += key.name.lower()
        
os.environ['SDL_VIDEO_CENTERED'] = '1'
pgzrun.go()