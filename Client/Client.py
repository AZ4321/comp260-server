import socket
import time

if __name__ == '__main__':
    isConnected = False
    mySocket = None

    isRunning = True

    while isRunning == True:
        while isConnected == False:

            if mySocket is None:
                mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                mySocket.connect(("127.0.0.1", 8222))
                isConnected = True
            except socket.error:
                isConnected = False

            if (isConnected == True):
                try:
                    testString = "You are now connected"
                    mySocket.send(testString.encode())
                except:
                    isConnected = False
                    mySocket = None

                    print("Server not found")
                    time.sleep(2.0)

        while isConnected == True:
            try:
                data = mySocket.recv(4096)
                print(data.decode("utf-8"))
            except:
                isConnected = False
mySocket = None

