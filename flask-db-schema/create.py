from app import db, Users, Games

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
testgame = Games(game_name='FIFA 99',game_price=19.99) # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.add(testgame)
db.session.commit()