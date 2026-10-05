class TeaLeaf:

    def __init__(self, age) -> None:
        self._age = age

    @property
    def age(self):
        return self._age +2

    @age.setter
    def age(self, age):
        if age>=1 and age<=5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")

leaf = TeaLeaf(2)

print(leaf.age)

leaf.age = 4

print(leaf.age)

leaf.age = 6

print(leaf.age)

