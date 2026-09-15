cargo = 'Supervisor'
hora = 12
chave_emergencia = True

if (chave_emergencia or cargo == 'Supervisor' or
    (cargo == 'Operador' and 8 <= hora <= 17)):
    print('Acesso Permitido')
else:
    ('Acesso Bloqueado')
    # outra forma é hora >= 8 and hora <= 17
    # com input:
    # cargo = input('Digite o cargo:')
# hora = int(input('Digite o horario atual (em horas):'))
# chave_emergencia = int(input('Possui chave de emercencia?(1 para Sim, 0 para Não)))

# if (chave_emergencia or cargo == 'Supervisor' or
    # (cargo == 'Operador' and 8 <= hora <= 17)):
    # print('Acesso Permitido')
# else:
    #print ('Acesso Bloqueado')