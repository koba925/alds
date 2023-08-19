class Tortoise:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


eruru = Tortoise("eruru", 100)
# eruru.name = "eruru"
# eruru.age = 100


print(f"{eruru.name} は {eruru.age} 歳です。")
