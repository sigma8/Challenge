#from pkgutil import iter_modules
#from sre_constants import SRE_FLAG_MULTILINE


class Item:
    
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality
        


class GildegRose(Item):
    

    def __init__(self, Item):
        self.name = Item[0]
        self.sellIn = Item[1]
        self.quality = Item[2] 
    

    def updateQuality(self):
        # Aged Brie Item
        if self.name == 'Aged Brie':
            self.sellIn -= 1
            if self.quality < 50:
                self.quality += 1

        # Backstage passes Item
        elif self.name == 'Backstage passes':
            # item sellIn greater than 10 days sell by date
            if self.sellIn > 10:
                self.sellIn -= 1
                if self.quality < 50:
                    self.quality += 1
            # item sellIn passed sell by date
            elif self.sellIn < 0:
                self.sellIn -= 1
                self.quality = 0
            # item sellIn under than 5 days sell by date
            elif self.sellIn <= 5:
                self.sellIn -= 1
                if self.quality <= 47:
                    self.quality += 3
                elif self.quality > 47 and self.quality < 50:
                    self.quality = 50
            # item sellIn under than 10 days sell by date
            elif self.sellIn <= 10:
                self.sellIn -= 1
                if self.quality <= 48:
                    self.quality += 2
                elif self.quality > 48 and self.quality < 50:
                    self.quality = 50 
        
        # Sulfuras Item                
        elif self.name == 'Sulfuras':
            self.quality = 80
        
        # Conjura Item
        elif self.name == 'Conjure':
            self.sellIn -= 1
            if self.quality > 2:
                self.quality -= 2
            elif self.quality == 1:
                self.quality = 0
        
        # Any Other item
        else:
            self.sellIn -= 1
            if self.quality > 0:
                self.quality -= 1
        
        print(self.name, self.sellIn, self.quality)

    def display(self):
        print(self.name, self.sellIn, self.quality)



    
#items = [['Aged Brie', 12, 12], ['Backstage passes', 22, 22], ['Sulfura', 22, 80], ['Conjure', 20, 11]]

#for item in items:
#    newreview = GildegRose(item)
#    newreview.updateQuality()
 