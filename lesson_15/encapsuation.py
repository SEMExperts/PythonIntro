"""
public - открытый класс
protected - можно получить доступ из класса потомка
private - данная часть класса полностью закрыта

"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.cpu = cpu
        self._memory = memory  # если одно подчеркивание то protected
        self.__hdd_volume = hdd    # два подчеркивания - private


    def get_hdd(self):
        return self.__hdd_volume


    def set_hdd(self, hdd):
        self.__hdd_volume = hdd

comp = Computer(2300, 16000, 500)
print(comp.cpu)
print(comp._memory)
print(comp.get_hdd())
print(dir(comp))