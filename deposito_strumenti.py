import csv
from operator import attrgetter


class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f'{self.id_strumento} {self.tipo} {self.marca} {self.anno_acquisto} {self.valore}'

class Prestito:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento= id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f'{self.id_prestito} {self.data} {self.cognome_allievo} {self.id_strumento} {self.cognome_allievo}'


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.elenco_strumenti = []
        self.lista_prestiti = []
        """Inizializza gli attributi e le strutture dati"""
        # TODO



    def carica_file_strumenti(self, file_path):
        try:
            file = open(file_path, "r")
            self.elenco_strumenti = []
            reader = csv.reader(file)
            for row in reader:
                oggetto = Strumento(id_strumento=row[0], tipo=row[1], marca=row[2], anno_acquisto = row[3], valore = row[4])
                self.elenco_strumenti.append(oggetto)

            '''for i in range(len(self.elenco_strumenti)):
                print({self.elenco_strumenti[i].id_strumento},{self.elenco_strumenti[i].tipo},{self.elenco_strumenti[i].marca},{self.elenco_strumenti[i].anno_acquisto},{self.elenco_strumenti[i].valore})
                CICLO DI PROVA PER STAMPARE ELENCP STRUMENTI
            '''
            file.close()
        except Exception as e:
            print(e)

    """Carica gli strumenti dal file"""
    # TODO

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        prova = self.elenco_strumenti[len(self.elenco_strumenti) - 1].id_strumento
        scatola = int(prova[1:])
        oggetto = Strumento(id_strumento=f'S{scatola + 1}', tipo=tipo, marca=marca, anno_acquisto=anno_acquisto,
                            valore=valore)
        self.elenco_strumenti.append(oggetto)

        return oggetto
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        elenco_ordinato = sorted(self.elenco_strumenti, key=attrgetter('marca'))

        return elenco_ordinato
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):

        if any(id_strumento == s.id_strumento for s in self.elenco_strumenti) and id_strumento not in [s.id_strumento for s in self.lista_prestiti] :
            if len(self.lista_prestiti) == 0 :
                prestito = Prestito( id_prestito = f'P{1}', data = data, id_strumento = id_strumento , cognome_allievo = cognome_allievo )
                self.lista_prestiti.append(prestito)
            else:
                stringa = self.lista_prestiti[len(self.lista_prestiti) - 1].id_prestito
                scatola = int(stringa[1:])
                prestito = Prestito( id_prestito= f'P{scatola + 1}', data = data,id_strumento= id_strumento , cognome_allievo = cognome_allievo )
                self.lista_prestiti.append(prestito)

            '''for i in range (len(self.lista_prestiti)):
                print(self.lista_prestiti[i].id_prestito, self.lista_prestiti[i].data,
                      self.lista_prestiti[i].id_strumento, self.lista_prestiti[i].cognome_allievo)
            '''

            return prestito
        else:
            raise Exception ('strumento non presente nel sistem o gia in prestito')






        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        if any(id_prestito == s.id_prestito for s in self.lista_prestiti):
            for i in self.lista_prestiti:
                if i.id_prestito == id_prestito:
                    try:
                        self.lista_prestiti.remove(i)
                    except Exception as e:
                        print(e)
        else: raise Exception( 'Prestito non presente' )


        """Termina un prestito in atto"""
        # TODO