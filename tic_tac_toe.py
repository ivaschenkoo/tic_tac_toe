class TicTacToe():
	"""Tic Tac Toe Game"""
	desk = [[' ' for i in range(3)] for i in range(3)]
	game_status = True
	x_counter = 0
	o_counter = 0

	def print_desk(self):
		print('\n---------')
		print(f'| {self.desk[0][0]} {self.desk[0][1]} {self.desk[0][2]} |')
		print(f'| {self.desk[1][0]} {self.desk[1][1]} {self.desk[1][2]} |')
		print(f'| {self.desk[2][0]} {self.desk[2][1]} {self.desk[2][2]} |')
		print('---------')

	#Determine whose move
	def current_move(self):
		if self.x_counter <= self.o_counter:
			self.x_counter += 1
			return 'X'
		else:
			self.o_counter += 1
			return 'O'

	#We check the accuracy of entering coordinates, the availability of the cell and make a move
	def get_move(self):
		while True:
			coordinates = [i for i in input('\nEnter the coordinates:\n').split()]
			if 1 < len(coordinates) < 3:
				y = coordinates[0]
				x = coordinates[1]
			else:
				print('\nEnter row number and column number.\nFor example: 1 1')
				continue
			if y in ('1', '2', '3') and x in ('1', '2', '3'):
				if self.desk[int(y) - 1][int(x) - 1] == ' ':
					self.desk[int(y) - 1][int(x) - 1] = self.current_move()
					break
				else:
					print('\nThe position is already taken!')
			else:
				print('\nCoordinates must be digits from 1 to 3!\nFor example: 1 1')
	
	#Check the status of the game. 1 cycle - lines. 2nd cycle - columns. 3 check - on the diagonal.
	def check_desk(self):
		for i in self.desk:
			if i == ['X', 'X', 'X'] or i == ['O', 'O', 'O'] and i[0] != ' ':
				print(f'{i[0]} wins')
				self.game_status = False
				return None
		for j in range(3):
			if self.desk[0][j] == self.desk[1][j] == self.desk[2][j] and self.desk[0][j] != ' ':
				print(f'{self.desk[j][0]} wins')
				self.game_status = False
				return None
		if self.desk[0][0] == self.desk[1][1] == self.desk[2][2] and self.desk[1][1] != ' ':
			print(f'{self.desk[1][1]} wins')
			self.game_status = False
			return None
		elif self.desk[0][2] == self.desk[1][1] == self.desk[2][0] and self.desk[1][1] != ' ':
			print(f'{self.desk[1][1]} wins')
			self.game_status = False
			return None
		else:
			return None

	#Zeroing values for starting a new game
	def new_game(self):
		self.desk = [[' ' for i in range(3)] for i in range(3)]
		self.game_status = True
		self.x_counter = 0
		self.o_counter = 0


desk1 = TicTacToe()
desk1.print_desk()

while desk1.game_status:
	desk1.get_move()
	desk1.print_desk()
	desk1.check_desk()
	if desk1.game_status == False:
		status = input('\nWant to play more?(yes/no)\n')
		if status.lower() == 'yes':
			desk1.new_game()
			desk1.print_desk()
		else:
			print('\nSee you later!')