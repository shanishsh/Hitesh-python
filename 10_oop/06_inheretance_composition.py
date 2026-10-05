class BaseChai:
    def __init__(self,type_) -> None:
        self.type = type_


    def prepare(self):
        print(f"Preparing {self.type} chai....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

#composition
class ChaiShop:
    chai_cls = BaseChai

    def __init__(self) -> None:
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()

shop.serve()