horario = input('Digite horario (0-23): ')

if horario.isdigit():
    horario = int(horario)
    
    if horario < 0 or horario > 23:
        print('Horário deve estar entre 0 e 23 horas.')
    else:
        if horario <= 11:
             print('Boa dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horario entre 0 e 23.')
