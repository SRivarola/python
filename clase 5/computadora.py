import time


class Computadora:
    def __init__(self, marca, modelo, precio, stock):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.stock = stock
        self.encendida = False

    def __str__(self):
        return f"Computadora marca: {self.marca}, modelo: {self.modelo}"

    def __isInStock__(self):
        time.sleep(1)
        if self.stock > 0:
            return "Si hay stock disponible"
        else:
            return "Lamentablemente no hay stock disponible."

    def __on_off__(self):
        time.sleep(1)
        if self.encendida == False:
            self.encendida = True
            print("La pc esta encendida")
            return self.encendida
        else:
            self.encendida = False
            print("La pc esta apagada")
            return self.encendida

    def __abrirWord__(self):
        time.sleep(1)
        if self.encendida == True:
            return "Se abrio el word correctamente"
        else:
            return "La pc debe estar encendida para poder abrir programas"

    def __vender__(self):
        time.sleep(1)
        if self.stock > 0:
            self.stock = self.stock - 1
            return "Felicitaciones has vendido la pc"
        else:
            return "No hay stock para vender, intente con otro modelo"


if __name__ == "__main__":

    lenovo = Computadora("Lenovo", "LNV-14N", 185000, 10)
    print(lenovo)
    print(lenovo.__isInStock__())
    lenovo.__on_off__()
    lenovo.__on_off__()
    print(lenovo.__abrirWord__())
    print(lenovo.__vender__())
