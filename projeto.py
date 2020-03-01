import re
import pandas as pd
import matplotlib.pyplot as plt

class Carros:
    def __init__(self, modelo, cor, ano, km, marca):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.km = km
        self.marca = marca

def buildData(obj):
    modelos = []
    cores = []
    anos = []
    kms = []
    marcas = []
    for item in obj:
        modelos.append(item.modelo)
        cores.append(item.cor)
        anos.append(item.ano)
        kms.append(item.km)
        marcas.append(item.marca)
    data = {'Modelo':modelos,
            'Cor':cores,
            'Ano':anos,
            'Quilometragem':kms,
            'Marca': marcas}
    return data


def plotModelo(data):
    if True:
        pass

if __name__ == '__main__':
    carros = []
    for number in range(1, 16):
        file = open("test" + str(number) + ".txt", "r", encoding="utf8").read().replace("\n", " ").replace(
            "Categoria Carros, vans e utilitários Modelo ", "")
        ano = re.findall('(\d{4})(?:./)(.*?\d{4})', file)[0]
        cor = re.findall("(?<=COR ).*?\w{4,8}", file, re.IGNORECASE)[0].capitalize()
        km = int(re.findall("(?<=KM ).*?\d{4,8}|(?<=Quilometragem ).*?\d{4,8}", file)[0])
        marca = re.findall("^\w{3,} | (?<=Marca ).*?\w{4,15}", file, re.IGNORECASE)[0].strip(" GM - ").capitalize()
        modelo = file.strip(" GM - ").split(" ")[1].capitalize()
        carros.append(Carros(modelo, cor, ano, km, marca))
    data = buildData(carros)
    dataF = pd.DataFrame(data)
    print(dataF)
    dataF.plot(kind='bar',x='Modelo',y='Quilometragem')
    plt.show()


    dataF.assign(dummy=1).groupby(['dummy', 'Marca']).size().to_frame().unstack().plot(kind='bar', stacked=True,
                                                                                     legend=False)
    plt.title('Número de carros por Marca')
    plt.xlabel('Marcas')
    plt.xticks([])
    current_handles, _ = plt.gca().get_legend_handles_labels()
    reversed_handles = reversed(current_handles)

    labels = reversed(dataF['Marca'].unique())

    plt.legend(reversed_handles, labels, loc='lower right')
    plt.show()

    dataF.assign(dummy=1).groupby(['dummy', 'Cor']).size().to_frame().unstack().plot(kind='bar', stacked=True,
                                                                                       legend=False)
    plt.title('Número de carros por Cor')
    plt.xlabel('Cores')
    plt.xticks([])
    current_handles, _ = plt.gca().get_legend_handles_labels()
    reversed_handles = reversed(current_handles)

    labels = reversed(dataF['Cor'].unique())

    plt.legend(reversed_handles, labels, loc='lower right')
    plt.show()

    dataF.groupby(['Ano', 'Cor']).size().unstack().plot(kind='bar', stacked=True)
    plt.show()

    dataF.groupby(['Marca', 'Modelo']).size().unstack().plot(kind='bar', stacked=True)
    plt.show()

