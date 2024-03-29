class DB:
    __stock = [["+5 Dexterity Vest", 10, 20],
                    ["Aged Brie", 2, 0],
                    ["Elixir of the Mongoose", 5, 7],
                    ["Sulfuras, Hand of Ragnaros", 0, 80],
                    ["Sulfuras, Hand of Ragnaros", -1, 80],
                    ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
                    ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
                    ["Backstage passes to a TAFKAL80ETC concert", 5, 49],
                    ["Conjured Mana Cake", 3, 6]
    
                    ]
    @classmethod
    def stock(cls):
        return cls.__stock
    
    @classmethod
    def item(cls, name):
        stock = cls.stock()
        items = list(filter(lambda item: item[0] == name, stock))
        if items: return items[0]
        return []

    
