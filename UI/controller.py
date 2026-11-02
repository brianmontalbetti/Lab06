import flet as ft
from UI.view import View
from model.model import DepositoStrumenti


class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        nuovo_responsabile = self._view.input_responsabile.value

        if not nuovo_responsabile or nuovo_responsabile.strip() == "":
            self._view.show_alert("Errore: il nome del responsabile non può essere vuoto!")
            return

        self._model.responsabile = nuovo_responsabile
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.input_responsabile.value = ""  # Svuota il campo
        self._view.update()

    def mostra_strumenti(self, e):
        try:
            # Chiama il Model per farsi dare i dati
            strumenti = self._model.get_tutti_strumenti()
            self._view.aggiorna_lista_strumenti(strumenti)
        except Exception as ex:
            self._view.show_alert(f"Errore di connessione al database: {ex}")

    def cerca_strumenti(self, e):
        tipo_cercato = self._view.input_tipo_strumento.value

        if not tipo_cercato or tipo_cercato.strip() == "":
            self._view.show_alert("Attenzione: inserisci un tipo di strumento per cercare!")
            return

        try:
            # Chiama il Model per filtrare i dati
            strumenti_trovati = self._model.cerca_per_tipo(tipo_cercato.strip())
            self._view.aggiorna_lista_ricerca(strumenti_trovati)
        except Exception as ex:
            self._view.show_alert(f"Errore durante la ricerca: {ex}")