import sphere

radius = float(input("Введіть радіус кулі: "))

volume = sphere.volume_of_sphere(radius)
surface_area = sphere.surface_area_of_sphere(radius)

print("Об'єм кулі:", volume)
print("Площа поверхні кулі:", surface_area)
print("Імпорт завершено")
