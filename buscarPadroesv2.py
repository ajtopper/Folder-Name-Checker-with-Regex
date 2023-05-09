import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Função para localizar as pastas e contar as ocorrências do padrão
def encontrar_pastas():
    # Abre a caixa de diálogo para o usuário escolher o diretório
    diretorio = filedialog.askdirectory()
    
    # Inicializa o contador de ocorrências do padrão e a lista de pastas encontradas e fora do padrão
    count = 0
    pastas_encontradas = []
    pastas_fora_padrao = []
    
    # Loop pelos arquivos do diretório
    for arquivo in os.listdir(diretorio):
        # Verifica se o arquivo é uma pasta e se o nome corresponde ao padrão
        if os.path.isdir(os.path.join(diretorio, arquivo)) and re.match(r'\d{4}_\d{2}_.*', arquivo):
            count += 1
            pastas_encontradas.append(arquivo)
        else:
            pastas_fora_padrao.append(arquivo)
    
    # Exibe o resultado na caixa de diálogo
    messagebox.showinfo('Resultado', f'Foram encontradas {count} pastas no padrão especificado')
    
    # Escreve um arquivo de log com os nomes das pastas encontradas
    with open(os.path.join(diretorio, 'log_dentro_padrao.txt'), 'w') as log_file:
        log_file.write('\n'.join(pastas_encontradas))
    
    # Escreve um arquivo de log com os nomes das pastas fora do padrão
    with open(os.path.join(diretorio, 'log_fora_padrao.txt'), 'w') as log_file:
        log_file.write('\n'.join(pastas_fora_padrao))

# Cria a janela principal com o botão "Começar"
root = tk.Tk()
root.title('Localizador de pastas')
root.minsize(320,240)
botao_comecar = tk.Button(root, text='Começar', command=encontrar_pastas)
botao_comecar.pack()

root.mainloop()
