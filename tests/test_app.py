from src.proses import hitung_rata_rata

# Pengujian manual dengan assert
assert hitung_rata_rata([75, 85, 90]) == 83.33333333333333
assert hitung_rata_rata([]) == 0
print("Semua test case sederhana BERHASIL (PASS)!")