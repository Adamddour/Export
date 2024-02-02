import csv

def read_csv(file_path, selected_fields, filter_column=None, filter_values=None):
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

            # Überprüfe, ob eine Filterbedingung angegeben ist und die Bedingung erfüllt ist
            if filter_column is not None and filter_values is not None:
                column_value = row.get(filter_column)
                # Überprüfe, ob der Wert in den Filterwerten enthalten ist, einschließlich Leerzeichen
                if any(value.strip() == column_value for value in filter_values):
                    data.append(selected_data)
                    counts.setdefault(column_value, 0)
                    counts[column_value] += 1
            else:
                data.append(selected_data)

    return data, counts

file_path = r'M:\_Ordnerumleitung\Desktop\Tasks\ExcelDateiauslesen\export.csv'
selected_fields = ['StableNet Status']  # Ersetze dies durch die tatsächlichen Spaltennamen
filter_column = 'StableNet Status'
filter_values = ['Angelegt', 'Nicht angelegt']

result, counts = read_csv(file_path, selected_fields, filter_column, filter_values)

#for entry in result:
    #print(entry)

for value, count in counts.items():
    print(f"Anzahl der Zeilen für '{value}': {count}")



#Hinweise für mich:
#Wo für steht r?
#um sicherzustellen, dass etwaige Escape-Zeichen im Pfad nicht interpretiert werden.
#  Dies kann nützlich sein, wenn du Windows-Pfade mit Backslashes verwendest,
#  da \ ein Escape-Zeichen in normalen Strings ist......