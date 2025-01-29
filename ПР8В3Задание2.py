def sort_letters_in_words(input_string):
    words = input_string.split()  # Разделяем строку на слова
    sorted_words = [''.join(sorted(word)) for word in words]  # Сортируем буквы в каждом слове
    return ' '.join(sorted_words)  # Объединяем слова обратно в строку

# Пример использования
input_string = "Привет мир"
sorted_string = sort_letters_in_words(input_string)
print(sorted_string)
