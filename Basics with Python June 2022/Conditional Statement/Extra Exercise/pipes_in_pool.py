v_of_pool = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())
pipe1_filled = pipe1 * hours
pipe2_filled = pipe2 * hours
pipes_filled = pipe1_filled + pipe2_filled
percent_p1 = pipe1_filled / pipes_filled * 100
percent_p2 = pipe2_filled / pipes_filled * 100
percent_pool_filled = pipes_filled / v_of_pool * 100
if v_of_pool >= pipes_filled:
    print(f'The pool is {percent_pool_filled:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.')
else:
    liters_overflow = abs(v_of_pool - pipes_filled)
    print(f'For {hours} hours the pool overflows with {liters_overflow} liters.')