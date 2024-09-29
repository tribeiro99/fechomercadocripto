import tkinter as tk
from tkinter import ttk
import vectorbt as vbt
import pandas as pd

# Função para obter os últimos três valores de fecho das criptomoedas
def get_crypto_data():
    cript_price = vbt.YFData.download(
        ["BTC-EUR", "XMR-EUR", "ETH-EUR"],
        missing_index='drop').get("Close")
    
    last_three_values = cript_price.tail(3)
    return last_three_values

# Função para exibir os dados na interface
def display_data():
    data = get_crypto_data()
    output_text.delete(1.0, tk.END)  # Limpar o texto anterior
    output_text.insert(tk.END, data)

# Criando a interface gráfica
root = tk.Tk()
root.title("Últimos 3 Valores de Criptomoedas")
root.geometry("600x400")  # Aumenta o tamanho da janela

# Label
label = ttk.Label(root, text="Clique no botão para obter os últimos 3 valores de BTC, XMR e ETH:")
label.pack(pady=10)

# Botão para atualizar os dados
button = ttk.Button(root, text="Atualizar", command=display_data)
button.pack(pady=5)

# Área de texto para exibir os resultados com maior tamanho
output_text = tk.Text(root, height=15, width=70, font=("Helvetica", 12))  # Aumenta a área de texto
output_text.pack(pady=10)

# Executa a interface
root.mainloop()
