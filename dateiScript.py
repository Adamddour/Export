import csv

def read_csv(file_path, selected_fields, filter_columns=None, filter_values=None):
    data = []
    counts = {}  # Dictionary zur Verfolgung der Zählungen für jeden eindeutigen Wert
    total_count = 0  # Zählvariable für die gesamte Anzahl der Zeilen

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Überprüfe, ob mindestens eine ausgewählte Spalte in der CSV-Datei vorhanden ist
        if not all(field in reader.fieldnames for field in selected_fields):
            print("Warnung: Keine der ausgewählten Spalten ist in der CSV-Datei vorhanden.")
            print(f"Tatsächliche Spaltennamen in der CSV-Datei: {reader.fieldnames}")
            print(f"Ausgewählte Spalten: {selected_fields}")

        for row in reader:
            selected_data = {field: row[field] for field in selected_fields if field in row}

            # Zähle jede Zeile, unabhängig von den Filterbedingungen
            total_count += 1

            # Überprüfe, ob Filterbedingungen angegeben sind und die Bedingungen erfüllt sind
            if filter_columns is not None and filter_values is not None:
                filter_match = all(row.get(col) == val for col, val in zip(filter_columns, filter_values))
                if filter_match:
                    data.append(selected_data)
                    counts.setdefault(tuple(filter_values), 0)
                    counts[tuple(filter_values)] += 1
            else:
                data.append(selected_data)

    return data, counts, total_count

file_path = r'M:\_Ordnerumleitung\Desktop\Tasks\ExcelDateiauslesen\export.csv'
selected_fields = ['Lifecylce Status','StableNet Status', 'Daten vollständig','Erreichbar Status + Fehler']  # Ersetze dies durch die tatsächlichen Spaltennamen
filter_columns = ['Lifecylce Status','StableNet Status', 'Daten vollständig','Erreichbar Status + Fehler']


#Filtern
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_erreichbar=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_ping=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingsnmp=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingssh=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingtelnet=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingssh=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmp=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmpssh=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmptelnet=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_ssh=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_telnet=0
count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtGeprueft=0

with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
            
            if row and row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt':
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt += 1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Erreichbar'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_erreichbar+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - PING'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_ping+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - PING SNMP'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingsnmp+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - PING SNMP SSH'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingssh+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - PING SNMP TELNET'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingtelnet+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - PING SSH'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingssh+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - SNMP'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmp+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - SNMP SSH'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmpssh+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - SNMP TELNET'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmptelnet+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - SSH'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_ssh+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht erreichbar - TELNET'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_telnet+=1
            if row and (row['Lifecylce Status'] == 'aktiv' or row['Lifecylce Status']== 'Fremdgerät' or row['Lifecylce Status']=='geplant Rückbau' or row['Lifecylce Status']=='gesperrt') and (row['StableNet Status']=='Nicht angelegt' and row['Daten vollständig']=='ja' and row['Erreichbar Status + Fehler']=='Nicht geprüft'):
                count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtGeprueft+=1




filter_gesamt_angelegt=['aktiv','Angelegt']
filter_gesamt_nicht_angelegt=['aktiv','Nicht angelegt']
filter_values_nicht_angelegt_nein = ['aktiv','Nicht angelegt', 'nein']
filter_values_nicht_angelegt_ja = ['aktiv','Nicht angelegt', 'ja']





result, counts_gesamt_angelegt, total_count = read_csv(file_path, selected_fields, filter_columns, filter_gesamt_angelegt)
result, counts_gesamt_nicht_angelegt, _ = read_csv(file_path, selected_fields, filter_columns, filter_gesamt_nicht_angelegt)
result, counts_nicht_angelegt_nein, _ = read_csv(file_path, selected_fields, filter_columns, filter_values_nicht_angelegt_nein)
result, counts_nicht_angelegt_ja, _ = read_csv(file_path, selected_fields, filter_columns, filter_values_nicht_angelegt_ja)




print(f"Gesamtanzahl der Zeilen: \t \t \t \t \t \t \t \t \t \t \t{total_count}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt'=\t \t \t \t \t \t{count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Angelegt': \t \t \t \t \t \t {counts_gesamt_angelegt.get(tuple(filter_gesamt_angelegt), 0)}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht Angelegt': \t \t \t \t \t \t {counts_gesamt_nicht_angelegt.get(tuple(filter_gesamt_nicht_angelegt), 0)}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht angelegt' Daten vollständig nein:\t\t\t {counts_nicht_angelegt_nein.get(tuple(filter_values_nicht_angelegt_nein), 0)}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht angelegt' Daten vollständig ja:\t\t\t  {counts_nicht_angelegt_ja.get(tuple(filter_values_nicht_angelegt_ja), 0)}")

print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Erreichbar:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_erreichbar}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - PING:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_ping}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - PING SNMP:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingsnmp}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - PING SNMP SSH:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingssh}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - PING SNMP TELNET:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingtelnet}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - PING SSH:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_pingssh}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - SNMP:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmp}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - SNMP SSH:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmpssh}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - SNMP TELNET:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_snmptelnet}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - SSH:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_ssh}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht erreichbar - TELNET:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtErreichbar_telnet}")
print(f"Anzahl der Zeilen Gesamt: 'aktiv|Fremdgerät|geplant Rückbau|gesperrt StableNet Status: 'Nicht angelegt' Daten vollständig ja und Nicht geprüft:'= {count_aktiv_Fremdgeraet_geplantRueckbau_gesperrt_nichtGeprueft}")


# ...

# Ausgabe der Ergebnisse
#print(f"Gesamtanzahl der Zeilen: \t \t \t \t \t \t \t \t \t \t \t{total_count}")

# ...


#Aufgabe 1)
#Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht angelegt' Daten vollständig nein: 
#Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht angelegt' Daten vollständig ja:




#Aufgabe 2)
#Bitte den ersten Filter (in allen obigen Zeilen) von 'aktiv' anpassen auf 'aktiv' oder 'Fremdgerät' oder 'geplant Rückbau' oder 'gesperrt' => Das sind alles aktive Devices!

#Hinweise für mich:
#Wo für steht r?
#um sicherzustellen, dass etwaige Escape-Zeichen im Pfad nicht interpretiert werden.
#  Dies kann nützlich sein, wenn du Windows-Pfade mit Backslashes verwendest,
#  da \ ein Escape-Zeichen in normalen Strings ist.

#Unterstrichzeichen counts_gesamt_nicht_angelegt, _ 
#In Python wird das Unterstrichzeichen (_) oft als Platzhalter für
#einen ungenutzten Wert verwendet. In deinem Fall gibt es Situationen,
#in denen der Rückgabewert der Funktion nicht verwendet wird,
#und das Unterstrichzeichen wird verwendet, um anzuzeigen, dass der Wert ignoriert wird. 
#Das bedeutet, dass der Rückgabewert an dieser Stelle in
#deinem Code nicht weiter verwendet wird.

#Für die Ausgabe alle Werte in einem Spalter anzuzeigen:
#with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
    #reader = csv.DictReader(csvfile, delimiter=';')
    #unique_values = set(row['Lifecylce Status'] for row in reader)

#print("Eindeutige Werte in 'Lifecylce Status':", unique_values)



