
class player:
    def __init__(self):
        self.cards=[]
        self.score=0
        self.x=0
        self.y=0
        self.status=""

    def add_card(self,card):
        self.cards.append(card)
        card.asign_value()
        print(card.value)
        aux=0
        aux = self.score+card.value
        print(aux)
        if aux > 21:
            for card in self.cards:
                if card.name == "AS" and not card.value == 1:
                    card.value = 1
        self.score=sum([x.value for x in self.cards])
        print(f"Score:{self.score}")
        card.x=self.x
        card.y=self.y

    def show_card(self):
        for card in self.cards:
            card.draw_card()
