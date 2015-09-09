from mongoengine import *

class Move(EmbeddedDocument):
    name = StringField(required=True)
    attack_type = StringField(choices=('Strike', 'Throw', 'Evasive', 'Ranged', 'Misc.'), default='Misc.')
    input_seq = ListField(StringField(), required=True)
    
    def __unicode__(self):
        return '\n'.join([self.name, self.attack_type, ', '.join(self.input_seq)])

class Fighter(Document):
    name = StringField(required=True)
    gender = StringField(required=True, choices=('female','male','other','robot'))
    blood_type = StringField(default="unknown")
    img_src = URLField(default="https://www.iconexperience.com/_img/v_collection_png/256x256/shadow/hand_fist.png")
    moves = EmbeddedDocumentListField(Move, required=True)
    
    def __unicode__(self):
        return '\n'.join([self.name, self.gender, self.blood_type, self.img_src, '\n'.join([ str(move) for move in self.moves ])])
