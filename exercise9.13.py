from random import randint

class Die:
    """Model sederhana untuk merepresentasikan sebuah dadu."""
    
    def __init__(self, sides=6):
        """Inisialisasi atribut jumlah sisi dadu (default 6 sisi)."""
        self.sides = sides
        
    def roll_die(self):
        """Mengembalikan angka acak antara 1 dan jumlah sisi dadu."""
        return randint(1, self.sides)


# 1. Dadu 6 Sisi
die_6 = Die(6)
results_6 = []
for _ in range(10):
    results_6.append(die_6.roll_die())

print("--- Lemparan Dadu 6 Sisi (10x) ---")
print(results_6)

# 2. Dadu 10 Sisi
die_10 = Die(10)
results_10 = []
for _ in range(10):
    results_10.append(die_10.roll_die())

print("\n--- Lemparan Dadu 10 Sisi (10x) ---")
print(results_10)

# 3. Dadu 20 Sisi
die_20 = Die(20)
results_20 = []
for _ in range(10):
    results_20.append(die_20.roll_die())

print("\n--- Lemparan Dadu 20 Sisi (10x) ---")
print(results_20)