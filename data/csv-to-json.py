
import csv
import json

csvFilePath = r'materias.csv'
jsonFilePath = r'materias.json'

def make_json(csvFilePath, jsonFilePath):
     
    data = {}
     
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        for row in csvReader:
            if (row["materia1"] in data):
                data[row["materia1"]]["equiv"] = {
                    "materia": data[row["materia1"]]["equiv"]["materia"],
                    "credito": data[row["materia1"]]["equiv"]["credito"],
                    "materia2": row["materia2"],
                    "credito2": row["creditos2"],
                }
            else:
                data[row["materia1"]] = {
                    "cuatrimestre": row["cuatrimestre"],
                    "creditosActuales": row["creditos1"],
                    "equiv": {
                        "materia": row["materia2"],
                        "credito": row["creditos2"],
                    }
                }
 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=True))
       
make_json(csvFilePath, jsonFilePath)