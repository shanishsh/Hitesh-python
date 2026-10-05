class Chai:
    def __init__(self, type_, strength) -> None:
        self.type = type_
        self.strength = strength

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         super().__init__(type_,strength)
#         self.spice_level = spice_level

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level) -> None:
#         Chai.__init__(type_, strength)
#         self.spice_level = spice_level

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level) -> None:
        super().__init__(type_, strength)
        self.spice_level = spice_level