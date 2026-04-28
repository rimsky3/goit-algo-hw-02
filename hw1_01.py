from queue import Queue
import random

# craete a queue
queue = Queue()
request_counter = 0

def generate_request():
    global request_counter
    request_counter += 1
    request = {
        
        "id": request_counter,
        "type": random.choice(["Ремонт", "Консультація", "Діагностика"])
    }
    queue.put(request)
    print(f"Згенеровано заявку: {request['id']} | {request['type']}")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Оброблено заявку: {request['id']} | {request['type']}")
    else:
        print("Немає заявок для обробки")


if __name__ == "__main__":

    while True:
        user_input = input("Нажми enter щоб продовжити, або 'q' для виходу: ")
        if user_input == 'q':
            print("Вихід з програми")
            break


        generate_request()
        process_request()
