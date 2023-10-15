class Jar:
    def __init__(self,capacity =12):
        if capacity <0:
            raise ValueError("Capacity should be postive int")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return int(self.cookies) * '🍪'

    def deposit(self,n):
        if n+self.cookies >self.capacity:
            raise ValueError("Cookie jar capacity Exceeded")
        self.cookies += n

    def withdraw(self, n):
        if self.cookies <n:
            raise ValueError("Not enough cookies in the jar")
        self.cookies -= n
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if not isinstance(capacity,int) or capacity <0:
            raise ValueError("Capacity must be an int")
        self._capacity= capacity

    @property
    def size(self):
        return self.cookies

def main():
    cookie_jar =Jar(capacity=10)
    cookie_jar.deposit(10)
    print(cookie_jar)
    cookie_jar.withdraw(5)
    print(cookie_jar)

if __name__=="__main__":
    main()