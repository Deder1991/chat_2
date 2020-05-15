
def read_file(filename):
	message = []
	with open(filename, 'r', encoding='utf-8-sig') as file:
		for line in file:
			message.append(line.strip())
	return message

def convert_message(filename):
	Allen_word_count = 0
	Allen_stickers_count = 0
	Allen_image_count = 0
	Viki_word_count = 0
	Viki_stickers_count = 0
	Viki_image_count = 0
	for line1 in filename:
		convert_message = line1.split(' ')
		time = convert_message[0]
		name = convert_message[1]
		message_split = convert_message[2:]
		print(message_split)
		if name == 'Allen':
			for line2 in message_split:
				if line2 == '貼圖':
					Allen_stickers_count += 1
				elif line2 == '圖片':
					Allen_image_count += 1
				else:
					Allen_word_count += len(line2)
		elif name == 'Viki':
			for line3 in message_split:
				if line3 == '貼圖':
					Viki_stickers_count += 1
				elif line3 == '圖片':
					Viki_image_count += 1
				else:
					Viki_word_count += len(line3)

		
	print('Allen說了:', Allen_word_count, '個字')
	print('Allen發了:', Allen_stickers_count, '個貼圖')
	print('Allen發了:', Allen_image_count, '個圖片')
	print('Viki說了:', Viki_word_count, '個字')
	print('Viki發了:', Viki_stickers_count, '個貼圖')
	print('Viki發了:', Viki_image_count, '個圖片')
	


def main():
	message = read_file('LINE-Viki.txt')
	print(message)
	convert_message(message)


main()