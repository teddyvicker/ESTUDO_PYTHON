entrada = input('Voce quer entrar ou sair do sistema?')
#entrada = 2 ou 1

if entrada == 'entrar':
    print('Voce entrou no sistema')
elif entrada == 'sair':
    print('voce saiu do sistema')
else:
    print('error: voce precisa digitar entrar ou sair')

#match entrada:
#    case 1:
#        print('Voce entrou no sistema')
#    case 2:
#        print('voce saiu do sistema')
#    case _ :
#        print('error: voce precisa digitar entrar ou sair')

#tipos de analise de dados com if e match