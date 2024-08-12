import heapq

def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0

    # Ініціалізація мінімальної купи
    heapq.heapify(cable_lengths)                                 # Перетворюємо список у мін-купу

    total_cost = 0

                                                                 # Об'єднуємо кабелі, поки в купі більше одного кабеля
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)                     # Витягуємо два найменших кабелі
        second = heapq.heappop(cable_lengths)

        
        cost = first + second                                    # Об'єднуємо кабелі та додаємо вартість об'єднання до загальних витрат
        total_cost += cost

        heapq.heappush(cable_lengths, cost)                      # Додаємо новий об'єднаний кабель до купи

        return total_cost

if __name__ == '__main__':
    cable_lengths = [1, 7, 6, 2, 3, 5]

    print("Вихідні довжини кабелів:", sorted(cable_lengths))
    print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
