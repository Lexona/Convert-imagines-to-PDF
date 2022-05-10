import qrcode
from PIL import Image
import random
import datetime

risposta = 'si'

while risposta == 'si': 

    #Genero 2 numeri casuali da 4 cifre 
    x = random.randint(1000, 9999)
    y = random.randint(1000, 9999)

    #Serve per contare i 5 qrcode da generare
    contatore = 0

    #Faccio inserire l'email della persona a cui serve la prenotazione
    email = input('Inserisci la prima parte della tua email istituzionale: ')

    #Faccio inserire la data
    data = input('Inserisci il primo mese-giorno della settimana: ')
    data = data.split("-")
    test_date = datetime.datetime(2022, int(data[0]), int(data[1]))

    K = 5
    giorni = []

    res = [test_date + datetime.timedelta(days = idx) for idx in range (K)]

    for date in res: 
        periodo = str(date)
        divisione = periodo.split("-")
        giorni.append(divisione[2].split(" "))

    img = []

    while contatore < 5:

        for date in giorni:
            #Genero il qrcode con le informazioni inserite 
            img.append(qrcode.make(f'{x}|{y}|2022-0{data[0]}-{date[0]}|UNINA\{email}'))

        img[contatore].save(f"{email}-{contatore}.png")

        image = Image.open(f"{email}-{contatore}.png")

        image = image.resize((350, 350))
        image.save(f"{email}-{contatore}.png")

        contatore += 1
    
    risposta = input('Vuoi creare altri QrCodes? ')






