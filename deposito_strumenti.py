import csv

class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f'{self.id_strumento}{self.tipo}{self.marca}{self.anno_acquisto}{self.valore}'

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.elenco_strumenti = []
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
        for i in range(len(self.elenco_strumenti)):
            print({self.elenco_strumenti[i].id_strumento}, {self.elenco_strumenti[i].tipo},
                  {self.elenco_strumenti[i].marca}, {self.elenco_strumenti[i].anno_acquisto},
                  {self.elenco_strumenti[i].valore})
        return oggetto
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
