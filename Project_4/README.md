# PROJECT-1. Анализ резюме из HeadHunter
Основной ноутбук - Project-1.ipynb

Ссылка на датасеты, используемые в работе:
 - https://drive.google.com/file/d/1bhjx6TbFW_bYNeoAHflnbBwuVzyXAmLX/view?usp=sharing
 - https://drive.google.com/file/d/1KGPFOjwI7XDMbx2SfaN3w-j3eWElZg2X/view?usp=sharing

В данном проекте в основном все диаграммы построены в plotly  и сохранены в папку "figures" в формате html.  Чтобы графики показывались, можно использовать nbviewer.org

## Оглавление  
[1. Описание проекта](https://github.com/balkhinag/Project_1#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[2. Какой кейс решаем?](https://github.com/balkhinag/Project_1#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)  
[3. Краткая информация о данных](https://github.com/balkhinag/Project_1#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/balkhinag/Project_1#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результат](https://github.com/balkhinag/Project_1#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/balkhinag/Project_1#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### Описание проекта   

В данном проекте нам предстоит решить настоящую задачу, которая часто встаёт перед аналитиками, работающими в банковском секторе.

Банки хранят огромные объёмы информации о своих клиентах. Эти данные можно использовать для того, чтобы оставаться на связи с клиентами и индивидуально ориентировать их на подходящие именно им продукты или банковские предложения.

Обычно с выбранными клиентами связываются напрямую через разные каналы связи: лично (например, при визите в банк), по телефону, по электронной почте, в мессенджерах и так далее. Этот вид маркетинга называется прямым маркетингом. На самом деле, прямой маркетинг используется для взаимодействия с клиентами в большинстве банков и страховых компаний. Но, разумеется, проведение маркетинговых кампаний и взаимодействие с клиентами — это трудозатратно и дорого.

Банкам хотелось бы уметь выбирать среди своих клиентов именно тех, которые с наибольшей вероятностью воспользуются тем или иным предложением, и связываться именно с ними.

Нам предоставили данные о последней маркетинговой кампании, которую проводил банк: задачей было привлечь клиентов для открытия депозита. Мы должны проанализировать эти данные, выявить закономерность и найти решающие факторы, повлиявшие на то, что клиент вложил деньги именно в этот банк. Если мы сможем это сделать, то поднимем доходы банка и поможем понять целевую аудиторию, которую необходимо привлекать путём рекламы и различных предложений.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Бизнес-задача: определить характеристики, по которым можно выявить клиентов, более склонных к открытию депозита в банке, и за счёт этого повысить результативность маркетинговой кампании.

Техническая задача для нас как для специалиста в Data Science: построить модель машинного обучения, которая на основе предложенных характеристик клиента будет предсказывать, воспользуется он предложением об открытии депозита или нет.

:arrow_up:[к оглавлению](.README.md#Оглавление)

### Краткая информация о данных
Данные, которые мы будем использовать, можно разделить на несколько групп:

##### *1. Данные о клиентах банка:*

- age (возраст);
- job (сфера занятости);
- marital (семейное положение);
- education (уровень образования);
- default (имеется ли просроченный кредит);
- housing (имеется ли кредит на жильё);
- loan (имеется ли кредит на личные нужды);
- balance (баланс).

##### *2. Данные, связанные с последним контактом в контексте текущей маркетинговой кампании:*

- contact (тип контакта с клиентом);
- month (месяц, в котором был последний контакт);
- day (день, в который был последний контакт);
- duration (продолжительность контакта в секундах).

##### *3. Прочие признаки:*

- campaign (количество контактов с этим клиентом в течение текущей кампании);
- pdays (количество пропущенных дней с момента последней маркетинговой кампании до контакта в текущей кампании);
- previous (количество контактов до текущей кампании)
- poutcome (результат прошлой маркетинговой кампании).

И, разумеется, наша целевая переменная *deposit*, которая определяет, согласится ли клиент открыть депозит в банке. Именно её мы будем пытаться предсказать в данном кейсе.
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
Проект будет состоять из пяти частей:

#### 1. Первичная обработка данных

В рамках этой части нам предстоит обработать пропуски и выбросы в данных. Это необходимо для дальнейшей работы с ними.

#### 2. Разведывательный анализ данных (EDA)

На этом этапе нам необходимо будет исследовать данные, нащупать первые закономерности и выдвинуть гипотезы.

#### 3. Отбор и преобразование признаков

На этом этапе мы перекодируем и преобразуем данные таким образом, чтобы их можно было использовать при решении задачи классификации. Если на первом этапе мы лишь избавим данные от ненужных артефактов, то на этом шаге совершим действия, более важные для подготовки данных к задаче классификации, уже понимая их структуру.

#### 4. Решение задачи классификации: логистическая регрессия и решающие деревья

На данном этапе мы построим свою первую прогностическую модель и оценим её качество. Подберем оптимальные параметры модели для того, чтобы получить наилучший результат для конкретного алгоритма.

#### 5. Решение задачи классификации: ансамбли моделей и построение прогноза

На заключительном этапе мы доработаем своё предсказание с использованием более сложных алгоритмов и оценим, с помощью какой модели возможно сделать более качественные прогнозы.


:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
По итогам проделанной работы мы получили следующий результат:
- Преобразовали "сырые" данные в более удобный для анализа формат
- Построили диаграммы, которые позволяют визуально оценить зависимости в данных
- отобрали 15 наиболее значимых признаков по методу SelectKBest
- построили следующие модели предсказания:
    - логистическую регрессию
    - решающие деревья
    - случайный лес
    - градиентный бустинг
    - стекинг моделей
- воспользовались такими инстурментами как Optuna и GridSearch для подбора оптимальных параметров


:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
В результате проделанного проекта удалось испытать на себе основные этапы работы с данными на примере датасета о резюме соискателей

:arrow_up:[к оглавлению](.README.md#Оглавление)
