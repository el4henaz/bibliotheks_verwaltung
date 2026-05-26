# Bibliotheksverwaltung: Ein OOP-basiertes System zur Verwaltung von Büchern
# Fokus: Objektorientierte Programmierung (OOP) in Python

class Buch:
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn
        self.ist_ausgeliehen = False

    def __str__(self):
        status = "Ausgeliehen" if self.ist_ausgeliehen else "Verfügbar"
        return f"{self.titel} von {self.autor} (ISBN: {self.isbn}) - Status: {status}"


class Bibliothek:
    def __init__(self):
        self.buecher_liste = []

    def buch_hinzufuegen(self, buch):
        self.buecher_liste.append(buch)
        print(f"Erfolg: Das Buch '{buch.titel}' wurde hinzugefügt.")

    def alle_buecher_anzeigen(self):
        if not self.buecher_liste:
            print("\nDie Bibliothek hat aktuell keine Bücher.")
            return
        print("\n--- BÜCHER IN DER BIBLIOTHEK ---")
        for buch in self.buecher_liste:
            print(buch)

    def buch_ausleihen(self, titel):
        for buch in self.buecher_liste:
            if buch.titel.lower() == titel.lower():
                if not buch.ist_ausgeliehen:
                    buch.ist_ausgeliehen = True
                    print(f"Erfolg: Sie haben das Buch '{buch.titel}' ausgeliehen.")
                    return
                else:
                    print("Hinweis: Dieses Buch ist bereits ausgeliehen.")
                    return
        print("Fehler: Das Buch wurde nicht gefunden.")


def hauptprogramm():
    meine_bibliothek = Bibliothek()
    
    # Einige Standardbücher direkt zu Beginn hinzufügen
    meine_bibliothek.buch_hinzufuegen(Buch("Python Clean Code", "Carola Kuschel", "111222"))
    meine_bibliothek.buch_hinzufuegen(Buch("Einführung in SQL", "Markus Neuer", "333444"))

    while True:
        print("\n--- BIBLIOTHEKS-VERWALTUNG ---")
        print("1. Neues Buch hinzufügen")
        print("2. Alle Bücher anzeigen")
        print("3. Ein Buch ausleihen")
        print("4. Programm beenden")
        
        auswahl = input("Bitte wählen Sie eine Option (1-4): ")
        
        if auswahl == "1":
            titel = input("Buchtitel: ")
            autor = input("Autor: ")
            isbn = input("ISBN-Nummer: ")
            neues_buch = Buch(titel, autor, isbn)
            meine_bibliothek.buch_hinzufuegen(neues_buch)
            
        elif auswahl == "2":
            meine_bibliothek.alle_buecher_anzeigen()
            
        elif auswahl == "3":
            suchtitel = input("Welches Buch möchten Sie ausleihen? ")
            meine_bibliothek.buch_ausleihen(suchtitel)
            
        elif auswahl == "4":
            print("Programm beendet. Auf Wiedersehen!")
            break
        else:
            print("Fehler: Ungültige Eingabe.")

if __name__ == "__main__":
    hauptprogramm()