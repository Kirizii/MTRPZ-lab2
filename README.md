# MTRPZ-lab2
# ArrayList and CircularLinkedList Application

## Опис
Цей проєкт демонструє роботу з типізованим списком літер (Character) у двох реалізаціях:

1️) **ArrayList** — реалізація списку на базі вбудованого масиву (Python list).

2️) **CircularLinkedList** — власна реалізація однобічно зв’язаного кільцевого списку без використання вбудованих колекцій.

Обидва класи підтримують основні методи:
- length()
- append(element: Character)
- insert(element: Character, index: Integer)
- delete(index: Integer)
- deleteAll(element: Character)
- get(index: Integer)
- clone()
- reverse()
- findFirst(element: Character)
- findLast(element: Character)
- clear()
- extend(elements: List).

---

## Варіант

- Номер варіанту: **2** (10%4=2)
- Початкова реалізація: список на базі масивів (Python list)
- Друга реалізація: однобічно зв’язаний кільцевий список

---

## Інструкція: як зібрати проект та запустити тести

1️. Склонуйте репозиторій:
```bash
git clone https://github.com/Kirizii/MTRPZ-lab2.git
cd MTRPZ-lab2
```
2. Встановіть залежності:
```bash
pip install pytest
```
3. Запустіть всі тести:
```bash
pytest
```

---

## Посилання на коміт, на якому впали тести на CI
https://github.com/Kirizii/MTRPZ-lab2/commit/f8bf6d2688f9b1d5d1bf69bb206790ca09f6b482

---

## Висновок
У цьому проєкті unit-тести показали себе як корисний практичний інструмент. Вони допомогли впевнитися, що основні методи працюють як очікується, і зменшили ризики помилок під час внесення змін. Підключення CI дозволило автоматизувати перевірки, що виявилося зручним способом тримати код у стабільному стані. Загалом досвід роботи з тестами й автоматизацією в цьому завданні був корисним, хоча місцями вимагав додаткового часу та уваги.
