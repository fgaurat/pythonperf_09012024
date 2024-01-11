from UserDAO import UserDAO



def filter_male(gen):

    for u in gen:
        if u.gender == "Male":
            yield u
    


def main():
    u = UserDAO("./tp08/formation.db")

    
    with UserDAO("./tp08/formation.db") as dao:
    
        users_gen = dao.findAll()
        male_users = filter_male(users_gen)
        for u in male_users:
            raise Exception("Erreur")
            print(u)

        # u = next(gen)
        # print(u)
        # u = next(gen)
        # print(u)

        # for u in gen:
        #     print(u)

        # l = list(dao.findAll())

        # for user in dao.findAll():
        #     print(user) # User name:, first.... 


        # dao2 = UserDAO("./tp08/formation.db")
        # for user in dao2.findAll():
        #     print("dao2",user) # User name:, first.... 

if __name__ == '__main__':
    main()