class Banco(object):
    count=0
    #Los atributos de cliente
    def __init__(self, name, date, curp, address, phone, first_deposit, account_type):
     self.name = name
     self.date = date
     self.curp = curp
     self.address = address
     self.phone =  phone
     self.first_deposit = first_deposit
     self.account_type = account_type

class Menu(): 
    num=0
    global listaclientes
    listaclientes = []
    print(listaclientes, "n")

    def NewAccount():
     nombre = input("Ingrese el nombre del cliente: ")
     date = input("Ingrese la fecha de nacimiento dd/mm/yyyy: ")
     curp = input("Ingrese CURP de la persona: ")
     address = input("Ingrese la dirección: ")
     phone = input("Ingrese el número de teléfono: ")
     first_deposit = input("Ingrese el deposito: ")
     account_type = input("Seleccione el tipo de cuenta: \n1. Ahorro \n2. Actual \n3. Por un año. \n4. Por dos años \n5. Por tres años ")  
     NUEVACUENTA = Banco(nombre,date,curp,address,phone,first_deposit,account_type)

     listaclientes.append(Banco)
     
    def view_list():
     print(listaclientes)

    def menuprincipal(self):
     op = 0
     while op != 7:
      print("                                       ||||||BIENVENIDO AL MENÚ PRINCIPAL||||||  \n ")
      print("1.Crea una nueva cuenta")
      print("2.Editar información en una cuenta existente")
      print("3.Transacción")
      print("4.Checar los detalles de una cuenta existente")
      print("5.Borrar cuenta")
      print("6.Lista de los clientes existentes")
      print("7.Salir")
      op = int(input("Ingresa la opción "))
      if op == 1:
       Menu.NewAccount()
      elif op == 2:
       print("         ||||||||||EDITA UNA CUENTA||||||||||")
      elif op == 3:
       print("         ||||||||||REALIZA UNA TRANSACCIÓN ||||||||||")
      elif op == 4:
       print("         ||||||||||VER CLIENTE||||||||||")
       Menu.BuscarCliente(self)        
      elif op == 5:
       print("         |||||||||BORRAR CLIENTE||||||||")
       Menu.BorrarCliente(self)       
      elif op == 6:
       print("         |||||||||VER LISTA||||||||")
       Menu.view_list()
      elif op == 7:
       print("Gracias por usar el programa")
       exit   
      elif op != 1 or op != 2 or op != 3 or op != 4 or op != 5 or op != 6 or op != 7:
        print("Ingrese una opción correcta")
 

#Termina clase

#archivocliente = Cliente()
MenuBanco=Menu()
MenuBanco.menuprincipal()


#Termina clase