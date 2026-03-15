#Calculadora Geometrica
import math
while True:
    print("=" *30, "CALCULADORA GEOMETRICA", "="*30)
    print("¿Con que figura desea trabajar?:")
    print("====FIGURAS 2D====")
    print("1) Triangulo")
    print("2) Cuadrado")
    print("3) Rectangulo")
    print("4) Circulo")
    print("5) Triangulo Rectangulo")
    print("====FIGURAS 3D====")
    print("6) Cilindro")
    print("7) Piramide con base cuadradada")
    print("8) Esfera")
    print("9) Cubo")
    print("10) Salir")

    while True:
        try:
            opcion = int(input("Seleccione su opcion (1-10):"))

            while opcion < 1 or opcion > 10:
                print("Opcion invalida")
                opcion = int(input("Seleccione su opcion (1-10):"))

            else:
                break

        except ValueError:
            print("Error: Por favor, introduce un número válido.")

    if opcion == 1:
        while True:
            print("=" * 30, "OPERACIONES CON TRIANGULO", "=" * 30)
            print("1) Area")
            print("2) Perimetro")
            print("3) Calcular angulo")
            print("4) Volver")

            while True:
                try:
                    sub_opcion_1 = int(input("Seleccione su opcion (1-4):"))

                    while sub_opcion_1 < 1 or sub_opcion_1 > 4:
                        print("Opcion invalida")
                        sub_opcion_1 = int(input("Seleccione su opcion (1-4):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_1 == 1:
                print("=" * 30, "AREA DE UN TRIANGULO", "=" * 30,"(Por favor ingrese floats)")
                base=float(input("Cuanto mide la base?(cm):"))
                altura= float(input("Cuanto mide la altura?(cm):"))
                print(f"Resultado:{(base*altura)/2}cm al cuadrado")

            elif sub_opcion_1 == 2:
                print("=" * 30, "PERIMETRO DE UN TRIANGULO", "=" * 30,"(Por favor ingrese floats)")
                lado=float(input("Cuanto mide el lado?(cm):"))
                print(f"Resultado:{lado*3}cm")

            elif sub_opcion_1 == 3:
                print("=" * 30, "ANGULO DE UN TRIANGULO", "=" * 30,"(Por favor ingrese floats)")
                angulo1=float(input("Angulo 1:"))
                angulo2=float(input("Angulo 2:"))
                print(f"Resultado:{180-angulo1-angulo2}°")

            elif sub_opcion_1 == 4:
                break

    if opcion == 2:
        while True:
            print("=" * 30, "OPERACIONES CON CUADRADO", "=" * 30)
            print("1) Area")
            print("2) Perimetro")
            print("3) Volver")

            while True:
                try:
                    sub_opcion_2 = int(input("Seleccione su opcion (1-3):"))

                    while sub_opcion_2 < 1 or sub_opcion_2 > 3:
                        print("Opcion invalida")
                        sub_opcion_2 = int(input("Seleccione su opcion (1-3):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_2 == 1:
                print("=" * 30, "AREA DE UN CUADRADO", "=" * 30,"(Por favor ingrese floats)")
                base=float(input("Cuanto mide la base?(cm):"))
                print(f"Resultado:{base*2}cm al cuadrado")

            elif sub_opcion_2 == 2:
                print("=" * 30, "PERIMETRO DE UN CUADRADO", "=" * 30,"(Por favor ingrese floats)")
                lado=float(input("Cuanto mide el lado?(cm):"))
                print(f"Resultado:{lado*4}cm")

            elif sub_opcion_2 == 3:
                break

    if opcion == 3:
        while True:
            print("=" * 30, "OPERACIONES CON RECTANGULO", "=" * 30)
            print("1) Area")
            print("2) Perimetro")
            print("3) Volver")

            while True:
                try:
                    sub_opcion_3 = int(input("Seleccione su opcion (1-3):"))

                    while sub_opcion_3 < 1 or sub_opcion_3 > 3:
                        print("Opcion invalida")
                        sub_opcion_3 = int(input("Seleccione su opcion (1-3):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_3 == 1:
                base=float(input("Cuanto mide la base?(cm):"))
                altura= float(input("Cuanto mide la altura?(cm):"))
                print(f"Resultado:{base*altura}cm al cuadrado")

            elif sub_opcion_3 == 2:
                lado_l=float(input("Cuanto mide el lado largo?(cm):"))
                lado_c=float(input("Cuanto mide el lado corto?(cm):"))
                print(f"Resultado:{(lado_c*2)+(lado_l*2)}cm")

            elif sub_opcion_3 == 3:
                break

    if opcion == 4:
        while True:
            print("=" * 30, "OPERACIONES CON CIRCULO", "=" * 30)
            print("1) Area")
            print("2) Perimetro/Circunferencia")
            print("3) Calcular Radio")
            print("4) Calcular Diametro")
            print("5) Volver")

            while True:
                try:
                    sub_opcion_4 = int(input("Seleccione su opcion (1-5):"))

                    while sub_opcion_4 < 1 or sub_opcion_4 > 5:
                        print("Opcion invalida")
                        sub_opcion_4 = int(input("Seleccione su opcion (1-5):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_4 == 1:
                print("=" * 30, "AREA DE UN CIRCULO", "=" * 30,"(Por favor ingrese floats)")
                radio=float(input("Cuanto mide el radio?(cm):"))
                print(f"Resultado:{math.pi*(radio*radio)}cm al cuadrado")

            elif sub_opcion_4 == 2:
                print("=" * 30, "PERIMETRO DE UN CIRCULO", "=" * 30,"(Por favor ingrese floats)")
                radio=float(input("Cuanto mide el radio?(cm):"))
                print(f"Resultado:{2*math.pi*radio}cm")

            elif sub_opcion_4 == 3:
                print("=" * 30, "RADIO DE UN CIRCULO", "=" * 30,"(Por favor ingrese floats)")
                diametro=float(input("Cuanto mide el diametro?(cm):"))
                print(f"Resultado:{diametro/2}cm")

            elif sub_opcion_4 == 4:
                print("=" * 30, "DIAMETRO DE UN CIRCULO", "=" * 30,"(Por favor ingrese floats)")
                radio=float(input("Cuanto mide el radio?(cm):"))
                print(f"Resultado:{radio*2}cm")

            elif sub_opcion_4 == 5:
                break
    if opcion == 5:
        while True:
            print("=" * 30, "OPERACIONES CON TRIANGULO RECTANGULO", "=" * 30)
            print("1) Calcular Hipotenusa")
            print("2) Calcular Cateto")
            print("3) Volver")

            while True:
                try:
                    sub_opcion_5 = int(input("Seleccione su opcion (1-3):"))

                    while sub_opcion_5 < 1 or sub_opcion_5 > 3:
                        print("Opcion invalida")
                        sub_opcion_5 = int(input("Seleccione su opcion (1-3):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_5 == 1:
                print("=" * 30, "HIPOTENUSA DE UN TRIANGULO RECTANGULO", "=" * 30,"(Por favor ingrese floats)")
                lado_a=float(input("Cual mide el cateto a?(cm):"))
                lado_b=float(input("Cuanto mide el cateto b?(cm):"))
                print(f"Resultado:{((lado_a*lado_a)+(lado_b*lado_b))**0.5}cm")

            elif sub_opcion_5 == 2:
                print("=" * 30, "CATETO DE UN TRIANGULO RECTANGULO", "=" * 30,"(Por favor ingrese floats)")
                hipo=int(input("Cuanto mide la hipotenusa?(cm):"))
                cateto=int(input("Cuanto mide el cateto?(cm):"))
                print(f"Resultado:{((hipo**2)-(cateto**2))**0.5}cm")

            elif sub_opcion_5 == 3:
                break
    if opcion == 6:
        while True:
            print("=" * 30, "OPERACIONES CON CILINDRO", "=" * 30)
            print("1) Volumen")
            print("2) Volver")

            while True:
                try:
                    sub_opcion_6 = int(input("Seleccione su opcion (1-2):"))

                    while sub_opcion_6 < 1 or sub_opcion_6 > 2:
                        print("Opcion invalida")
                        sub_opcion_6 = int(input("Seleccione su opcion (1-2):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_6 == 1:
                print("=" * 30, "VOLUMEN DE UN CILINDRO", "=" * 30,"(Por favor ingrese floats)")
                radio=int(input("Cuanto mide el radio de la base?(cm):"))
                altura=int(input("Cuanto mide la altura del cilindro?(cm):"))
                print(f"Resultado:{math.pi*(radio)**2*altura}cm al cubo")

            elif sub_opcion_6 == 2:
                break

    if opcion == 7:
        while True:
            print("=" * 30, "OPERACIONES CON PIRAMIDE CON BASE CUADRADADA", "=" * 30)
            print("1) Volumen")
            print("2) Volver")

            while True:
                try:
                    sub_opcion_7 = int(input("Seleccione su opcion (1-2):"))

                    while sub_opcion_7 < 1 or sub_opcion_7 > 2:
                        print("Opcion invalida")
                        sub_opcion_7 = int(input("Seleccione su opcion (1-2):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_7 == 1:
                print("=" * 30, "VOLUMEN DE UNA PIRAMIDE CON BASE CUADRADADA", "=" * 30, "(Por favor ingrese floats)")
                altura=float(input("Cuanto mide la altura?(cm):"))
                lado=float(input("Cuanto mide uno de los lados?(cm):"))
                print(f"Resultado:{((lado)**2*altura)/3}cm al cubo")

            elif sub_opcion_7 == 2:
                break

    if opcion == 8:
        while True:
            print("=" * 30, "OPERACIONES CON ESFERA", "=" * 30)
            print("1) Volumen")
            print("2) Volver")

            while True:
                try:
                    sub_opcion_8 = int(input("Seleccione su opcion (1-2):"))

                    while sub_opcion_8 < 1 or sub_opcion_8 > 2:
                        print("Opcion invalida")
                        sub_opcion_8 = int(input("Seleccione su opcion (1-2):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")


            if sub_opcion_8 == 1:
                print("=" * 30, "VOLUMEN DE UNA ESFERA", "=" * 30, "(Por favor ingrese floats)")
                radio=float(input("Cuanto mide el radio?(cm):"))
                print(f"Resultado:{(4*math.pi*(radio)**3)/3}cm al cubo")

            elif sub_opcion_8 == 2:
                break

    if opcion == 9:
        while True:
            print("=" * 30, "OPERACIONES CON UN CUBO", "=" * 30)
            print("1) Volumen")
            print("2) Volver")

            while True:
                try:
                    sub_opcion_9 = int(input("Seleccione su opcion (1-2):"))

                    while sub_opcion_9 < 1 or sub_opcion_9 > 2:
                        print("Opcion invalida")
                        sub_opcion_9 = int(input("Seleccione su opcion (1-2):"))

                    else:
                        break

                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            if sub_opcion_9 == 1:
                print("=" * 30, "VOLUMEN DE UN CUBO", "=" * 30, "(Por favor ingrese floats)")
                arista=float(input("Cuanto mide una arista del cubo? (cm):"))
                print(f"Resultado:{arista**3}cm al cubo")

            if sub_opcion_9 == 2:
                break

    if opcion == 10:
        print("=" * 30, "GOODBYE", "=" * 30)
        print("Gracias por usar esta calculadora :)")
        break
