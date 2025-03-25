# Temporary script to create Questions, Answers, QGroups for the test.
from hyiptest.models import Answer, QGroup, Question

# Questions + Answers for QGroup1
q = Question.objects.create(
    text="Обещает ли сайт быструю и гарантированную прибыль без рисков?"
)
a = Answer.objects.create(
    text="Да, прямо заявляют, что заработок гарантирован", bad_score=3, question=q
)
a = Answer.objects.create(
    text="Косвенно намекают на это, но без гарантий", bad_score=2, question=q
)
a = Answer.objects.create(text="Нет, таких заявлений нет", bad_score=0, question=q)

q = Question.objects.create(text="Как именно сайт объясняет способы заработка?")
a = Answer.objects.create(
    text="Четкое объяснение с примерами, документами и расчётами",
    bad_score=0,
    question=q,
)
a = Answer.objects.create(
    text='Общее описание типа "мы инвестируем за вас"', bad_score=2, question=q
)
a = Answer.objects.create(
    text="Нет объяснений, только обещания дохода", bad_score=3, question=q
)

q = Question.objects.create(text="Требует ли сайт предоплату или вложения?")
a = Answer.objects.create(
    text="Да, нужно вложить деньги сразу", bad_score=3, question=q
)
a = Answer.objects.create(
    text="Да, но обещают вернуть деньги в любой момент", bad_score=2, question=q
)
a = Answer.objects.create(
    text='Нет, но есть платные "премиум" услуги', bad_score=1, question=q
)
a = Answer.objects.create(text="Нет, всё бесплатно", bad_score=0, question=q)

q = Question.objects.create(
    text='Есть ли на сайте программа "Приведи друга", бонусы за привлечение людей?'
)
a = Answer.objects.create(
    text="Да, обещают деньги за привлечение новых пользователей",
    bad_score=3,
    question=q,
)
a = Answer.objects.create(
    text="Есть бонусы, но не связанные с деньгами (например, скидки)",
    bad_score=1,
    question=q,
)
a = Answer.objects.create(text="Нет", bad_score=0, question=q)

q = Question.objects.create(
    text="Можно ли легко вывести деньги с сайта? (по отзывам или личному опыту)"
)
a = Answer.objects.create(text="Да, вывод без проблем", bad_score=0, question=q)
a = Answer.objects.create(
    text="Есть задержки, но деньги выводят", bad_score=1, question=q
)
a = Answer.objects.create(
    text="Нет, много жалоб на блокировки аккаунтов, задержки", bad_score=3, question=q
)
a = Answer.objects.create(text="Неизвестно", bad_score=2, question=q)

q = Question.objects.create(text="Как давно существует сайт?")
a = Answer.objects.create(text="Менее 3 месяцев", bad_score=3, question=q)
a = Answer.objects.create(text="От 3 до 6 месяцев", bad_score=2, question=q)
a = Answer.objects.create(text="Более 6 месяцев", bad_score=0, question=q)
a = Answer.objects.create(text="Неизвестно", bad_score=1, question=q)

q = Question.objects.create(
    text=(
        "Есть ли у сайта реальные контактные данные"
        " (адрес, телефон, юридическая информация)?"
    )
)
a = Answer.objects.create(text="Да, и они проверяемы", bad_score=0, question=q)
a = Answer.objects.create(
    text="Есть, но вызывают сомнения (например, адрес ведёт в жилой дом)",
    bad_score=2,
    question=q,
)
a = Answer.objects.create(
    text="Нет, найти контакты невозможно", bad_score=3, question=q
)

q = Question.objects.create(
    text=(
        "Присутствуют ли на сайте логотипы известных компаний"
        " или рекомендации знаменитостей?"
    )
)
a = Answer.objects.create(
    text="Да, но без подтверждения (нет ссылок на первоисточник)",
    bad_score=2,
    question=q,
)
a = Answer.objects.create(text="Нет", bad_score=0, question=q)

q = Question.objects.create(
    text=(
        "Требует ли сайт паспортные данные, "
        "банковскую информацию без объяснения причин?"
    )
)
a = Answer.objects.create(text="Да, требуют сразу", bad_score=3, question=q)
a = Answer.objects.create(
    text="Да, но объясняют причину (например, верификация)", bad_score=1, question=q
)
a = Answer.objects.create(text="Нет", bad_score=0, question=q)

q = Question.objects.create(
    text=(
        "Найдены ли в интернете отзывы о том, "
        "что сайт – мошеннический или финансовая пирамида?"
    )
)
a = Answer.objects.create(
    text="Да, много жалоб на мошенничество", bad_score=5, question=q
)
a = Answer.objects.create(
    text="Есть некоторые негативные отзывы, но не доказано", bad_score=2, question=q
)
a = Answer.objects.create(
    text="Нет, отзывы в основном положительные", bad_score=0, question=q
)
a = Answer.objects.create(
    text="Немного или вообще нет отзывов", bad_score=3, question=q
)

# QGroup1
g = QGroup.objects.create(name="Опросник проверки безопасности сайта", fail_floor=11)

g.questions.set(Question.objects.all())

g.save()  # is it needed?; just in case
