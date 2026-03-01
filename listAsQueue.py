from collections import deque
queue = deque(["Babita", "Ishani", "Bijaya"])
queue.append("Sandip")
queue.append("Asmita")
print(queue)
queue.popleft()
queue.popleft()
print(queue)
#esma popleft() le items haru left bata remove garxa, like mathi herda babita and ishani remove hunxan queue bata
