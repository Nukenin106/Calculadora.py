# Calculadora
fun = int(input('Escolha a função que deseja fazer.\n 1) Soma \n 2) Subtração \n 3) Divisão \n 4) mutiplicação \n '))
if (fun==1) and (fun<=4):
    num1 = int(input('Insira o primeiro número\n'))
    num2 = int(input('Insira o segundo número\n'))
# Inicio do if
    if fun==1:
        print('A função escolhida foi a soma \n A soma de ',num1,' com ',num2, ' dá ', num1+num2)
    else:
        if fun==2:
            print('A função escolhida foi a subtração \n A subtração de ',num1,' com ',num2, ' dá ', num1-num2)
        else:
            if fun==3:
                print('A função escolhida foi a divisão \n A divisão de ',num1,' com ',num2, ' dá ', num1/num2)
            else:
                if fun==4:
                    print('A função escolhida foi a  \n A soma de ',num1,' com ',num2, ' dá ', num1*num2)
else:
    print('Operação ínvalida!!')
