# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
country_set = set()
for i in range(0, n):
    country = input()
    country_set.add(country)
print(len(country_set))
