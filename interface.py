import tkinter as tk
import random

# Variáveis globais
jogadas = 3
dados = {"dado1": 0, "dado2": 0, "dado3": 0, "dado4": 0, "dado5": 0}
dados_guardados = {"dado1": False, "dado2": False, "dado3": False, "dado4": False, "dado5": False}
pontuacao_total = 0

def sorteio():
    global jogadas, pontuacao_total, dados, dados_guardados
    try:
        valor = int(entrada.get())  # Obter valor da entrada
        if valor == 2:
            if jogadas > 1:
                jogadas -= 1

                # Habilitar o botão "Guardar Dados"
                botao_guardar.config(state=tk.NORMAL)

                # Sorteio dos dados não guardados
                for dado in dados:
                    if not dados_guardados[dado]:
                        dados[dado] = random.randint(1, 6)

                # Pontuação atual
                pontuacao_atual = sum(dados.values())
                pontuacao_total += pontuacao_atual  # Soma ao total

                # Formatar os dados sorteados para exibição
                resultados_dados = (
                    f"Dado 1: {dados['dado1']}, Dado 2: {dados['dado2']}, "
                    f"Dado 3: {dados['dado3']}, Dado 4: {dados['dado4']}, Dado 5: {dados['dado5']}"
                )
                # Atualizar o label com as jogadas restantes e os resultados
                label_resultado.config(
                    text=f"Jogadas restantes: {jogadas}\n\n{resultados_dados}\n\n"
                         f"Escolha quais dados deseja guardar digitando os números correspondentes (ex: 1 3 5).\n"
                         f"Depois, pressione o botão 'Guardar Dados'."
                )
            else:
                
                label_resultado.config(
                    text=f"Fim de jogo! Você não tem mais jogadas.\nSua pontuação total foi de: {pontuacao_total}\n"
                    f"\nDado 1: {dados['dado1']}, Dado 2: {dados['dado2']}, "
                    f"Dado 3: {dados['dado3']}, Dado 4: {dados['dado4']}, Dado 5: {dados['dado5']}"
                )
                botao_guardar.config(state=tk.DISABLED)
            entrada.delete(0, tk.END)

    except ValueError:
        label_resultado.config(text="Digite um número inteiro válido!")

def guardar_dados():
    global dados_guardados
    try:
        valores_guardar = entrada.get().strip().split()  # Obter os números dos dados a guardar
        mensagem_erro = ""  # Armazena mensagens de erro
        for valor in valores_guardar:
            if valor.isdigit() and 1 <= int(valor) <= 5:
                dado = f"dado{valor}"
                if dados_guardados[dado]:
                    mensagem_erro += f"Erro: {dado} já foi guardado.\n"
                else:
                    dados_guardados[dado] = True
            else:
                mensagem_erro += f"Erro: '{valor}' não é um número de dado válido.\n"

        if mensagem_erro:
            label_resultado.config(text=mensagem_erro.strip())
        else:
            label_resultado.config(
                text="Dados guardados! Pressione 'Jogar' para continuar.\n"
                     f"Dados guardados: {[dado for dado, guardado in dados_guardados.items() if guardado]}"
            )

        # Desabilitar o botão "Guardar Dados" até que "Jogar" seja pressionado novamente
        botao_guardar.config(state=tk.DISABLED)
    except ValueError:
        label_resultado.config(text="Digite números válidos separados por espaço!")
    entrada.delete(0, tk.END)


def rules():
    try:
        valor = int(entrada.get())  # Obtendo o texto inserido pelo usuário
        if valor == 1:
            label_resultado.config(
                text="Regras🎲\n - Você tem apenas 3 jogadas de dados\n"
                     " - Escolha quais dados deseja guardar para tentar obter maior pontuação final\n"
                     " - Pressione 'Guardar Dados' após escolher."
            )
    except ValueError:
        label_resultado.config(text="Digite um número inteiro válido!")
    entrada.delete(0, tk.END)

# Interface Gráfica
root = tk.Tk()
root.title("Jogo do General")
root.geometry("800x600")
root.configure(bg="white")

label = tk.Label(root, text="Jogo do General", font=("Cardinal", 16), bg="white", fg="purple")
label.pack(pady=20)
label = tk.Label(
    root,
    text="Digite 1 para ver as regras\nDigite 2 para iniciar o jogo\nAperte no X para sair",
    font=("Cardinal", 13),
    bg="white",
    fg="purple"
)
label.pack(pady=0)

entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=10)  # Exibindo a entrada com espaçamento vertical

botao_regras = tk.Button(root, text="Regras", font=("Cardinal", 12), bg="white", fg="black", command=rules)
botao_regras.pack(pady=10)

botao_jogar = tk.Button(root, text="Jogar", font=("Cardinal", 12), bg="white", fg="black", command=sorteio)
botao_jogar.pack(pady=10)

# Botão "Guardar Dados" começa desabilitado
botao_guardar = tk.Button(root, text="Guardar Dados", font=("Cardinal", 12), bg="white", fg="black", command=guardar_dados, state=tk.DISABLED)
botao_guardar.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Cardinal", 10), bg="white", fg="darkblue")
label_resultado.pack(pady=20)

root.bind("key", sorteio)
root.mainloop()
