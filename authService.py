import time

def main():
    while True:
        time.sleep(3)
        currentRequests = []
        currentRead = []
        trueFlag = False
        #store request in list and delete txt file
        with open("request.txt", "r") as filestream:
            line = filestream.readline()
            currentRequests = line.split(", ")
        #with open("request.txt", "w") as filestream:
            #filestream.truncate(0)
        if(currentRequests != []):
            if(currentRequests[0] == "read"):
                with open("data.txt", "r") as filestream:
                    for line in filestream:
                        currentline = line.split(", ")
                        currentRead.append(currentline)
                for data in currentRead:
                    if(currentRequests[2] != data[2]):
                        print("yes it does")
                        print(currentRequests[2]) 
                        print(data[2])
                    if(currentRequests[1] == data[1] and currentRequests[2] == data[2]):
                        print(True)
                        writeTrue()
                        trueFlag = True
                    if(trueFlag == False):
                        writeFalse()
            if(currentRequests[0] == "write"):
                writeNewData(currentRequests[1], currentRequests[2])
                writeTrue()

def writeTrue():
    with open("response.txt", "w") as filestream:
        filestream.truncate(0)
        filestream.write("true")
    return

def writeFalse():
    with open("response.txt", "w") as filestream:
        filestream.truncate(0)
        filestream.write("false")
    return

def writeNewData(userName, serviceName):
    with open("data.txt", "a") as filestream:
        filestream.write(userName + ", " + serviceName + "\n")
    return

if __name__ == "__main__":
    main()





