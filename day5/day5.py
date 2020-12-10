import BoardingPass

def get_all_seats():
    with open("input.txt") as input_file:
        return [BoardingPass.BoardingPass(line.rstrip()) for line in input_file]

all_seat_ids = [seat.get_seat_id() for seat in get_all_seats()]

max_seat_id = max(all_seat_ids)
print(f"The highest seat ID is: {max_seat_id}") # solution to part 1

# for part 2, we are told the seats with IDs +1 and -1 from ours are in the list
# so our seat ID is somewhere in the range between lowest and highest seat IDs
min_seat_id = min(all_seat_ids)
seat_range = [num for num in range(min_seat_id,max_seat_id+1)]
for seat in all_seat_ids:
    seat_range.remove(seat)
print(seat_range) # solution to part 2