def rooms_booked(reservations):
    occupied = set()
    for r in reservations:
        room = r[1:]
        if r.startswith("+"):
            occupied.add(room)
        else:
            occupied.remove(room)
    return len(occupied), occupied


print(rooms_booked(["+3A", "+8G", "-3A"]))
print(rooms_booked(["+3A", "+8G", "-3A", "+3A"]))
print(rooms_booked([]))
print(rooms_booked(["+1W", "+3W", "+4W"]))
print(rooms_booked(["+1W", "+3W", "+4W", "-1W", "-3W", "-4W"]))
