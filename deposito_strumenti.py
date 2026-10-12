import csv
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        """Inizializza gli attributi e le strutture dati"""
        # TODO

    def carica_file_strumenti(self, file_path):
        elenco_strumenti = []
        try:
            file = open(file_path, "r")

            class Strumento:
                def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
                    self.id_strumento = None
                    self.tipo = None
                    self.marca = None
                    self.anno_acquisto = None
                    self.valore = None

                def __str__(self):
                    return f'{self.id_strumento}{self.tipo}{self.marca}{self.anno_acquisto}{self.valore}'
            reader = csv.reader(file)
            for row in reader:
                oggetto = Strumento(id_strumento=row[0], tipo=row[1], marca=row[2], anno_acquisto = row[3], valore = row[4])
                elenco_strumenti.append(oggetto)

            print(elenco_strumenti)
            file.close()
        except FileNotFoundError:
            print(f'File non trovato')

        """Carica gli strumenti dal file"""
        # TODO

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
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
