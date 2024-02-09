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
filter_gesamt_aktiv=['aktiv']
filter_gesamt_angelegt=['aktiv','Angelegt']
filter_gesamt_nicht_angelegt=['aktiv','Nicht angelegt']
filter_values_nicht_angelegt_ja = ['aktiv','Nicht angelegt', 'ja']
filter_values_nicht_angelegt_nein = ['aktiv','Nicht angelegt', 'nein','Nicht geprüft']

result, counts_gesamt_aktiv, total_count = read_csv(file_path, selected_fields, filter_columns, filter_gesamt_aktiv)
result, counts_gesamt_angelegt, total_count = read_csv(file_path, selected_fields, filter_columns, filter_gesamt_angelegt)
result, counts_gesamt_nicht_angelegt, _ = read_csv(file_path, selected_fields, filter_columns, filter_gesamt_nicht_angelegt)
result, counts_nicht_angelegt_ja, _ = read_csv(file_path, selected_fields, filter_columns, filter_values_nicht_angelegt_ja)
result, counts_nicht_angelegt_nein, _ = read_csv(file_path, selected_fields, filter_columns, filter_values_nicht_angelegt_nein)

print(f"Gesamtanzahl der Zeilen: \t \t \t \t \t \t \t \t \t \t \t{total_count}")
print(f"Anzahl der Zeilen Gesamt aktiv: \t \t \t \t \t \t \t \t \t \t{counts_gesamt_aktiv.get(tuple(filter_gesamt_aktiv), 0)}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Angelegt': \t \t \t \t \t \t {counts_gesamt_angelegt.get(tuple(filter_gesamt_angelegt), 0)}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht Angelegt': \t \t \t \t \t \t {counts_gesamt_nicht_angelegt.get(tuple(filter_gesamt_nicht_angelegt), 0)}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht angelegt' Daten vollständig ja: \t \t \t  {counts_nicht_angelegt_ja.get(tuple(filter_values_nicht_angelegt_ja), 0)}")
print(f"Anzahl der Zeilen Status: 'aktiv' StableNet Status: 'Nicht angelegt' Daten vollständig nein und Nicht geprüft: \t {counts_nicht_angelegt_nein.get(tuple(filter_values_nicht_angelegt_nein), 0)}")


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



