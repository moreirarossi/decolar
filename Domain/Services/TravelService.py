from Domain.Model import Travel

def CheckValues(params: str):
    def _checkItem(item, text):
        try:
            value = listParams[item]
        except IndexError:
            erros.append(text)

    listParams = params.split(",")
    erros = []
    _checkItem(0,"Informe o aeroporto de ORIGEM")
    _checkItem(1,"Informe o aeroporto de DESTINO")
    _checkItem(2,"Informe a data de PARTIDA")
    _checkItem(3,"Informe a data de RETORNO")
    _checkItem(4,"Informe a quantidade de passageiros")

    if erros:
        print("\n".join(erros))
    else:
        print(
            (
                "Origem:{0}\n"
                "Destino:{1}\n"
                "Saida:{2}\n"
                "Chegada:{3}\n"
                "Passageiros:{4}\n"
            ).format(*listParams)
        )
