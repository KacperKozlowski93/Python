n = int(input("Podaj liczbe cupcakes: "))

Number_of_full_boxes = n // 12
Number_of_leftover_cupcakes = n % 12
Partial_box = 1 if(Number_of_leftover_cupcakes > 0) else 0
Total_boxes_needed = Number_of_full_boxes + Partial_box


print(f" Liczba pełnych opakowań wynosi: {Number_of_full_boxes:.1f}")
print(f" Liczba pozostałych ciasteczek wynosi: {Number_of_leftover_cupcakes:.1f}")
print(f" Suma wszystkich opakowań wynosi: {Total_boxes_needed:.1f}")