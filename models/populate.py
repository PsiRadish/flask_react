
from fighter import *

connect('Ultimate_Showdown')

# class Move(EmbeddedDocument):
#     name = StringField(required=True)
#     attack_type = StringField(choices=('Strike', 'Throw', 'Evasive', 'Ranged', 'Misc.'), defaultsTo='Misc.')
#     input_seq = ListField(StringField(), required=True)

# class Fighter(Document):
#     name = StringField(required=True)
#     gender = StringField(required=True, choices=('female','male','other','robot'))
#     blood_type = StringField(defaultsTo="unknown")
#     img_src = URLField(default="https://www.iconexperience.com/_img/v_collection_png/256x256/shadow/hand_fist.png")
#     moves = EmbeddedDocumentListField(EmbeddedDocumentField(Move), required=True)

if len(Fighter.objects(name="Stephen Colbert")) == 0:
    colbert_move1 = \
    {
        'name': "Tip of the Hat",
        'attack_type': "Evasive",
        'input_seq': ['↞', 'G']
    }
    colbert_move2 = \
    {
        'name': "Wag of the Finger",
        'attack_type': "Throw",
        'input_seq': ['↔','↔','B+D']
    }
    colbert_move3 = \
    {
        'name': "Go For the Eyes, America",
        'attack_type': "Ranged",
        'input_seq': ['Hold ← (2 sec)','→','A']
    }
    Stephen_Colbert = Fighter(name="Stephen Colbert",
                              gender="male",
                              blood_type="Red, white, and blue",
                              img_src="http://www.chicagonow.com/newsboy/files/2015/09/838-495_StephenColbert.jpg",
                              moves=[Move(**colbert_move1), Move(**colbert_move2), Move(**colbert_move3)])
    Stephen_Colbert.save()

if len(Fighter.objects(name="Emily Dickinson")) == 0:
    dickinson_move1 = \
    {
        'name': "Pride",
        'attack_type': "Strike",
        'input_seq': ['↠', 'D']
    }
    dickinson_move2 = \
    {
        'name': "Prejudice",
        'attack_type': "Throw",
        'input_seq': ['↻', 'C+D']
    }
    Emily_Dickinson = Fighter(name="Emily Dickinson",
                              gender="female",
                              # blood_type="",
                              img_src="http://www.poets.org/sites/default/files/styles/286x289/public/images/biographies/155_EmilyDickinsonSmall.jpg?itok=cQkQwNTK",
                              moves=[Move(**dickinson_move1), Move(**dickinson_move2)])
    Emily_Dickinson.save()


"""
move = \
{
    'name': "",
    'attack_type': "",
    'input_seq': ['', '']
}
"""
