def setdir(i, j):
	si = i
	sj = j
	r = j + 1
	l = j - 1
	u = i - 1
	d = i + 1
	if i == 0 and j == 0:
		dirs[0] = (si, r)
		dirs[1] = ""
		dirs[2] = ""
		dirs[3] = (d, sj)
	elif i == 0 and j == 3:
		dirs[0] = ""
		dirs[1] = (si, l)
		dirs[2] = ""
		dirs[3] = (d, sj)
	elif i == 3 and j == 0:
		dirs[0] = (si, r)
		dirs[1] = ""
		dirs[2] = (u, sj)
		dirs[3] = ""
	elif i == 3 and j == 3:
		dirs[0] = ""
		dirs[1] = (si, l)
		dirs[2] = (u, sj)
		dirs[3] = ""
	elif i == 0:
		dirs[0] = (si, r)
		dirs[1] = (si, l)
		dirs[2] = ""
		dirs[3] = (d, sj)
	elif i == 3:
		dirs[0] = (si, r)
		dirs[1] = (si, l)
		dirs[2] = (u, sj)
		dirs[3] = ""
	elif j == 0:
		dirs[0] = (si, r)
		dirs[1] = ""
		dirs[2] = (u, sj)
		dirs[3] = (d, sj)
	elif j == 3:
		dirs[0] = ""
		dirs[1] = (si, l)
		dirs[2] = (u, sj)
		dirs[3] = (d, sj)
	else:
		dirs[0] = (si, r)
		dirs[1] = (si, l)
		dirs[2] = (u, sj)
		dirs[3] = (d, sj)


def allowed(ls):
	for objs in dirs:
		if objs != "":
			ls.append(objs)
	return ls


def checkwumpus(steps):
	if w[int(steps[0])][int(steps[1])] == 1:
		print("Player got killed")
		print(f'visited: {visited}')
		print('\n')
		for i in k:
			print(i)
		print('\n')
		exit(0)
	elif w[int(steps[0])][int(steps[1])] == 2:
		return 2
	else:
		return 0


def checkpit(steps):
	if p[int(steps[0])][int(steps[1])] == 3:
		print("Player got killed")
		print('\n')
		for i in k:
			print(i)
		print('\n')
		exit(0)
	elif p[int(steps[0])][int(steps[1])] == 4:
		return 4
	else:
		return 0


def stepintocell(step):
	ws = checkwumpus(step)
	pb = checkpit(step)
	return (ws, pb)


def action():
	global tl2, present, tv
	for step in tl:
		print(f'\nFor {step}:')
		if step in visited:
			print(step, "is visited\n")
			if int(step[0]) == pm and int(step[0]) == pn:
				print("1")
			elif '2' in str(k[int(step[0])][int(step[1])]):
				print("2")
		else:
			setdir(int(step[0]), int(step[1]))
			tl2 = tl2[0:0]
			tl2 = allowed(tl2)
			print("Connections of", step, ': ', tl2)
			for st in tl2:
				if st == present:
					print(st, "is Present Cell")
				else:
					print("checking ", st)
					if st in start:
						print(st, "is Start state")
					elif st == present:
						print(st, "is Present state")
					elif st in visited:
						print(st, "is visited")
						if (k[int(st[0])][int(st[1])] in [(0, 4), (4, 0), (0, 2), (2, 0)]) and (
								k[int(present[0])][int(present[1])] in [(0, 2), (2, 0), (0, 4), (4, 0)]):
							k[int(step[0])][int(step[1])] = 'S'
							print(f'Putting Safe State at ({step[0]}, {step[1]})')
							print("Visited :", visited)
							return step
						print("\n")
	print("______\n")
	return 0


def nextstep(ws, wp):
	global tl, present, prev, tmp, h
	print("\nPresent: ", present, end=' ')
	print("Previous: ", prev)
	setdir(ws, wp)
	tl = tl[0:0]
	tl = allowed(tl)
	if ws == gm and wp == gn:
		h = 1
		if h == 1:
			print("\nHurray!!Got the Gold", end=' ')
		print("\nPresently in %s returning back to %s" % (present, start))
		for steps in range(len(mypath), 0, -1):
			prev = present
			present = mypath[steps - 1]
		print("Now reached to :", present)
		exit(0)
	elif k[ws][wp] == "S":
		print(f'\n{present} is a Safe Cell')
		print("Allowed Steps", tl)
		for step in tl:
			tmp = step
			if step not in visited:
				print(step, "Not visited")
				prev = present
				print("Previous: ", prev)
				present = (step[0], step[1])
				print("Present: ", present)
				k[int(step[0])][int(step[1])] = stepintocell(step)
				print(f'\nStepping into ({step[0]}, {step[1]})')
				mypath.append(step)
				visited.append(step)
				print(f'visited: {visited}')
				print('\n')
				for i in k:
					print(i)
				print('\n')
				nextstep(int(step[0]), int(step[1]))
			else:
				print(step, "is already visited")
	else:
		print(f'\n{present} is not a Safe Cell', end=' ')
		print("\nConnections of ", present, ":", tl, end=' ')
		l = action()
		if l == 0:
			print("Stepping Back to", prev, "\n")
			mypath.pop()
			present = prev
			nextstep(int(prev[0]), int(prev[1]))
		else:
			print("Reached ", l)
			visited.append(l)
			print(f'visited: {visited}')
			prev = tmp
			present = l
			print("\nfrom here Stepping into ", l, end=' ')
			mypath.append(l)
			nextstep(int(l[0]), int(l[1]))


dirs = ["right", "left", "up", "down"]
gm = 1
gn = 1
pm = 3
pn = 0
h = 0
visited = []
w = [[2, 0, 0, 0], [1, 2, 0, 2], [2, 0, 2, 1], [0, 0, 0, 2]]
print('wumpus:')
for i in w:
	print(i)
p = [[0, 0, 4, 3], [0, 4, 3, 4], [0, 0, 4, 0], [0, 4, 3, 4]]
print('pit:')
for i in p:
	print(i)
k = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
k[pm][pn] = 'S'
print('\n')
for i in k:
	print(i)
print('\n')
tl = []
tl2 = []
tmp = ""
tv = 1
mypath = []
prm = pm
prn = pn
start = (pm, pn)
visited.append(start)
print(f'visited: {visited}')
print(f'Starting from ({pm}, {pn})')
prev = (pm, pn)
present = (pm, pn)
mypath.append(start)
nextstep(pm, pn)
print(present)
print('\n')
for i in k:
	print(i)
print('\n')
