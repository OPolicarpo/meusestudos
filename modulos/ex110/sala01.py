try:
    a = int(input('Numerador: '))
    b = int(input('denominador: '))
    r = a / b
except Exception as erro:
    print(f'problema encontrado foi {erro.__class__}')

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou')

except ZeroDivisionError:
    print(' O usuario preferiu nao informar os dados ')

except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')
else:
    print(r)
finally:
    print('volte sempre! Muito obrigado!')