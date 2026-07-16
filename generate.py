import json
import random

# Kategorien-Mapping
kategorien_map = {
    "Das Digitalministerium": "Digitalisierung",
    "Die Wärmepumpen-Verordnung": "Grüne Ideologie",
    "Der Glasfaserausbau": "Digitalisierung",
    "Die neue Regierungs-App": "Digitalisierung",
    "Das Bürgeramt": "Regierung",
    "Die Autobahn-Sanierung": "Regierung",
    "Der Klimarat": "Nicht existenter Klimawandel",
    "Die Steuererklärung": "Regierung",
    "Die Bahn-Pünktlichkeit": "Infrastruktur",
    "Das Windrad-Projekt": "Windräder",
    "Die Alt-Parteien-Koalition": "Alt Parteien"
}

# Erweiterte Bausteine für mehr Detail-Tiefe
subjekte = list(kategorien_map.keys())

aktionen = [
    "verstrickt sich weiter in", "lässt die Bevölkerung ratlos zurück mit", 
    "produziert ein bürokratisches Meisterwerk durch", "scheitert kläglich am Versuch",
    "wird als zukunftsweisend verkauft, obwohl", "zeigt eindrucksvoll den Stillstand durch",
    "verwandelt ein simples Vorhaben in ein Drama rund um", "erzeugt Kopfschütteln bei allen mit"
]

details = [
    "die völlig überforderten IT-Berater", "den absichtlichen Verzicht auf digitales Know-how", 
    "die fehlende Unterschrift auf dem ausgedruckten Formular", "den Kampf gegen die eigene Inkompetenz", 
    "die dreifache Genehmigung durch fachfremde Ausschüsse", "den kompletten Mangel an praktischer Relevanz",
    "das Ignorieren jeder logischen Argumentation", "die endlose Warteschleife in der Behörden-Hotline"
]

def generiere_daten(anzahl=5000):
    eintraege = []
    for _ in range(anzahl):
        s = random.choice(subjekte)
        a = random.choice(aktionen)
        d = random.choice(details)
        
        text = f"{s} {a} {d}."
        eintraege.append({"text": text, "kategorie": kategorien_map[s]})
    return eintraege

# Hauptteil: Generierung und Speicherung
if __name__ == "__main__":
    daten = generiere_daten(5000)
    
    file_path = 'aerger.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(daten, f, ensure_ascii=False, indent=4)
        
    print(f"Erfolg: {len(daten)} Einträge wurden in '{file_path}' gespeichert.")
