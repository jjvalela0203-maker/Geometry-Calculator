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

    opcion= int(input("Seleccione su opcion (1-10):"))
    
    while opcion < 1 or opcion > 10:
        print("Opcion invalida")
        opcion= int(input("Seleccione su opcion (1-10):"))
    
    if opcion == 1:
        while True:
            print("=" * 30, "OPERACIONES CON TRIANGULO", "=" * 30)
            print("1) Area")
            print("2) Perimetro")
            print("3) Calcular angulo")
            print("4) Volver")

            sub_opcion_1=int(input("Seleccione su opcion (1-3):"))

            if sub_opcion_1 == 1:
                base=float(input("Cual es la base?:"))
                altura= float(input("Cual es la altura?:"))
                print(f"Resultado:{(base*altura)/2}")
            
            elif sub_opcion_1 == 2:
                lado=float(input("Cual es el lado?:"))
                print(f"Resultado:{lado*3}")
            
            elif sub_opcion_1 == 3:
                angulo1=float(input("Angulo 1:"))
                angulo2=float(input("Angulo 2:"))
                print(f"Resultado:{180-angulo1-angulo2}")
            
            elif sub_opcion_1 == 4:
                break
    
    if opcion == 2:
        while True:
            print("=" * 30, "OPERACIONES CON CUADRADO", "=" * 30)
            print("1) Area")
            print("2) Perimetro")
            print("3) Volver")

            sub_opcion_2= int(input("Seleccione su opcion (1-3):"))
            if sub_opcion_2 == 1:
                print("=" * 30, "AREA DE UN CUADRADO", "=" * 30,"(Por favor ingrese floats)")
                base=float(input("Cual es la base?:"))
                altura= float(input("Cual es la altura?:"))
                print(f"Resultado:{base*altura}")
            elif sub_opcion_2 == 2:
                lado=float(input("Cual es el lado?:"))
                print(f"Resultado:{lado*4}")
            elif sub_opcion_2 == 3:
                break
    if opcion == 3:
        while True:
            print("=" * 30, "OPERACIONES CON RECTANGULO", "=" * 30)
            print("1) Area")
            print("2) Perimetro")
            print("3) Volver")
            sub_opcion_3= int(input("Seleccione su opcion (1-3):"))
            if sub_opcion_3 == 1:
                base=float(input("Cual es la base?:"))
                altura= float(input("Cual es la altura?:"))
                print(f"Resultado:{base*altura}")
            elif sub_opcion_3 == 2:
                lado_l=float(input("Cual es el lado largo?:"))
                lado_c=float(input("Cual es el lado corto?:"))
                print(f"Resultado:{(lado_c*2)+(lado_l*2)}")
            elif sub_opcion_3 == 3:
                break
    if opcion == 4:
        while True:
            print("=" * 30, "OPERACIONES CON CIRCULO", "=" * 30)
            print("1) Area")
            print("2) Perimetro/Circunferencia")
            print("3) Calcular Radio")
            print("4) Calcular diametro")
            print("5) Volver")
            
            sub_opcion_4= int(input("Seleccione su opcion (1-5):"))
            
            if sub_opcion_4 == 1:
                print("=" * 30, "AREA DE UN CIRCULO", "=" * 30,"(Por favor ingrese floats)")
                radio=float(input("Cual es el radio?:"))
                print(f"Resultado:{math.pi*(radio*radio)}")
            elif sub_opcion_4 == 2:
                lado_l=float(input("Cual es el lado largo?:"))
                lado_c=float(input("Cual es el lado corto?:"))
                print(f"Resultado:{(lado_c*2)+(lado_l*2)}")
            elif sub_opcion_4 == 3:
                print("=" * 30, "RADIO DE UN CIRCULO", "=" * 30,"(Por favor ingrese floats)")
                diametro=float(input("Cual es el diametro?:"))
                print(f"Resultado:{diametro/2}")
            elif sub_opcion_4 == 5:
                break












































































    if opcion == 10:
        print("=" * 30, "GOODBYE", "=" * 30)
        print("Gracias por usar esta calculadora :)")
        break