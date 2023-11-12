import tkinter as tk
import serial

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle de GPIO - Raspberry Pi Pico W")

        self.label = tk.Label(master, text="Digite o número do pino:")
        self.label.pack()

        self.pin_entry = tk.Entry(master)
        self.pin_entry.pack()

        self.read_button = tk.Button(master, text="Ler Pino", command=self.read_pin)
        self.read_button.pack()

        self.write_button = tk.Button(master, text="Escrever Pino", command=self.write_pin)
        self.write_button.pack()

        # Configuração da porta serial (ajuste a porta conforme necessário)
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    def read_pin(self):
        pin = self.pin_entry.get()
        command = f"READ {pin}\n"
        self.serial_port.write(command.encode())
        response = self.serial_port.readline().decode()
        print(f"Valor lido do pino {pin}: {response}")

    def write_pin(self):
        pin = self.pin_entry.get()
        value = input(f"Digite o valor a ser escrito no pino {pin}: ")
        command = f"WRITE {pin} {value}\n"
        self.serial_port.write(command.encode())
        print(f"Valor escrito no pino {pin}: {value}")

if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)
    root.mainloop()
