import time

def ft_progress(l):
    """
    Generator returning every item one by one contained in the list l.
    """
    for i in range(len(l)):
        yield i


def handle_elapsed(begin,now):
	time = now - begin
	return time

def handle_arrow()

def main():
	listy = range(1000)
	ret = 0
	begin = time.time()
	old = time.time()
	currelem = 0
	full = len(listy)
	for elem in ft_progress(listy):
		currelem += 1
		ret += (elem + 3) % 5
		time.sleep(0.01)
		current = time.time()
		ETA = (current - old) * full
		old = time.time()
		print("ETA: %.2fs [ %d%%][=====>                 ] 233/1000 | elapsed time %.2fs" % (ETA, (currelem *100 / full),handle_elapsed(begin, current)), end = "\r")
	print()
	print(ret)


if __name__ == "__main__":
	main()