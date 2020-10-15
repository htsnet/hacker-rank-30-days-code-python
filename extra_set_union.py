# Set .union() Operation


nE = int(input())
english = set(input().split())
nF = int(input())
french = set(input().split())

print(len(english.union(french)))
