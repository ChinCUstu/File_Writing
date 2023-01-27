with open('ChapelServiceAttendance.txt', 'r') as file:
	line = file.readline().rstrip('\n')
	with open('Updated.txt', 'w') as out_file:
		out_file.write(line + '    Percentage' + '\n')
		total = 0
		avg = 0.0
		for line in file:
			new = line.strip('\n').split('    ')
			for i in range(3, len(new)):
				if int(new[i]) == 1:
					total += 1
			avg = total / 4
			percent = avg * 100
			new = '    '.join(new)
			out_file.write(f"{new}    {percent}%\n")
			total = 0
		print('Done writing to file Updated.txt')
