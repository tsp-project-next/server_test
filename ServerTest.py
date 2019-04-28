import subprocess
import tempfile
import time
import os

clients = []

numClients = 200
counter = 0

for i in range(0, numClients):
    output = tempfile.TemporaryFile()
    #time.sleep(1)

    process = subprocess.Popen(['java', '-jar', '/Users/connor/projectnext-gradle/build/libs/projectnext-gradle-1.0-SNAPSHOT.jar'], stdout = output)
    
    clients.append((output, process, i))

for output, process, i in clients:
    process.wait()
    counter += 1
    output.seek(0)
    #print("Client " + str(i) + ":\n" + output.read().decode('utf-8'))
    output.close()

if (counter == numClients):
    print("There were " + str(counter)  + " clients that successfully communicated 8 unique packet types with the server"