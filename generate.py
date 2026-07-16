import json
import random

def generiere_chaos(anzahl, dateiname):
    subjekte = ["Das Digitalministerium", "Die Wärmepumpen-Verordnung", "Der Glasfaserausbau", 
                "Die Regierungs-App", "Das Bürgeramt", "Die Autobahn-Sanierung", 
                "Der Klimarat", "Die Steuererklärung", "Die Bahn-Pünktlichkeit"]
    
    # Kategorien werden jetzt zufällig zugewiesen, um das Chaos perfekt zu machen
    kategorien = ["Digitalisierung", "Regierung", "Infrastruktur", "Grüne Ideologie", "Klimawandel (nicht existent)"]

    aktionen = ["scheitert kläglich an:", "wurde verschoben wegen:", "verbraucht das Budget von:", 
                "wird als Erfolg gefeiert trotz:", "ist der Beweis für:", "wurde beerdigt wegen:"]
    
    details = ["völliger Inkompetenz", "eines Faxanschlusses", "einer 50-seitigen DIN-Norm", 
               "komplettem Datenverlust", "der deutschen Bürokratie", " weil das immer Montags so ist...",
               "einer Blockade", "digitaler Steinzeit-Technik"]

    chaos_eintraege = []
    
    for _ in range(anzahl):
        # Zufällige Auswahl ohne inhaltliche Logik
        text = f"{random.choice(subjekte)} {random.choice(aktionen)} {random.choice(details)}."
        
        chaos_eintrag = {
            "text": text,
            "kategorie": random.choice(kategorien) # Komplett zufällig
        }
        chaos_eintraege.append(chaos_eintrag)

    with open(dateiname, 'w', encoding='utf-8') as f:
        json.dump(chaos_eintraege, f, ensure_ascii=False, indent=2)
    
    print(f"Chaos-Daten erfolgreich generiert: {anzahl} Einträge in '{dateiname}'.")

if __name__ == "__main__":
    # Generiert 5000 Einträge vollkommenes Chaos
    generiere_chaos(5000, "aerger.json")