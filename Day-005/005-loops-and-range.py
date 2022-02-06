# range
print(f"range(1,5) =")
for number in range(1, 5):
    print(number)
    # ini bakal ngeprint angka 1-4 (angka terakhir ga termasuk ya)

print(f"\nrange(1,5,3) =")
for number in range(1, 15, 3):
    print(number)
    # ini bakal ngeprint angka 1-15 (angka terakhir ga termasuk ya), dengan selisih 3 tiap angka

# cerita carl gauss yang disuruh 1 + 2 + 3 + .... + 98 + 99 + 100 = ?
total = 0
for number in range(1, 101):
    total += number
print(f"\n{total}")