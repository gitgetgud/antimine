from models.board import Board
ar=[
[' ', ' ', ' ', '1', 'X', 'X', 'X', 'X', 'X'],
[' ', ' ', ' ', '1', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', '1', '2', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', '2', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', '1', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', ' ', '1', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', ' ', '1', 'X', 'X', 'X', 'X', 'X', 'X']
]

b=Board(9,9,ar)
b.analyze_mines()
b.analyze_safe()
b.debug()
print("probs")
b.debug(lambda o: " " if o.mine_prob == None else str(int(o.mine_prob)))
print(b.get_safe())
print(b.cells[0][3].get())