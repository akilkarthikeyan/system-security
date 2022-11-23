import os
import subprocess

graph = [[0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0], 
         [1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [1, 0, 0, 1, 0]]

ports = [7001, 7002, 8001, 8002, 8003]
start = 2

for i in range(start, len(graph)):
    os.system('cp Skeleton.txt B' + str(i) + '.py')
    arr = []
    for j in range(len(graph)):
        if(graph[i][j]):
            arr.append(ports[j])
    os.system('echo "\nports = ' + str(arr) + '" >> B' + str(i) + '.py')
    os.system('echo "label = \'B' + str(i) + '\'" >> B' + str(i) + '.py')
    st = "if __name__ == '__main__':\n\tuvicorn.run(app, port = " + str(ports[i]) + ", host = '127.0.0.1')"
    os.system('echo "' + st + '" >> B' + str(i) + '.py')

# export DISPLAY_NUMBER="0.0"
# export DISPLAY=$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}'):$DISPLAY_NUMBER
# export LIBGL_ALWAYS_INDIRECT = 1
# setsid emacs

for i in range(start, len(graph)):
    os.system('gnome-terminal -- python3 B' + str(i) + '.py')
    