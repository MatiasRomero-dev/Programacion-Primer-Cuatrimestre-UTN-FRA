tipo_vehiculo = input("ingresa el tipo de vehiculo (automovil, motocicleta, camion): ")
kilometraje = int(input("Ingresa el kilometraje acumulado en el vehiculo: "))

if tipo_vehiculo == "automovil":
    if kilometraje < 10000:
        mantenimiento = "mantenimiento basico"
elif kilometraje <= 50000:
        mantenimiento = "mantenimiento preventivo"
else:
        mantenimiento = "mantenimiento general"

print(mantenimiento)