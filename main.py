class Member:

  def __init__(self, name, clan):
    self.name = name
    self.clan = clan

  def details(self):
    print(f"{self.name} is a part of {self.clan}")

  @classmethod
  def fromstr(cls, str):
    return cls(str.split("-")[0], str.split("-")[1])


m = Member("Tahmid", "Fighter")
m.details()

new = ("Ahmad-Choton")
m2 = Member.fromstr(new)
m2.details()