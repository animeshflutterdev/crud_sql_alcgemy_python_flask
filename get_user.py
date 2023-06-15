from main import User, Session, engine
# from create_users import local_session

local_session = Session(bind=engine)

## Get all users
# users = local_session.query(User).all()

# for user in users:
    # print('get-all-User', user.userName)

user = local_session.query(User).filter(User.userName =='Animesh').first()

print('animesh data = ',user)