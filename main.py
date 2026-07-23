from datetime import datetime
from pathlib import Path
from id_generator import id_generator


#''''''
#Додаток, який буде зберігати нотатки

#This is my note, that I am taking on my laptop
#- Created on 06.01.2026 23:00

[("This is my note, that I am taking on my laptop, 06.01.2026 23:00")]
[("06.01.2026 23:00", "This is my note, that I am taking on my laptop")]

#if note_data_one[1] > note_data_one[1]:
#    ...
#
#if note_data_one["creation_date"] > note_data_one["creation_date"]:
#    ...
#
#{"text": "This is my note, that I am taking on my laptop", "creation_date": "06.01.2026 23:00"}
#{"creation_date": "06.01.2026 23:00", "text": "This is my note, that I am taking on my laptop"}

    
    
#...
#1) Створити словник, який буде зберігати нотатки та їх дату створення
#2) Написати функцію, яка буде виводити нотатку
#3) Написати функцію, яка буде виводити всі нотатки
#4) Написати цикл, який буде отримувати інформацію від користувача та реагувати на неї
#5) Пофіксити проблему, де є глобальна змінна
#'''

note_list = []  # [{"creation_date": "06.01.2026 23:00", "text": "This is my note, that I am taking on my laptop", id: 1}]
note_file = "notes.txt"
note_id_generator = id_generator()


# Hello note; 01.06.2026 23:00

welcome_banner = """
█   █ █████ █     ████  █████ ████      ████   ███  █████ 
█   █ █     █     █   █ █     █   █     █   █ █   █   █   
█████ ████  █     ████  ████  ████      ████  █   █   █   
█   █ █     █     █     █     █   █     █   █ █   █   █   
█   █ █████ █████ █     █████ █    █    ████   ███    ©   
"""

commands = """
1) exit - to exit the app
2) add_note - to add new note
3) print_note (i)- to print note number i
4) print_all - to print all notes
5) help - to print this menu
6)


"""


def add_new_note(note_text) -> bool:
    note_creation_date = datetime.today()
    next_id = note_id_generator()
    note_list.append({"text": note_text, "creation_date": note_creation_date, "id": next_id})
    save_notes()  # Автоматично зберігаємо у файл після додавання!
    return True

def print_note(index: int):
    note = note_list[index]
    #dd.mm.yyyy hh:mm
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'{note["id"]}: "{note["text"]}"\n- Created on {formatted_creation_date}\n') #strptime str p time string parse time - перетворює рядок у дату

def print_all_notes():
    for note_index in range(len(note_list)):
        print_note(note_index)

def find_top_note_id(notes: list[dict]) -> int:
    max_id = 0
    for note in notes:
        note_id = note['id']
        if not_id > max_id:
            max_id = note_id
    return max_id

#def find_top_note_id_functional(notes: list[dict]) -> int:
    note_ids = []
    for note in notes:
        note_ids.append(note['id'])
    return max(note_ids)

#comprehenshions  
def find_top_note_id_functional(notes: list[dict]) -> int:
    return max([note['id'] for note in notes] + [0])


def save_notes():
    with open(note_file, "w") as file:
        for note in note_list:
            # Зберігаємо дату у чіткому текстовому форматі, щоб потім легко прочитати
            date_str = note["creation_date"].strftime("%d.%m.%Y %H:%M")
            file.write(f'{note["id"]};{note["text"]};{date_str}\n')

def read_notes() -> list[dict]:
    # Створюємо локальний список з правильним відступом
    local_note_list = []

    # Перевіряємо, чи існує файл, щоб open() не видавав помилку при першому запуску
    if not Path(note_file).exists():
        return []

    with open(note_file) as file:
        for line in file:
            line.split(";") #["This is my note", "06.01.2026 23:00"]
            id, text, date = line.strip().split(";")
            creation_date = datetime.strptime(date, "%d.%m.%Y %H:%M") #datetime object
            # Виправлено відступи та додано об'єкт creation_date, щоб працював метод .strftime у print_note
            note_list.append({"id": int(id), "text": text, "creation_date": creation_date})
    return local_note_list


def init():
    # Робимо так, щоб read_notes записував дані в глобальний note_list
    global note_list
    note_list = read_notes()

    max_note_id = find_top_note_id_functional(note_list)

    global note_id_generator
    note_id_generator = id_generator(max_note_id)

    print(welcome_banner)
    print("\nHello and welcome to our app!")
    print(commands)
    print()

def main():
    while True:
        # Усі команди всередині циклу while тепер мають рівні 8 пробілів від краю
        command, *args = input("Please, enter command (enter exit to stop): ").strip().split() #print_note
        
        if command == "exit":
            print("Goodbye!")
            break

        elif command == "add_note":
            text = input("Please, enter note text: ")
            if add_new_note(text):
                print("\nNote added successfully!\n")
            else:
                print("\nError adding note!\n")
                
        elif command =="help":
            print(commands)
            
        elif command == "print_note":
            # Перевірка на випадок, якщо користувач забув ввести цифру після print_note
            if not args:
                print("Please, enter note index after command!")
                continue
                
            index = int(args[0]) - 1
            if index < 0 or index >= len(note_list):
                print("Please, enter valid note index!")
                continue
            print_note(index)
        elif command == 'print_all':
            print_all_notes()

init()
main()