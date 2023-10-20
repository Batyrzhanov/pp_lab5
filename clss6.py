class PrimeNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
prime_filter = PrimeNumberFilter(numbers)
prime_numbers = prime_filter.filter_primes()
print("Prime numbers in the list:", prime_numbers)

