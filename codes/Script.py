import os
import subprocess

graph = [[0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0], 
         [1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [1, 0, 0, 1, 0]]

ports = [7001, 7002, 8001, 8002, 8003]
start = 2

for i in range(0, start):
    os.system('cp SkeletonDB.txt DB' + str(i) + '.py')
    os.system('echo "\nlabel = \'DB' + str(i) + '\'" >> DB' + str(i) + '.py')
    st = "if __name__ == '__main__':\n\tuvicorn.run(app, port = " + str(ports[i]) + ", host = '127.0.0.1')"
    os.system('echo "' + st + '" >> DB' + str(i) + '.py')

for i in range(start, len(graph)):
    os.system('cp Skeleton.txt B' + str(i - start) + '.py')
    arr = []
    for j in range(len(graph)):
        if(graph[i][j]):
            arr.append(ports[j])
    os.system('echo "\nports = ' + str(arr) + '" >> B' + str(i - start) + '.py')
    os.system('echo "label = \'B' + str(i - start) + '\'" >> B' + str(i - start) + '.py')
    st = "if __name__ == '__main__':\n\tuvicorn.run(app, port = " + str(ports[i]) + ", host = '127.0.0.1')"
    os.system('echo "' + st + '" >> B' + str(i - start) + '.py')

for i in range(0, start):
    os.system('gnome-terminal -- python3 DB' + str(i) + '.py')

for i in range(start, len(graph)):
    os.system('gnome-terminal -- python3 B' + str(i - start) + '.py')
    