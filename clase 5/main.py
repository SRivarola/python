from computadora import Computadora

lenovo = Computadora("Lenovo", "LNV-14N", 185000, 10)
hp = Computadora("HP", "tfd-1014", 210000, 0)

print(lenovo)
print(lenovo.__isInStock__())
lenovo.__on_off__()
lenovo.__on_off__()
print(lenovo.__abrirWord__())
print(lenovo.__vender__())

print(hp)
print(hp.__isInStock__())
hp.__on_off__()
hp.__on_off__()
hp.__on_off__()
print(hp.__abrirWord__())
print(lenovo.__vender__())
