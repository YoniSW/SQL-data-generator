from distances import city
from random import randint



station_name = ["Eilat", "Beer-sheva", "Holon", "Tel-Aviv", "Haifa", "Jerusalem"]
CUSTOMER_TYPE = ["POLICE", "IDF", "AMBULANCE", "GOOGLE", "GOVERMENT", "MOSSAD", "INTEL", "SHABBAK", "TARA", "TNOOVA"]
line2station = [None]*100

def pairCity():
    src = station_name[(randint(0, 5))]
    dst = station_name[(randint(0, 5))]
    while src == dst:
        src = station_name[(randint(0, 5))]
        dst = station_name[(randint(0, 5))]
    return src + ", " + dst + ", " + str(city[str(src)][str(dst)])[:-12]

def ranDate(year):
    day = (randint(1, 30))
    month = (randint(1, 12))
    return str(day) +"-"+str(month)+"-"+str(year)


def createTrainStop(size):
    stationNum = 1
    f = open('TRAIN_STOP.txt', 'w')
    for x in range(0, size):
        row1 = "insert into YZADIK.TRAIN_STOP (STATION_NAME, NEXT_STATION, NEXT_STATION_DISTANCE)"
        row2 = "values ("+ pairCity() + ");"
        quary = row1 + '\n' + row2 + '\n\n'
        f.write(quary)
        stationNum += 1
    f.write("commit;")
    f.close()

def createTrainLine(size):
    lineNum = 1
    f = open('TRAIN_LINE.txt', 'w')
    for x in range(0, size):
        line2station[lineNum-1] = station_name[(randint(0, 5))]
        row1 = "insert into YZADIK.TRAIN_LINE (LINE_NUMBER, EXIT_STATION, TIMING, DATING)"
        row2 = "values (" + str(lineNum) + ", " + line2station[lineNum-1] + ", " + str((randint(0, 23))) + ", " + ranDate(2019) + ");"
        quary = row1 + '\n' + row2 + '\n\n'
        f.write(quary)
        lineNum += 1
    f.write("commit;")
    f.close()

def createCustomer(size):
    cusNum = 1
    f = open('CUSTOMER.txt', 'w')
    for x in range(0, size):
        row1 = "insert into YZADIK.CUSTOMER (CUSTOMER_NUMBER, CUSTOMER_TYPE)"
        row2 = "values (" + str(cusNum) + ", " + CUSTOMER_TYPE[(randint(0, 9))] + ");"
        quary = row1 + '\n' + row2 + '\n\n'
        f.write(quary)
        cusNum += 1
    f.write("commit;")
    f.close()


def createInvitation(size):
    num = 1
    f = open('INVITATION.txt', 'w')
    for x in range(0, size):
        row1 = "insert into YZADIK.INVITATION (LINE_NUMBER, CUSTOMER_NUMBER)"
        row2 = "values (" + str(randint(1, 100)) + ", " + str(randint(1, 100)) + ");"
        quary = row1 + '\n' + row2 + '\n\n'
        num += 1
        f.write(quary)
    f.write("commit;")
    f.close()

def createLineStops(size):
    num = 1
    f = open('LINES_STOPS.txt', 'w')
    row1 = "insert into YZADIK.LINES_STOPS (LINE_NUMBER, STATION_NAME)"
    row2 = "values (" + str(1) + ", " + str(line2station) + ");"
    quary = row1 + '\n' + row2 + '\n\n'
    num += 1
    f.write(quary)
    for x in range(0, size):
        rand = (randint(1, NUMBER_OF_ROWS))
        row1 = "insert into YZADIK.LINES_STOPS (LINE_NUMBER, STATION_NAME)"
        if line2station[rand - 1] == "SOLVED":
            row2 = "values (" + str(rand) + ", " + station_name[(randint(0, 5))] + ");"
        else:
            row2 = "values (" + str(rand) + ", " + str(line2station[rand-1]) + ");"
            line2station[rand - 1] = "SOLVED"
        quary = row1 + '\n' + row2 + '\n\n'
        num += 1
        f.write(quary)
    f.write("commit;")
    f.close()

NUMBER_OF_ROWS = 100

createTrainLine(NUMBER_OF_ROWS)
createTrainStop(NUMBER_OF_ROWS)
createCustomer(NUMBER_OF_ROWS)
createInvitation(NUMBER_OF_ROWS)
createLineStops(NUMBER_OF_ROWS)
