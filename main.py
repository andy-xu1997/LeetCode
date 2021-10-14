res = []
n = 3
right = 0
left = 0
def huisu(paths,right,left):
    if right > n or left > right:
        return
    if len(paths) == 2 * n:
        res.append(paths)
        print(paths)
    huisu(paths + '(', right + 1, left)
    huisu(paths + ')', right, left + 1)
huisu('',0,0)