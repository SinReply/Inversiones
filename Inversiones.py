import random as rm
import time as t
import sys

neg = []
pos = []
nuevo_monto = 0
monto = 0
variacion = 0
perdida = 0
ganancia = 0
monto_anterior = 0

def obtener_listas():
  global neg, pos

  neg_minus = 0
  pos_maxus = 0
  for _ in range(201):
    neg.append(round(neg_minus, 3))
    neg_minus-= 0.001

    pos.append(round(pos_maxus, 3))
    pos_maxus += 0.001

  neg.remove(0.0); pos.remove(0.0)
  return None

def invertir(dinero):
  global neg, pos, variacion, perdida, ganancia, monto_anterior
  dinero = float(dinero)
  monto_anterior = dinero

  prob = rm.randint(0, 100)
  if prob < 48:
    variacion = rm.choice(neg)
  elif prob >= 48:
    variacion = rm.choice(pos)
  else:
    variacion = 0

  if variacion < 0:
    perdida = round((dinero * variacion), 2)
    ganancia = 0
  else:
    ganancia = round((dinero * variacion), 2)
    perdida = 0
    
  monto_nuevo = dinero + perdida + ganancia
  monto_nuevo = float(round(monto_nuevo, 2))
  if monto_nuevo <= 0:
    print(f"Te quedaste en ¥0.\n")
    sys.exit()
  else:
    return monto_nuevo

def main():
  global neg, pos, nuevo_monto, monto, variacion, monto_anterior, ganancia, perdida
  obtener_listas()
  
  #Errores
  
  Error_0 = "Debes ingresar una opcion valida."
  Error_1 = "El monto inicial es invalido."
  Error_5 = "El saldo añadido es invalido."

  #Fin de Erorres

  while True:
    opcion = input("Ingresa Una Opcion Para Continuar:\n- Opcion 1 - Ingresar monto inicial.\n- Opcion 2 - Generar interes.\n- Opcion 3 - Salir del programa.\n- Opcion 4 - Generar intereses por lotes.\n- Opcion 5 - Añadir saldo.\n--> ")
    try:
      opcion = int(opcion)
      if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
        print("Procesando La Opcion Seleccionada.", end="")
        for _ in range(2):
          t.sleep(0.15)
          print(".", end = "")
        print("\n")
      else:
        raise ValueError

    except ValueError:
      print(f"Error: {Error_0}\n")
      main()

    if opcion == 1:
      monto = input("Ingresa el monto inicial para invertir: ")
      try:
        monto = float(monto)
        monto = round(monto, 2)
      except ValueError:
        print(f"Error: {Error_1}\n")
        main()

      print("\nProcesando el monto ingresado.", end = "")
      if monto < 0:
        print(f"\nNo puedes ingresar un monto inferior o igual a 0.\n")
        main()
      else:
        for _ in range(2):
          t.sleep(0.15)
          print(".", end = "")
        print(f"\nMonto Actual: ¥{monto}")
        nuevo_monto = float(invertir(monto))
        nuevo_monto = round(nuevo_monto, 2)
        t.sleep(2)
        print(f"\nDespues de esperar un poco, tu saldo actual es de ¥{nuevo_monto}\n- Con un interes de: {round((variacion * 100), 3)}%\n", end = "")
        if nuevo_monto < monto_anterior:
          print(f"- Obtuviste una perdida de ¥{perdida}\n")
        else:
          print(f"- Obtuviste una ganancia de ¥{ganancia}\n")
        main()
    elif opcion == 2:
      if nuevo_monto == 0:
        print("Debes primero ingresar un monto inicial.\n")
        main()
      else:
        nuevo_monto = invertir(nuevo_monto)
        nuevo_monto = round(nuevo_monto, 2)
        t.sleep(0.06)
        print(f"\nDespues de esperar un poco, tu saldo actual es de ¥{nuevo_monto}\nCon un interes de: {round((variacion * 100), 3)}%\n", end = "")
        if nuevo_monto < monto_anterior:
          print(f"- Obtuviste una perdida de ¥{perdida}\n")
        else:
          print(f"- Obtuviste una ganancia de ¥{ganancia}\n")
    elif opcion == 3:
      if float(monto) < float(nuevo_monto):
        print(f"Terminaste con una ganancia de ¥{round((float(nuevo_monto) - float(monto)), 2)}")
      else:
         print(f"Terminaste con una perdida de ¥{round((float(nuevo_monto) - float(monto)), 2)}")
      
      print("Cerrando el programa.", end = "")
      for _ in range(2):
        t.sleep(0.75)
        print(".", end = "")
      print("\nPrograma Cerrado.")
      sys.exit()
    elif opcion == 4:
      if nuevo_monto == 0:
        print("Debes primero ingresar un monto inicial.\n")
        main()
      else:  
        veces = input("Ingresa cuantas veces quieres invertir. (MIN-1 999-MAX) --> "); print("\n")
        try:
          veces = int(veces)
        except ValueError:
          print(f"Debes ingresar una cantidad válida.\n")
          main()
        if veces >= 1 or veces <= 999:
          for i in range(veces):
            monto_nuevo = nuevo_monto
            nuevo_monto = invertir(nuevo_monto)
            if nuevo_monto < 0:
              print(f"Te quedaste en banca rota y debes ¥{nuevo_monto}\n")
              sys.exit()
            elif nuevo_monto == 0:
              print(f"Te quedaste justamente en ¥0, no debes nada.")
              main()
            else:
              print(f"Acabaste con la cantidad de ¥{nuevo_monto} Despúes de {i + 1} años.")
              
              if float(monto_nuevo) < float(nuevo_monto):
                print(f"Terminaste con una ganancia de ¥{round((float(nuevo_monto) - float(monto_nuevo)), 2)} Este año.\n")
              else:
                 print(f"Terminaste con una perdida de ¥{round((float(nuevo_monto) - float(monto_nuevo)), 2)} Este año.\n")
                
          if float(monto) < float(nuevo_monto):
            print(f"\nTerminaste con una ganancia total de ¥{round((float(nuevo_monto) - float(monto)), 2)}\n")
          else:
             print(f"\nTerminaste con una perdida total de ¥{round((float(nuevo_monto) - float(monto)), 2)}\n")
        else:
          print(f"Debes ingresar una cantidad entre el 1 hasta el 999 --> [1, 999]\n")
          main()
    elif opcion == 5:
      if nuevo_monto == 0:
        print("Debes primero ingresar un monto inicial.\n")
        main()
      else:
        mas_saldo = input("Ingresa el monto inicial para invertir: ")
        try:
          mas_saldo = float(monto)
          mas_saldo = round(monto, 2)
        except ValueError:
          print(f"Error: {Error_5}\n")
          main()
        monto_nuevo = nuevo_monto
        nuevo_monto += mas_saldo
        print(f"Saldo actualizado de ¥{monto_nuevo} --> ¥{nuevo_monto}\n")
        main()

main()
