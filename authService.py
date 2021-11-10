import time

CONST_DATABASE = "data.txt"
CONST_REQUEST = "request.txt"
CONST_RESPONSE = "response.txt"
CONST_REQUEST_FREQUENCY = 3


def main():
    while True:
        time.sleep(CONST_REQUEST_FREQUENCY)
        currentRequests = []

        #store request in list and delete txt file
        with open(CONST_REQUEST, "r") as filestream:
            line = filestream.readline()
            currentRequests = line.split(", ")
        clearRequest()

        if(currentRequests != []):
            if(currentRequests[0] == "read"):
                if(checkDatabaseForMatch(currentRequests[1], currentRequests[2], currentRequests[3]) == True):
                    writeTrue()
                else:
                    writeFalse()
            if(currentRequests[0] == "write"):
                writeNewData(currentRequests[1], currentRequests[2], currentRequests[3])
                writeTrue()

def checkDatabaseForMatch(username, service, task):
    currentRead = []
    with open(CONST_DATABASE, "r") as filestream:
        for line in filestream:
            currentline = line.split(", ")
            currentRead.append(currentline)
    for data in currentRead:
        if(username == data[0] and service == data[1], task == data[2]):
            return True
    return False


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

def writeNewData(userName, serviceName, taskName):
    with open("data.txt", "a") as filestream:
        filestream.write(userName + ", " + serviceName + ", " + taskName + "\n")
    return

def clearRequest():
    with open("request.txt", "w") as filestream:
        filestream.truncate(0)

if __name__ == "__main__":
    main()