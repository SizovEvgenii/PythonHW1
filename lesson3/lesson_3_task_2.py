from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy 5", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 5", "+79345678901"),
    Smartphone("Huawei", "1245", "+79456789012"),
    Smartphone("Google", "Pixel 1touch", "+79567890123")
]
for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. {smartphone.phone_number}.")