import flet as ft
from UI.alert import AlertManager


class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Elementi UI
        self.txt_titolo = None
        self.txt_responsabile = None
        self.input_responsabile = None
        self.lista_strumenti = None
        self.input_tipo_strumento = None
        self.lista_strumenti_ricerca = None
        self.toggle_cambia_tema = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        # --- Inizializzazione Componenti ---
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")
        self.input_tipo_strumento = ft.TextField(label="Tipo (es. Chitarra)")

        # ListView per i risultati con altezza fissa per gestire lo scroll senza occupare tutto lo schermo
        self.lista_strumenti = ft.ListView(expand=False, height=150, spacing=5, padding=10, auto_scroll=False)
        self.lista_strumenti_ricerca = ft.ListView(expand=False, height=150, spacing=5, padding=10, auto_scroll=False)

        # Pulsanti
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.Button("Conferma", on_click=self.controller.conferma_responsabile)
        pulsante_mostra_strumenti = ft.Button("Mostra", on_click=self.controller.mostra_strumenti)
        pulsante_cerca_strumenti = ft.Button("Cerca", on_click=self.controller.cerca_strumenti)

        # --- LAYOUT ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=20,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3
            ft.Text("Strumenti", size=20),
            pulsante_mostra_strumenti,
            self.lista_strumenti,
            ft.Divider(),

            # Sezione 4
            ft.Text("Cerca Strumento per Tipo", size=20),
            ft.Row(spacing=20,
                   controls=[self.input_tipo_strumento, pulsante_cerca_strumenti],
                   alignment=ft.MainAxisAlignment.CENTER),
            self.lista_strumenti_ricerca
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.update()

    # --- Metodi Helper per aggiornare le Liste chiamati dal Controller ---
    def aggiorna_lista_strumenti(self, strumenti):
        self.lista_strumenti.controls.clear()
        if not strumenti:
            self.lista_strumenti.controls.append(ft.Text("Nessuno strumento presente nel deposito."))
        else:
            for s in strumenti:
                self.lista_strumenti.controls.append(ft.Text(str(s)))
        self.update()

    def aggiorna_lista_ricerca(self, strumenti):
        self.lista_strumenti_ricerca.controls.clear()
        if not strumenti:
            self.lista_strumenti_ricerca.controls.append(ft.Text("Nessuno strumento trovato per il tipo inserito."))
        else:
            for s in strumenti:
                self.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))
        self.update()