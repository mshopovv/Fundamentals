number_of_rooms = int(input())
total_free_seats = 0
total_visitors = 0

for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    total_visitors += visitors
    total_free_seats += chairs
    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {room}")

if total_visitors <= total_free_seats:
    print(f"Game On, {total_free_seats - total_visitors} free chairs left")