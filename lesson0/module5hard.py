# Свой YouTube

class UrTube:
    """
    Класс проигрывателя, содержащий атрибуты:
    users (список объектов User),
    videos (список объектов Video),
    current_user (текущий пользователь, User)
    """
#    videos = Video()
    def __init__(self):
        self.users = []
        self.videos = []
#        self.current_user = current_user

    def log_in(self, nickname, password):
        pass
#Метод log_in,
#который принимает на вход аргументы: nickname, password
#и пытается найти пользователя в users с такими же логином и паролем.
#Если такой пользователь существует, то current_user меняется на найденного.
#Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
#        for u in self.users:
#            print(u.nickname)
#            if u.nickname != nickname:
        self.users.append(user)
        for u in self.users:
            print(u.nickname)

    #            else:
#                print('АЛЯРМА!!!!!!')
#        for u in UrTube.users:
#            if nickname == u.nickname:
#                print(f'Пользователь {nickname} уже существует')
#            else:
#                user.log_in(nickname, password)


    #Метод register,
#который принимает три аргумента: nickname, password, age,
#и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
#Если существует, выводит на экран: "Пользователь {nickname} уже существует".
#После регистрации, вход выполняется автоматически.

    def log_out(self):
        pass
#Метод log_out для сброса текущего пользователя на None

    def add(self, *args):
        for v in args:
#            print(v.title)
            for vv in self.videos:
                print(vv.title)
                if v.title != vv.title:
                    self.videos.append(v)
                else:
                    print('ЕСТЬ СОВПАДЕНИЯ НАЗВАНИЙ')

#        print(*args)
#Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
#если с таким же названием видео ещё не существует.
#В противном случае ничего не происходит.

    def get_videos(self, video_name):
        pass
#Метод get_videos,
#который принимает поисковое слово
#и возвращает список названий всех видео, содержащих поисковое слово.
#Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

    def watch_video(self):
        pass
#Метод watch_video,
#который принимает название фильма,
#если не находит точного совпадения (вплоть до пробела),
#то ничего не воспроизводится,
#если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
#После текущее время просмотра данного видео сбрасывается.


class Video:
    """
    Класс видео, содержащий атрибуты:
    title (заголовок, строка),
    duration (продолжительность, секунды),
    time_now (секунда остановки (изначально 0)),
    adult_mode (ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

#    def pt(self):
#        for i in Video:
#            print(i)
#        print(self)
class User:
    """
    Класс пользователя, содержащий атрибуты:
    nickname (имя пользователя, строка),
    password (в хэшированном виде, число),
    age (возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash((self.password))



if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    v3 = Video('Для чего девушкам парень программист?', 30)

    # Добавление видео
    ur.add(v1, v2, v3)
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)


#    user = User(nickname, password, age)
#    name = "Shubham"
#    hash1 = hash(name)
#    hash2 = hash(name)
#    print("Hash 1: %s" % hash1)
#    print("Hash 2: %s" % hash2)



