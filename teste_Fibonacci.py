

# Nesta primeira parte damos as condições para definir a sequência de Fibonacci
# Tendo como base a sua fórmula [ Fn = Fn - 1 + Fn - 2] , definida na linha 12 como " fn[i-1] + fn[i-2] "
# Utilizamos a função append para registrar o ultima número dado e continuar a sua soma progressivamente.


def seq_fibonacci(x):
    if x == 0:
        return [0]
    elif x == 1:
        return [0, 1]
    else:
        fn = [0, 1]
        for i in range(2, x +1):
            fn.append(fn[i-1] + fn[i-2])
        return fn

# Na segunda etapa definindas as condições para soma , utilizamos condições booleanas
# para verificar se o numero retorna um resultado que atende à condição especificada.

def is_in_seq_fibonacci(x):
    fn = seq_fibonacci(x)
    if x in fn:
        return True
    else:
        return False

# Na terceira etapa , criamos um input e guardamos em uma variavel "x"
# ao guardar esse valor de entrada utilizamos para comparar com os numeros contidos na sequencia registrada.
# Para retornar ao usuário usamos as condições if = como pertencente e else = como não pertencente.

x = int(input("Insira um número para saber se ele pertence a sequencia de Fibonacci: "))

if is_in_seq_fibonacci(x):
    print(f" Sim ! O número {x} pertence à sequencia.")
else:
    print(f" Não ! O número {x} não pertence à sequencia.")
