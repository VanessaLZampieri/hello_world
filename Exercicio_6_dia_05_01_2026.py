dia = int(input('Digite um número de dias: '))

convertido_hora = dia*24
convertido_minuto = dia * 1440
convertido_segundo = dia * 86400

print(f'{dia} dias equivalem a {convertido_hora} horas, {convertido_minuto} minutos e {convertido_segundo} segundos')