# Temporary script to create Questions, Answers, QGroups for the test.
from hyiptest.models import Answer, QGroup, Question

# Questions + Answers for QGroup1
q = Question.objects.create(
    text="Обещает ли сайт быструю и гарантированную прибыль без рисков?"
)
a = Answer.objects.create(
    text="Да, прямо заявляют, что заработок гарантирован", risk_score=3, question=q
)
a = Answer.objects.create(
    text="Косвенно намекают на это, но без гарантий", risk_score=2, question=q
)
a = Answer.objects.create(text="Нет, таких заявлений нет", risk_score=0, question=q)

q = Question.objects.create(text="Как именно сайт объясняет способы заработка?")
a = Answer.objects.create(
    text="Четкое объяснение с примерами, документами и расчётами",
    risk_score=0,
    question=q,
)
a = Answer.objects.create(
    text='Общее описание типа "мы инвестируем за вас"', risk_score=2, question=q
)
a = Answer.objects.create(
    text="Нет объяснений, только обещания дохода", risk_score=3, question=q
)

q = Question.objects.create(text="Требует ли сайт предоплату или вложения?")
a = Answer.objects.create(
    text="Да, нужно вложить деньги сразу", risk_score=3, question=q
)
a = Answer.objects.create(
    text="Да, но обещают вернуть деньги в любой момент", risk_score=2, question=q
)
a = Answer.objects.create(
    text='Нет, но есть платные "премиум" услуги', risk_score=1, question=q
)
a = Answer.objects.create(text="Нет, всё бесплатно", risk_score=0, question=q)

q = Question.objects.create(
    text='Есть ли на сайте программа "Приведи друга", бонусы за привлечение людей?'
)
a = Answer.objects.create(
    text="Да, обещают деньги за привлечение новых пользователей",
    risk_score=3,
    question=q,
)
a = Answer.objects.create(
    text="Есть бонусы, но не связанные с деньгами (например, скидки)",
    risk_score=1,
    question=q,
)
a = Answer.objects.create(text="Нет", risk_score=0, question=q)

q = Question.objects.create(
    text="Можно ли легко вывести деньги с сайта? (по отзывам или личному опыту)"
)
a = Answer.objects.create(text="Да, вывод без проблем", risk_score=0, question=q)
a = Answer.objects.create(
    text="Есть задержки, но деньги выводят", risk_score=1, question=q
)
a = Answer.objects.create(
    text="Нет, много жалоб на блокировки аккаунтов, задержки", risk_score=3, question=q
)
a = Answer.objects.create(text="Неизвестно", risk_score=2, question=q)

q = Question.objects.create(text="Как давно существует сайт?")
a = Answer.objects.create(text="Менее 3 месяцев", risk_score=3, question=q)
a = Answer.objects.create(text="От 3 до 6 месяцев", risk_score=2, question=q)
a = Answer.objects.create(text="Более 6 месяцев", risk_score=0, question=q)
a = Answer.objects.create(text="Неизвестно", risk_score=1, question=q)

q = Question.objects.create(
    text=(
        "Есть ли у сайта реальные контактные данные"
        " (адрес, телефон, юридическая информация)?"
    )
)
a = Answer.objects.create(text="Да, и они проверяемы", risk_score=0, question=q)
a = Answer.objects.create(
    text="Есть, но вызывают сомнения (например, адрес ведёт в жилой дом)",
    risk_score=2,
    question=q,
)
a = Answer.objects.create(
    text="Нет, найти контакты невозможно", risk_score=3, question=q
)

q = Question.objects.create(
    text="Присутствуют ли на сайте логотипы или упоминания известных компаний?"
)
a = Answer.objects.create(
    text="Да, но без подтверждения (нет ссылок на первоисточник)",
    risk_score=2,
    question=q,
)
a = Answer.objects.create(text="Нет", risk_score=0, question=q)

q = Question.objects.create(
    text=(
        "Требует ли сайт паспортные данные,"
        " банковскую информацию или другие документы удостоверяющие личность?"
    )
)
a = Answer.objects.create(text="Да, требуют сразу", risk_score=3, question=q)
a = Answer.objects.create(
    text="Да, но объясняют причину (например, верификация)", risk_score=1, question=q
)
a = Answer.objects.create(text="Нет", risk_score=0, question=q)

q = Question.objects.create(text="Найдены ли в интернете какие-либо отзывы о сайте?")
a = Answer.objects.create(
    text="Да, много жалоб на мошенничество", risk_score=5, question=q
)
a = Answer.objects.create(
    text="Есть некоторые негативные отзывы", risk_score=2, question=q
)
a = Answer.objects.create(
    text="Да, отзывы в основном положительные", risk_score=0, question=q
)
a = Answer.objects.create(
    text="Немного или вообще нет отзывов", risk_score=3, question=q
)

# QGroup1
g = QGroup.objects.create(
    name="Опросник проверки безопасности сайта",
    risk_fail_trigger=11,
    risk_suspicious_trigger=6,
)

g.questions.set(Question.objects.all())

g.save()  # is it needed?; just in case
