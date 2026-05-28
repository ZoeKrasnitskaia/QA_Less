import random
import time


class Practice:

    def list_numbers(self):
        start = 1
        end = 8
        limit = 5

        numbers = list(range(start, end))
        for n in numbers:
            if n == limit:
                break
            print(n)

    def list_words(self):
        limit = 10
        words = [f"str{i}" for i in range(limit)]
        for word in words:
            print(word)

    def simulate_rostics_load(self):
        max_iterations = 10
        critical_load_limit = 85
        pause_duration = 0.2
        iteration = 0

        while iteration < max_iterations:
            current_load = random.randint(0, 100)
            print(
                f"Итерация {iteration + 1}:"
                f"Текущая нагрузка {current_load}%")

            if current_load > critical_load_limit:
                print(
                    f"️ВНИМАНИЕ: Высокая нагрузка на серверы Rostics!"
                    f"({current_load}%)"
                )

            time.sleep(pause_duration)
            iteration += 1


object_for_pract1 = Practice()
object_for_pract1.list_numbers()

object_for_words = Practice()
object_for_words.list_words()

object_for_rostics = Practice()
object_for_rostics.simulate_rostics_load()
