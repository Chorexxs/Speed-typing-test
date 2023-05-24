import time
import random

# Función para generar una lista de palabras aleatorias
def get_words():
    words = ["python", "program", "speed", "typing", "test", "keyboard",
             "mouse", "computer", "screen", "code", "debug", "algorithm",
             "happy", "sad", "joy", "anger", "fear", "love", "hate",
             "sun", "moon", "star", "planet", "galaxy", "universe",
             "dog", "cat", "bird", "fish", "horse", "hamster",
             "green", "blue", "red", "yellow", "orange", "purple",
             "music", "song", "dance", "singer", "instrument", "guitar",
             "book", "novel", "story", "author", "reader", "library",
             "movie", "film", "cinema", "actor", "director", "script",
             "ocean", "beach", "wave", "island", "swim", "surf",
             "tree", "flower", "grass", "forest", "leaf", "nature",
             "car", "bike", "train", "plane", "bus", "subway",
             "food", "drink", "meal", "restaurant", "cook", "recipe",
             "school", "teacher", "student", "lesson", "study", "class",
             "work", "job", "career", "money", "boss", "employee",
             "friend", "family", "love", "relationship", "marriage", "divorce"]
    random.shuffle(words)
    return words[:10]

# Función para mostrar las palabras y medir el tiempo de escritura
def start_typing(words):
    start_time = time.time()
    typed_words = []
    for word in words:
        print(word)
        typed_word = input()
        typed_words.append(typed_word)
    end_time = time.time()
    return typed_words, end_time - start_time

# Función para calcular la puntuación en palabras por minuto
def calculate_wpm(typed_words, time_elapsed):
    typed_chars = sum(len(word) for word in typed_words)
    wpm = (typed_chars / 5) / (time_elapsed / 60)
    return wpm

# Programa principal
print("Bienvenido al Speed Typing Test!")
input("Presione Enter para empezar...")
words = get_words()
typed_words, time_elapsed = start_typing(words)
wpm = calculate_wpm(typed_words, time_elapsed)
print(f"Su puntuación es de {wpm:.2f} palabras por minuto.")
