# Temporary script to create models for the test.
from hyiptest.models import Answer, QGroup, Question

q = Question.objects.create(text="Какова цель сайта?")
a = Answer.objects.create(
    text="Инвестирование или получение дохода", bad_score=2, question=q
)
a = Answer.objects.create(
    text="Продажа товаров/услуг / Информационный ресурс", bad_score=0, question=q
)

q = Question.objects.create(text="Требует ли вложений?")
a = Answer.objects.create(
    text="Да, без вложений пользоваться нельзя", bad_score=3, question=q
)
a = Answer.objects.create(text="Да, но не обязательно", bad_score=1, question=q)
a = Answer.objects.create(text="Нет", bad_score=0, question=q)

q = Question.objects.create(text="Обещаемая доходность")
a = Answer.objects.create(text="До 10% в месяц", bad_score=1, question=q)
a = Answer.objects.create(text="10-30% в месяц", bad_score=3, question=q)
a = Answer.objects.create(text="Более 30% в месяц", bad_score=5, question=q)
a = Answer.objects.create(text="Доходность не указана", bad_score=0, question=q)

q = Question.objects.create(text="Юридическая информация о компании")
a = Answer.objects.create(text="Есть регистрация и лицензии", bad_score=0, question=q)
a = Answer.objects.create(text="Указаны только контакты", bad_score=2, question=q)
a = Answer.objects.create(text="Нет информации", bad_score=5, question=q)

q = Question.objects.create(text="Способы оплаты")
a = Answer.objects.create(text="Банковская карта", bad_score=1, question=q)
a = Answer.objects.create(text="Криптовалюта", bad_score=3, question=q)
a = Answer.objects.create(text="Электронные кошельки", bad_score=2, question=q)

q = Question.objects.create(text="Реферальная система")
a = Answer.objects.create(
    text="Основной доход за счёт привлечения людей", bad_score=5, question=q
)
a = Answer.objects.create(text="Есть, но не главное", bad_score=2, question=q)
a = Answer.objects.create(text="Нет", bad_score=0, question=q)

q = Question.objects.create(text="Возраст сайта")
a = Answer.objects.create(text="Менее 1 месяца", bad_score=5, question=q)
a = Answer.objects.create(text="От 1 до 6 месяцев", bad_score=3, question=q)
a = Answer.objects.create(text="Более 1 года", bad_score=0, question=q)

q = Question.objects.create(text="Реклама сайта")
a = Answer.objects.create(text="Через таргетированную рекламу", bad_score=0, question=q)
a = Answer.objects.create(
    text="Через спам-рассылки / подозрительные Telegram-чаты", bad_score=4, question=q
)
a = Answer.objects.create(
    text="Через личные сообщения и навязчивые предложения", bad_score=5, question=q
)

q = Question.objects.create(text="Что требует сайт?")
a = Answer.objects.create(text="Оставить контактные данные", bad_score=2, question=q)
a = Answer.objects.create(text="Внести предоплату", bad_score=5, question=q)
a = Answer.objects.create(text="Поделиться сайтом для бонусов", bad_score=3, question=q)
a = Answer.objects.create(text="Просто зарегистрироваться", bad_score=0, question=q)

g = QGroup.objects.create(name="Тест на мошенников")

g.questions.set(Question.objects.all())

g.save()  # is it needed?; just in case
