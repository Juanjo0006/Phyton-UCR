sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
                "math":  90
            },
        }
    }
}

notas= sampleDict["class"]["student"]["marks"]


promedio = sum(notas.values()) / len(notas)


resultado = {"name": sampleDict["class"]["student"]["name"], "marks": promedio}

print(resultado)