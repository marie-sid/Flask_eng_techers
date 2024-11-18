goals = {"travel": "⛱ Для путешествий", "study": "🏫 Для учебы", "work": "🏢 Для работы", "relocate": "🚜 Для переезда",
         "programming": "⌨️ Для программирования"}

teachers = [

    {
        "id": 0,
        "name": "Профессор Мяуислав Ушаков",
        "about": "Репетитор американского английского языка. Структурированная система обучения. Всем привет! Я "
                 "предпочитаю называть себя «тренером» английского языка. Мои занятия похожи на тренировки",
        "rating": 4.2,
        "picture": "/static/cat_1.jfif",
        "price": 900,
        "goals": ["travel", "relocate", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": True, "12:00": True, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "tue": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "wed": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "thu": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "fri": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": False},
        }
    },
    {
        "id": 1,
        "name": "Кошаченко Мурка Мурзовна",
        "about": "Я носитель языка и репетитор по разговорной речи, дающий частные уроки разговорной речи на английском языке с использованием "
                 "того, что называется Life Learning. Этот метод позволяет ученикам полностью контролировать, как и что "
                 "они изучают. Это обучение под руководством учеников, сосредоточенное на интересах, жизненных целях, удовольствии и эффективном "
                 "обучении для вас, как личности. Перестаньте тратить время на учебники, тесты и ненужное "
                 "давление. Найдите любовь к изучению и разговору на английском языке с креативностью и свободой. Уроки "
                 "выбираются полностью вами, чтобы поддерживать вашу мотивацию и стремление к достижению ваших целей.",
        "rating": 4.8,
        "picture": "/static/cat_2.jfif",
        "price": 1200,
        "goals": ["relocate", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 2,
        "name": "Пухляков Феликс Викторович",
        "about": "Английский язык стал языком мира, поэтому его считают мировым языком"
                 "Сегодня английский язык, похоже, развивается в будущий глобальный язык, как показывает его распространение в Интернете в последние "
                 "годы (почти 80% страниц всемирной паутины теперь написаны на английском языке). научные "
                 "исследователи обнаружили, что на самом деле многие малые языки уже исчезли. Но чтобы преподавать его "
                 "удовлетворительным образом, требуется хороший учитель английского языка. Хороший учитель английского языка должен "
                 "обладать некоторыми качествами. Деловой, общий и разговорный английский",
        "picture": "/static/cat_3.jfif",
        "rating": 4.7,
        "price": 1300,
        "goals": ["work"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "tue": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 3,
        "name": "Котова Киса Витальевна",
        "about": "У меня широкий круг интересов, поверьте, вам никогда не будет скучно на наших занятиях. Я работал "
                 "с юристами, врачами, биологами и многими другими, чтобы помочь им улучшить свой английский в их "
                 "соответствующих областях. Поскольку я всю жизнь удовлетворял свое любопытство, я приобрел огромный "
                 "словарный запас, который я могу передать вам.",
        "picture": "/static/cat_4.jfif",
        "rating": 4.9,
        "price": 1300,
        "goals": ["travel", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 4,
        "name": "Пушистик Виталина Ушастовна",
        "about": "Здравствуйте! Я носитель русского языка и свободно владею "
                 "английским. Преподаю онлайн уже 3 года. У меня индивидуальная программа, изучив "
                 "ваши требования, я составляю спец. программу. план, а значит и дело) Книги Кембридж, "
                 "Оксфорд и т. д. Тренирую и развиваю разговорную речь. Изучаем слова, устойчивые сочетания и применяем "
                 "их на практике. Говорим и пытаемся говорить :) на разные темы. Слушаем аудиоуроки, "
                 "смотрим фильмы с субтитрами. Разбираем все по полочкам :) Параллельно, конечно, "
                 "изучаем основы грамматики и правильную подачу предложений :) Все материалы "
                 "предоставляю я. Обещаю, что вы заговорите с первого занятия :)",
        "picture": "/static/cat_5.jfif",
        "rating": 4.3,
        "price": 900,
        "goals": ["travel"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 5,
        "name": "Котик Киса Владмировна",
        "about": "Здравствуйте! Меня зовут Ян, и я преподаю английский язык уже более пяти лет. Часть этого времени я "
                 "провел в Китае, где работал со студентами от 3 до 40 лет. Я работаю как со взрослыми, так и с детьми. Но для "
                 "всех возрастов я стараюсь сделать свои занятия интересными и интерактивными. Преподавание английского языка для "
                 "меня — это не просто урок языка. Я всегда стараюсь привлекать более широкий культурный и исторический контекст, "
                 "который помогает моим студентам лучше понять язык и его особенности. Степень по истории очень помогает мне "
                 " создавать такую интеллектуальную среду в классе. Для каждого студента я разрабатываю индивидуальную учебную "
                 "программу, которая зависит от его целей и потребностей.",
        "picture": "/static/cat_6.jfif",
        "rating": 3.9,
        "price": 800,
        "goals": ["travel", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 6,
        "name": "Хвостик Снежинка Олеговна",
        "about": "Здравствуйте, я дружелюбный носитель английского языка. Я опытный преподаватель "
                 "английского языка с нейтральным акцентом, который легко понять. Это потому, что я вырос, живя в "
                 "13 странах на 4 континентах. Среди них Англия, Америка, Австралия и Япония. В настоящее время, "
                 "я живу в Лиссабоне, Португалия. Хотя я в основном сосредоточен на индивидуальном обучении, ранее я преподавал "
                 "занятия с 50 учениками одновременно. Мои ученики были в возрасте от 12 до 70 лет. "
                 "От израильских школьников средней школы до тайских правительственных чиновников. В результате, "
                 "я изучил широкий спектр методов обучения. В настоящее время я беру учеников с уровнем английского: "
                 "B2 и выше, а также тех, кто заинтересован в долгосрочном развитии и множественных уроках. Я "
                 "понимаю, как сложно может быть выучить другой язык. Вот почему мой стиль преподавания веселый, "
                 "конструктивный и легкий. Уроки будут подобраны с учетом ваших потребностей и целей. Благодаря моим урокам, "
                 "вы обретете уверенность в том, что сможете говорить по-английски в повседневной жизни.",
        "picture": "/static/cat_7.jfif",
        "rating": 4.5,
        "price": 1200,
        "goals": ["travel", "relocate", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 7,
        "name": "Котякова Муся Евгеньевна",
        "about": "Мои уроки увлекательны и практичны, но самое главное, мы будем чрезвычайно продуктивны. Я "
                 "считаю, что лучший способ овладеть английским языком — это ВЫПОЛНЕНИЕ. Меньше теории, больше практики. Много "
                 "практики. Наша цель — достичь максимальной вовлеченности и сосредоточиться на предмете. Школы приучили "
                 "нас быть очень пассивными. Сидеть тихо в одиночестве, слушать лекции, просто поглощать информацию. ЭТО не то, как мы собираемся изучать английский язык.",
        "picture": "/static/cat_8.jfif",
        "rating": 4.5,
        "price": 1100,
        "goals": ["study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 8,
        "name": "Лапочкина Нюша Денисовна",
        "about": "Привет! Я из Лондона в Соединенном Королевстве, но сейчас живу в Японии. "
                 "У меня есть сертификат TEFL, который я получил в прошлом году. После переезда в Японию я преподаю "
                 "английский язык некоторым своим японским друзьям. Я считаю, что обучение должно быть веселым и "
                 "увлекательным, и хотя английский язык может быть сложным для изучения, я стремлюсь сделать его "
                 "приятным. Мне нравится смотреть футбол и путешествовать. Я много занимаюсь йогой в свободное время и "
                 "с нетерпением жду встречи с вами!",
        "picture": "/static/cat_9.jfif",
        "rating": 5,
        "price": 1700,
        "goals": ["relocate", "work", "programming"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 9,
        "name": "Мяучкин Барсик Артемович",
        "about": "Привет и добро пожаловать в мой профиль для изучающих прекрасный мир английского языка! Я "
                 "сертифицированный преподаватель-носитель английского языка с оценкой A по TOEFL. Изучение чего-то нового должно быть веселым и "
                 "захватывающим, а не тем, что вы тянете с места, поэтому я считаю, что немного веселья "
                 "и юмора играют огромную роль в процессе обучения, а также в развитии здоровых и "
                 "приятных отношений между нами. Я также сейчас пытаюсь выучить новый язык, и поэтому я знаю "
                 "по собственному опыту, насколько это может быть пугающе или иногда сложно, но, пожалуйста, помните, что я здесь, "
                 "чтобы работать с вами, а не против вас. Мы можем вместе работать над произношением, чтением, "
                 "разговорным английским, домашним заданием, которое у вас может быть в школе или колледже, сленгом, по сути, над любым предметом, "
                 "в области, которая вам нравится или которую вы хотите развивать, когда вы наслаждаетесь процессом обучения, который вы изучаете, "
                 "даже не осознавая этого",
        "picture": "/static/cat_10.jfif",
        "rating": 4.1,
        "price": 1200,
        "goals": ["work", "programming"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 10,
        "name": "Академик Пушистик Котович",
        "about": "Я мотивирую и направляю студентов к достижению их целей. Это зависит от того, с какой проблемой они "
                 "сталкиваются. Иногда они просто хотят попрактиковаться в разговоре, чтобы улучшить свою беглость. Иногда это более "
                 "сложно, например, из-за языкового барьера, и мне нужно повысить их уверенность. Некоторые приходят с "
                 "конкретным заданием сдать экзамен, такой как IELTS и TOEFL. Более того, некоторые стремятся улучшить свои "
                 "деловые навыки и деловую беседу. Иногда им нужно пройти собеседование на английском языке. "
                 "В соответствии с их требованиями у меня есть материалы и программы, которые помогут им достичь желаемых "
                 "целей. Мой обширный опыт преподавания также играет важную роль.",
        "picture": "/static/cat_11.jfif",
        "rating": 4.7,
        "price": 1100,
        "goals": ["travel", "study", "work", "programming"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 11,
        "name": "Муркин Борис Витаминочив",
        "about": "Привет, ребята! Меня зовут Эндрю, я преподаватель английского языка из США, в настоящее время проживаю в "
                 "Атланте, штат Джорджия. Мой опыт преподавания варьируется от индивидуальных занятий до групповых, для детей и взрослых, "
                 "лично или онлайн. ВАЖНО*** Хотя у меня есть опыт преподавания детям, сейчас я только "
                 "обучаю взрослых разговорному английскому. Это моя специализация, и я делаю это, сосредоточившись "
                 "в основном на снижении акцента, произношении, логопедии и улучшении словарного запаса. Я "
                 "путешествую и преподаю с 2008 года, и мои путешествия действительно помогли мне стать более "
                 "культурно осведомленным и актуальным. Я веселый и уникальный, когда дело касается преподавания английского языка, вы не найдете моих "
                 "занятий где-либо еще.",
        "picture": "/static/cat_12.jfif",
        "rating": 4.2,
        "price": 900,
        "goals": ["travel", "work", "programming"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
]
