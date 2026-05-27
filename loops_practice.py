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

object_for_pract1 = Practice()
object_for_pract1.list_numbers()