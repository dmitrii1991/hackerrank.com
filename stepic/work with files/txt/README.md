
Дан текст на языке племени Мумба-Юмба. Выведите все слова, встречающиеся в тексте, разделяя их пробелом. Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в алфавитном порядке.

Подсказка. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму. Это почти то, что требуется в задаче, а чтобы сделать то что нужно — вспомните про параметр key в сортировке.

В этой задачи нужно сдать только ответ для входного файла. Ссылка на входной файл https://stepik.org/media/attachments/lesson/258916/input.txt
