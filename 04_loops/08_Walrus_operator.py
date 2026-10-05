value = 13

remaindeer =  value % 5

if remaindeer:
    print(f"Not divisible, remainder id {remaindeer}")

value = 13

if (remaindeer := value % 5):
    print(f"Not divisible, remainder is {remaindeer}")