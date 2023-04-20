import serial
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class JIGZInterface:
    def __init__(self, master):
        self.master = master
        master.title("JIGZ MANUTENÇÃO")
        master.geometry("600x400")
        self.button_style = ttk.Style()
        self.button_style.configure("Custom.TButton", background="black", foreground="blue", font=("arial", 10, "bold"))
        
        # Cria widgets
        self.connection_status_label = tk.Label(master, text="Desconectado", fg="red", font=("arial", 15, "bold"))
        self.device_status_label = tk.Label(master, text="Status do aparelho: ")
        self.device_status_text = tk.StringVar(value="---")
        self.device_id_label = tk.Label(master, text="ID do aparelho:", fg="black", font= ("arial", 10, "bold" ))
        self.device_id_entry = tk.Entry(master, width=10)
        self.check_status_button = ttk.Button(master, text="Verificar status", command=self.check_status, style="Custom.TButton")
        self.command_label = tk.Label(master, text="Comando:")
        self.command_entry = tk.Entry(master, width=50)
        self.send_button = ttk.Button(master, text="Enviar", command=self.send_command, style="Custom.TButton")
        
        # Posiciona widgets
        self.connection_status_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        self.device_status_label.grid(row=1, column=0, sticky="W", padx=10, pady=10)
        tk.Label(master, textvariable=self.device_status_text).grid(row=1, column=1, sticky="W", padx=10, pady=10)
        self.device_id_label.grid(row=2, column=0, sticky="W", padx=10, pady=10)
        self.device_id_entry.grid(row=2, column=1, sticky="W", padx=10, pady=10)
        self.check_status_button.grid(row=3, column=0, sticky="W", padx=10, pady=10)
        self.command_label.grid(row=4, column=0, sticky="W", padx=10, pady=10)
        self.command_entry.grid(row=4, column=1, sticky="W", padx=10, pady=10)
        self.send_button.grid(row=4, column=2, sticky="W", padx=10, pady=10)
        
        # Inicializa a conexão serial
        self.ser = None
        self.connected = False

    def check_status(self):
        device_id = self.device_id_entry.get()
        if not self.connected:
            self.device_status_text.set("Erro: porta serial não está conectada")
            return    

        # A partir daqui, todo o código relacionado à porta serial foi removido


        # Apenas uma simulação de um status de dispositivo foi adicionada para teste
        self.device_status_text.set("Online")
            

    def send_command(self):
        command = self.command_entry.get()
        if not self.connected:
            messagebox.showerror("Erro", "Porta serial não está conectada")
            return
        
        # Aqui você pode adicionar o código para enviar o comando pela porta serial
        # Por exemplo: self.ser.write(command.encode())
        
# Cria a janela principal
root = tk.Tk()


# Cria a interface JIGZ
jigz = JIGZInterface(root)

# Inicia o loop principal do tkinter
root.mainloop()
