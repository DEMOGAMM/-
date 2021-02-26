#####создаем класс game
class game:
    #создаем атрибуты класса
    name="cs 1.6"
    model="шутер"
    founded="1996"
    #создаем методы класса
    def start(self):
        print ("запуск игры cs1.6")
    def maps (self):
        print("запуск карты dust 2")

    def stop(self):
        print("выход из игры cs1.6")


game_a=game()
game_b=game()
game_a.start()
game_a.maps()
game_b.stop()
