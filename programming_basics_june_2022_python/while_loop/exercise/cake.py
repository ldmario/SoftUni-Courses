cake_width = int(input())
cake_length = int(input())
total_pieces = cake_length * cake_width
pieces = total_pieces
taken = 0

while True:
    taken_pieces = input()
    if not taken_pieces == "STOP":
        taken_pieces = int(taken_pieces)
        pieces -= taken_pieces
        taken += taken_pieces
        if pieces <= 0:
            break
    else:
        break

diff = abs(pieces)

if taken > total_pieces:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")
