from main import User, Session, engine


local_session = Session(bind=engine)


user_to_update = local_session.query(User).filter(User.userName =='Animesh').first()

user_to_update.userName = 'Parv'
user_to_update.email = 'Parv@email.xo'

local_session.commit()