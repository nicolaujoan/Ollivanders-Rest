class GildedRose(object):

    def __init__(self, stock):
        self.stock = stock  # GildedRose has-a stock

    def updateQuality(self):
        for item in self.stock:
            item.updateQuality()

    def add_item(self):
        pass


# this class cannot be modified ( kata rules !!! )
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# our informal interface
class Updateable:
    def updateQuality(self) -> None:
        """Update the quality of an item"""
        pass


class NormalItem(Item, Updateable):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def getQuality(self) -> int:
        return self.quality

    def getSellIn(self) -> int:
        return self.sell_in

    def decreaseQuality(self, decrement):
        self.quality -= decrement

    def decreaseSellIn(self):
        self.sell_in -= 1

    def updateQuality(self):
        if self.getSellIn() <= 0 and self.getQuality() > 1:
            self.decreaseQuality(2)

        if self.getSellIn() > 0 and self.getQuality() > 0:
            self.decreaseQuality(1)

        self.decreaseSellIn()


class Sulfuras(Item, Updateable):
    QUALITY = 80

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, Sulfuras.QUALITY)


# inherits from NormalItem because its behaviour is similar (can reuse methods)
class Conjured(NormalItem, Updateable):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def updateQuality(self):
        if self.getSellIn() < 0 and self.getQuality() == 1:
            self.decreaseQuality(1)

        if self.getSellIn() <= 0 and self.getQuality() > 1:
            self.decreaseQuality(2)

        if self.getSellIn() > 0 and self.getQuality() > 0:
            self.decreaseQuality(1)

        self.decreaseSellIn()


class AgedBrie(Item, Updateable):
    MAX_QUALITY = 50

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def getQuality(self) -> int:
        return self.quality

    def increaseQuality(self, increment):
        self.quality += increment

    def getSellIn(self) -> int:
        return self.sell_in

    def decreaseSellIn(self):
        self.sell_in -= 1

    def updateQuality(self):
        if self.getQuality() < AgedBrie.MAX_QUALITY and self.getSellIn() > 0:
            self.increaseQuality(1)

        if self.getQuality() < AgedBrie.MAX_QUALITY and self.getSellIn() <= 0:
            self.increaseQuality(2)

        self.decreaseSellIn()


class BackstagePass(Item, Updateable):
    MAX_QUALITY = 50

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def getQuality(self) -> int:
        return self.quality

    def increaseQuality(self, increment):
        self.quality += increment

    def decreaseQuality(self, decrement):
        self.quality -= decrement

    def getSellIn(self) -> int:
        return self.sell_in

    def decreaseSellIn(self, decrement):
        self.sell_in -= decrement

    def updateQuality(self):
        if self.getSellIn() <= 0 and self.getQuality() >= 0:
            self.decreaseQuality(self.getQuality())

        elif self.getSellIn() <= 5 and self.getQuality() < (BackstagePass.MAX_QUALITY - 2):
            self.increaseQuality(3)

        elif self.getSellIn() <= 10 and self.getQuality() < (BackstagePass.MAX_QUALITY - 1):
            self.increaseQuality(2)

        else:
            self.increaseQuality(1)

        self.decreaseSellIn(1)
