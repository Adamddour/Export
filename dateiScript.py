import csv

def read_csv(file_path, selected_fields, filter_columns=None, filter_values=None):
    data = []
    counts = {}  # Dictionary zur Verfolgung der Zählungen für jeden eindeutigen Wert

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Überprüfe, ob mindestens eine ausgewählte Spalte in der CSV-Datei vorhanden ist
        if not all(field in reader.fieldnames for field in selected_fields):
            print("Warnung: Keine der ausgewählten Spalten ist in der CSV-Datei vorhanden.")
            print(f"Tatsächliche Spaltennamen in der CSV-Datei: {reader.fieldnames}")
            print(f"Ausgewählte Spalten: {selected_fields}")

        for row in reader:
            selected_data = {field: row[field] for field in selected_fields if field in row}

            # Überprüfe, ob Filterbedingungen angegeben sind und die Bedingungen erfüllt sind
            if filter_columns is not None and filter_values is not None:
                filter_match = all(row.get(col) == val for col, val in zip(filter_columns, filter_values))
                if filter_match:
                    data.append(selected_data)
                    counts.setdefault(tuple(filter_values), 0)
                    counts[tuple(filter_values)] += 1
            else:
                data.append(selected_data)

    return data, counts

file_path = r'M:\_Ordnerumleitung\Desktop\Tasks\ExcelDateiauslesen\export.csv'
selected_fields = ['StableNet Status', 'Daten vollständig','Erreichbar Status + Fehler']  # Ersetze dies durch die tatsächlichen Spaltennamen
filter_columns = ['StableNet Status', 'Daten vollständig','Erreichbar Status + Fehler']

filter_values_nicht_angelegt_ja = ['Nicht angelegt', 'ja']
filter_values_nicht_angelegt_nein = ['Nicht angelegt', 'nein','Nicht geprüft']

result, counts_nicht_angelegt_ja = read_csv(file_path, selected_fields, filter_columns, filter_values_nicht_angelegt_ja)
result, counts_nicht_angelegt_nein = read_csv(file_path, selected_fields, filter_columns, filter_values_nicht_angelegt_nein)


print(f"Anzahl der Zeilen für 'Nicht angelegt' Daten vollständig ja: {counts_nicht_angelegt_ja.get(tuple(filter_values_nicht_angelegt_ja), 0)}")
print(f"Anzahl der Zeilen für 'Nicht angelegt' Daten vollständig nein und Nicht geprüft: {counts_nicht_angelegt_nein.get(tuple(filter_values_nicht_angelegt_nein), 0)}")




#Hinweise für mich:
#Wo für steht r?
#um sicherzustellen, dass etwaige Escape-Zeichen im Pfad nicht interpretiert werden.
#  Dies kann nützlich sein, wenn du Windows-Pfade mit Backslashes verwendest,
#  da \ ein Escape-Zeichen in normalen Strings ist.