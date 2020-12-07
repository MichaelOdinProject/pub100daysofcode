# list of fruit/veg but separated into fruit - veg
# nested lists

not_a_veg_list_yet = "Spinach Kale Celery Potatoes"
not_a_fruit_list_yet = "Strawberries Nectarines Apples Grapes Peaches Cherries Pears Tomatoes"
veg_list = not_a_veg_list_yet.split(" ")
fruit_list = not_a_fruit_list_yet.split(" ")

dirty_dozen = [veg_list, fruit_list]
print(dirty_dozen)
