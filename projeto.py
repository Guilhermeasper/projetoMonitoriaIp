import re

files = []
anos = []
cores = []
kms = []
marcas = []
for number in range(1, 16):
    file = open("test" + str(number) + ".txt", "r", encoding="utf8").read().replace("\n", " ").replace(
        "Categoria Carros, vans e utilitários Modelo ", "")
    ano = re.findall('(\d{4})(?:./)(.*?\d{4})', file)
    cor = re.findall("(?<=COR ).*?\w{4,8}", file, re.IGNORECASE)
    km = re.findall("(?<=KM ).*?\d{4,8}|(?<=Quilometragem ).*?\d{4,8}", file)
    marca = re.findall("^\w{3,} | (?<=Marca ).*?\w{4,15}", file, re.IGNORECASE)[0].strip(" GM - ")
    modelo = file.strip(" GM - ").split(" ")[1]
    print(modelo)
    kms.append(km)
    cores.append(cor)
    anos.append(ano)
    marcas.append(marca)
    files.append(file)
