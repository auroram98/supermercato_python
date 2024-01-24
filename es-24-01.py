import random



# Scrivere un programma che chieda all'utente di inserire i dati dei dipendenti di un supermercato.
# Ciascun dipendente è caratterizzato da un nome, un cognome, una data di nascita e un mestiere.
# ASSEGNARE A CIASCUN DIPENDENTE UN IDENTIFICATIVO UNIVOCO
# - prendere le prime due lettere del nome, le ultime due lettere del cognome e 3 numeri casuali
# compresi tra 1 e 9. Es. Mario Rossi -> id univoco MASI356
# Chiedere all'utente di inserire i dati relativi ad un determinato dipendente e memorizzarli
# all'interno di un dizionario.
# (A)ggiungi: aggiunta di un dipendente
# (S)tampa
# (R)icerca dei dipendenti con un certo nome (consideriamo anche le omonimie)

database_dipendenti= []
while True:
    scelta = input("Quale operazione vuoi eseguire? (A)Aggiungi/(S)Stampa/(R)Ricerca/(Q)Quit: ").upper()
    if scelta == "A":
        #richiesta dati utente
        nome= input("Inserire nome: ")
        cognome= input("Inserire cognome: ")
        data_nascita= int(input("Inserire la data di nascita: "))
        mestiere= input("Inserire il mestiere: ")
        #generare ID
        id = nome[:2]+cognome[len(cognome)-2:]+ str(random.randint(100,999))
        #creare dipendente come un dizionario
        dipendente = {"identificativo": id, "nome": nome, "cognome": cognome, "data": data_nascita, "mestiere": mestiere}
        #aggiungerlo ad un database
        database_dipendenti.append(dipendente)
    elif scelta == "S":
        
        pass
    elif scelta == "R":
        pass
    elif scelta == "Q":
        break
    else:
        print("SCELTA NON VALIDA")



