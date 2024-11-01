def converter(hora, minuto):
    if hora < 0:
        return None, None

    if hora == 0:
        return 12, minuto, "A"
    elif hora == 12:
        return 12, minuto, "P"
    elif hora > 12:
        return hora - 12, minuto, "P"
    else:
        return hora, minuto, "A"


def exibir_hora(hora, minuto, periodo):
    periodo_texto = "A.M." if periodo == "A" else "P.M."
    print(f"{hora:02}:{minuto:02} {periodo_texto}")


while True:
    hora = int(input("Digite a hora em notação de 24 horas (digite um valor negativo para encerrar): "))
    if hora < 0:
        break
    minuto = int(input("Digite os minutos: "))

    hora_12, minuto_12, periodo = converter(hora, minuto)
    if hora_12 is not None:
        exibir_hora(hora_12, minuto_12, periodo)
