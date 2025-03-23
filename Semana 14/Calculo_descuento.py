    # Definimos la función

def calcular_descuento(total, descuento=30):
    descuento_aplicado = (total * descuento) / 100
    return descuento_aplicado  # Retorna el descuento aplicado


    # Monto total de la compra
monto_total = 1000

 # Primera llamada: Proporciona monto_total
    # Cálculo con el valor predeterminado de descuento
descuento_compra = calcular_descuento(monto_total)  # 30% de descuento
monto_final = monto_total - descuento_compra

    # Segunda llamada: Proporciona monto_total y un porcentaje de descuento
descuento_1 = 10  # Porcentaje de descuento
monto_total_descuento_1 = calcular_descuento(monto_total, descuento_1)  # Calcula con el parametro de descuento dado
monto_con_descuento_1 = monto_total - monto_total_descuento_1  # Monto con el descuento aplicado


    # Imprimir resultados
print("  ")
print("Monto total :" , monto_total)
print(f"Valor de descuento aplicado ({descuento_compra * 100 / monto_total}%): {descuento_compra}")
print("Monto final a pagar después de descuento", monto_final)

print("  ")

print("Monto total :" , monto_total)
print(f"Valor de descuento aplicado ({descuento_1}%): {monto_total_descuento_1}")
print("Monto final a pagar después de descuento", monto_con_descuento_1)