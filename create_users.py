from main import User, Session, engine

local_session = Session(bind=engine)

## Add single user
new_user = User(userName='Animesh001',email='aaa2a@gmail.com',)

local_session.add(new_user)

local_session.commit()


## Add multiple user
# users = [
#     {'userName':'ani','email':'maiL@d.ck'},
#     {'userName':'anim','email':'maiL1@d.ck'},
#     {'userName':'anime','email':'maiL11@d.ck'},
#     {'userName':'animesh','email':'maiL11@d.ck'},
# ]

# for user in users:
#     new_user = User(userName= user['userName'],email= user['email'])
#     local_session.add(new_user)
#     local_session.commit()
