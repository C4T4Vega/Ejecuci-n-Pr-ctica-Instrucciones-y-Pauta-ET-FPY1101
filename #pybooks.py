#pybooks
productos = {'8475HD': ['HP',15.6,'8GB','DD','1T','Intel Core i7', 'Nvidia GTX1050'], 
             '2175HD': ['Aser', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2028'],
             'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'], 
             'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel core i3', 'Nvidia GTX1050'],
             '123FHD': ['Aser', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
             '342FHD': ['Aser', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'NvidiaGTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']
             }
stock = {'8475HD': [387990,10], 
             '2175HD': [327990,4],
             'JjfFHD': [424990,1],
             'fgdxFHD': [664990,21], 
             'GF75HD': [290890,32],
             '123FHD': [444990,7],
             '342FHD': [749990,2],
             'UWU131HD': [349990,1]
             }

def stock_marca(marca):
  print(marca)


def busqueda_precio(p_min,p_max):
        print("Los notebooks entre los precios consultados son: ")

def ordenar_productos():
  for i in productos:
      print(f"marca: {productos[i][0]} - modelo: {i} - Ram: {productos[i][2]} - Disco: {productos[i][3]}")

def main ():
    while True:
        print("""*** MENU PRINCIPAL***
              1-. Stock marca.
              2-. Busqueda por precio.
              3-. Listado de productos.
              4-. Salir.""")
        try:
            op = int(input("Ingrese opción: "))
        except ValueError:
            print("Ingrese digitos positivos.")
            return op
        if op == 1:
            marca = input("Ingrese marca a consultar: ").capitalize()
            stock_marca(marca)
        elif op == 2:
            try:
                p_min = int(input("Ingrese precio minimo:"))
            except ValueError:
                print("Ingrese digitos.")
                return p_min
            while True:
                try:
                    p_max = int(input("Ingrese precio maximo: "))
                except ValueError:
                    print("Ingrese digitos")  
                if p_max < p_min:
                    print("Rango no valido") 
                else:
                    break
            busqueda_precio(p_min,p_max)
        elif op == 3:
            print("-------Listado de Notebooks Ordenados-------")
            ordenar_productos()
            print("---------------------------------------------------------")
        elif op == 4:
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción valida!!")


main()