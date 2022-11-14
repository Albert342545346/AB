class Situation:
    def __init__(self):
        self.description = ""
        self.ways = dict()
        self.name = ""


situations = dict()
start = Situation()
start.description = "Вы проснулись у себя в квартире."
start.ways["Пропуск"] = "Вы остаетесь дома."
start.ways["Рутина"] = "Вы как обычно преподаете в школе."
start.ways["Бессонница"] = "Вы не спали ночью."
start.ways["Атака"] = "Машины восстали против человечества."
start.ways["Новая жизнь"] = "Вы переехали в Париж."
start.ways["Шаурмечная"] = "Вы открыли свою шаурмечную."
start.ways["Арест"] = "Вас арестовали за эксплуатацию детского труда. Заявление на вас оставили ученики 10 А класса."
start.ways["Сон"] = "Оказалось, что ваша жизнь это сон, начиная с 2006."
start.ways["Двуличие"] = "В вас проснулась вторая личность."
start.name = "Старт"
situations[start.name] = start

dismissal = Situation()
dismissal.description = "Вы не поднимаете трубки и не выходите на улицу больше недели."
dismissal.ways["Увольнение"] = "Начальству это надоело и вас уволили."
dismissal.name = "Пропуск"
situations[dismissal.name] = dismissal


routine = Situation()
routine.description = "Вы общаетесь с другими преподавателями и учениками."
routine.ways["Будни"] = "Так вы проживаете до глубокой старости."
routine.name = "Рутина"
situations[routine.name] = routine

insomnia = Situation()
insomnia.description = "Вы не спали ночью и у вас плохое настроение плохого настроения."
insomnia.ways["Гнев"] = "В добавок к этому ученики сломали принтер, вы бесились и кричали на учеников.\nИз за них вы не получили зарплату за прошедщий месяц."
insomnia.ways["Ненависть"] = "По этой причине вы выставляете всем плохие оценки.\nДети начинают негодовать и жалуются классным руководителям."
insomnia.name = "Бессонница"
situations[insomnia.name] = insomnia

hero = Situation()
hero.ways["Герой"] = "Вы смогли в одиночку одолеть их и стали известны на весь мир."
hero.ways["Страх"] = "Вы струсили и чтобы пережить их ношествие спрятались в подвале."
hero.name = "Атака"
situations[hero.name] = hero

new_life = Situation()
new_life.description = "Сделали вы это, чтобы Исупов Матвей не смог вас достать."
new_life.ways["Будущее"] = "Там вы уже через несколько лет стали известны и Матвей Исупов вас нашел."
new_life.ways["Стратегия"] = "Вы решили усмирить его, сказав, что поставите ему 2 в полугодие, если он не успокоится."
new_life.name = "Новая жизнь"
situations[new_life.name] = new_life

shawarmechnaya = Situation()
shawarmechnaya.description = "Дело начало набирать абороты"
shawarmechnaya.ways["Торговля"] = "Через два года вы открыли уже 5 шаурмечных. После чего решили отрыть завод по производству сладостей."
shawarmechnaya.name = "Шаурмечная"
situations[shawarmechnaya.name] = shawarmechnaya

arrest = Situation()
arrest.description = "В суде вам вынесли приговор.(15 лет)"
arrest.ways["Проблемы"] = "Уже через пару лет вы сошли с ума. Купив оборудование для побега и подкупив охранника, ровно в полночь вы выбрались из тюрьмы. Позже вы узнаете из за кого вы попали сюда. И начнете мстить. А как именно это уже другая история..."
arrest.ways["Тюрьма"] = "Вы купили себе шаурму сразу после выхода из тюрьмы."
arrest.name = "Арест"
situations[arrest.name] = arrest

sleep = Situation()
sleep.description = "Вы решили не идти на учителя."
sleep.ways["Осознание"] = "Вы решили податься в компанию. Там вы стали миллиардером, попав в топ 3 богатейщих людей на планете"
sleep.name = "Сон"
situations[sleep.name] = sleep

duplicity = Situation()
duplicity.description = "Ваша вторая личность решила ограбить банк."
duplicity.ways["Последствия"] = "Все сложилось неудачно. Началась перестрелка в которой вас подстрелили и вы не смогли понять в чем смысл жизни."
duplicity.name = "Двуличие"
situations[duplicity.name] = duplicity


current_situation = situations["Старт"]
while True:
    print(current_situation.description)
    for k, v in current_situation.ways.items():
        print(k, v)
    choice = input()
    current_situation = situations[choice]
    if len(current_situation.ways) == 0:
        break
print(current_situation.description)