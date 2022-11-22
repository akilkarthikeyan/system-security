import os
import subprocess

graph = [[0, 0, 0, 1], 
         [0, 0, 1, 0], 
         [1, 0, 0, 1],
         [0, 1, 1, 0]]

ports = [8001, 8002, 8003, 8004]

for i in range(len(graph)):
    os.system('cp Skeleton.txt B' + str(i) + '.py')
    arr = [7001, 7002]
    # for j in range(len(graph[i])):
    #     if graph[i][j]:
    #         arr.append(ports[j])
    os.system('echo "\nports = ' + str(arr) + '" >> B' + str(i) + '.py')
    os.system('echo "label = \'B' + str(i) + '\'" >> B' + str(i) + '.py')
    st = "if __name__ == '__main__':\n\tuvicorn.run(app, port = " + str(ports[i]) + ", host = '127.0.0.1')"
    os.system('echo "' + st + '" >> B' + str(i) + '.py')

for i in range(len(graph)):
    os.system('cmd.exe /c start cmd.exe /c wsl.exe')
    # os.system('python3 B' + str(i) + '.py')
    
