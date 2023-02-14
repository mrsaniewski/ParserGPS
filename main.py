
from datetime import datetime
from prettytable import PrettyTable


print ("-------------------------P A R S E R------------------------------------------------------------------------------")


#TABELA 1 ZESTAW1
print ("TABELA 1 ZESTAW 1")
line = "$GPRMC,183729,A,3907.356,N,12102.482,W,000.0,360.0,080301,015.5,E*6F"
line = line.split(",")
if line[2] == "A":
    status = "Aktywny"
elif line[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"
data = datetime.strptime(line[9], '%d%m%y')
data = data.date()
czas = datetime.strptime(line[1], '%H%M%S')
czas = czas.time()
last = line[11]
last = last.split("*")
neededData1 = (data,czas,str(float(line[10]))+  "°" +  last[0],"-","-","-",last[1])
neededData2 = (line[3] + "' " + line[4], line[5] + "' " + line[6], float(line[7]),str(float(line[8])) + "º","-","-","-", "-","-","-",status)
neededData3 = ("-", "-", "-","-","-","-")





infsys1 = PrettyTable()

infsys1.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys1.add_row(neededData1)
print (infsys1)

pozurz1 = PrettyTable()

pozurz1.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz1.add_row(neededData2)
print (pozurz1)

dos1 = PrettyTable()

dos1.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos1.add_row(neededData3)
print (dos1)


#TABELA 2 ZESTAW 1

print ("TABELA 2 ZESTAW 1")
line2 = "$GPGGA,183730,3907.356,N,12102.482,W,1,05,1.6,646.4,M,-24.1,M,,*75"
line2 = line2.split(",")
czas = datetime.strptime(line2[1], '%H%M%S')
czas = czas.time()
last2 = line2[14]
last2 = last2.split("*")
neededData4 = (data,czas,str(float(line[10]))+  "°" +  last[0],line2[11] + "m","-",float(line2[6]),last2[1])
neededData5 = ([line[3] + "' " + line[4], line[5] + "' " + line[6],line[7],line[8],line2[9] + "m",line2[8],"-","-",line2[7],"-",status])
neededData6 = (["-","-","-","-","-","-"])


infsys2 = PrettyTable()

infsys2.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys2.add_row(neededData4)
print (infsys2)

pozurz2 = PrettyTable()

pozurz2.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz2.add_row(neededData5)
print (pozurz2)

dos2 = PrettyTable()

dos2.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos2.add_row(neededData6)
print (dos2)

#TABELA 3 ZESTAW 1

print ("TABELA 3 ZESTAW 1")
line3 = "$GPGSA,A,3,02,,,07,,09,24,26,,,,,1.6,1.6,1.0*3D"
line3 = line3.split(",")
if line3[1] == "A":
    sppozycji = "Automatyczny"
elif line3[1] == "M":
    sppozycji = "Manualny"
else:
    sppozycji = "-"
czas = datetime.strptime(line2[1], '%H%M%S')
czas = czas.time()
last3 = line3[17]
last3 = last3.split("*")
neededData7 = (data,czas,str(float(line[10]))+  "°" +  last[0],line2[11] + "m",sppozycji + "," + last3[1],float(line2[6]),last3[1])
neededData8 = ([line[3] + "' " + line[4], line[5] + "' " + line[6],line[7],line[8],line2[9] + "m",line3[15],last3[0],line3[16],line2[7],line3[3] + "," + line3[6] + "," + line3[8] + "," + line3[9] + "," + line3[10],status])
neededData9 = (["-","-","-","-","-","-"])


infsys3 = PrettyTable()

infsys3.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys3.add_row(neededData7)
print (infsys3)

pozurz3 = PrettyTable()

pozurz3.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz3.add_row(neededData8)
print (pozurz3)

dos3 = PrettyTable()

dos3.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos3.add_row(neededData9)
print (dos3)

#TABELA 4 ZESTAW 1

print ("TABELA 4 ZESTAW 1")
line4 = "$GPGSV,2,1,08,02,43,088,38,04,42,145,00,05,11,291,00,07,60,043,35*71"
line4 = line4.split(",")
if line3[1] == "A":
    sppozycji = "Automatyczny"
elif line3[1] == "M":
    sppozycji = "Manualny"
else:
    sppozycji = "-"
czas = datetime.strptime(line2[1], '%H%M%S')
czas = czas.time()
last4 = line4[19]
last4 = last4.split("*")
neededData10 = (data,czas,float(line[10]),float(line2[11]),sppozycji + "," + last3[1],float(line2[6]),last4[1])
neededData11 = ([line[3],line[5],line[7],line[8],line2[9],line3[15],last3[0],line3[16],line2[7],line3[3] + "," + line3[6] + "," + line3[8] + "," + line3[9] + "," + line3[10],status])
neededData121 = (["-","",line4[4],line4[5],line4[6],line4[7]])
neededData122 = (["-",line4[3],line4[8],line4[9],line4[10],line4[11]])
neededData123 = (["-","",line4[12],line4[13],line4[14],line4[15]])
neededData124 = (["-","",line4[16],line4[17],line4[18],last4[0]])

infsys4 = PrettyTable()

infsys4.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys4.add_row(neededData10)
print (infsys4)

pozurz4 = PrettyTable()

pozurz4.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz4.add_row(neededData11)
print (pozurz4)

dos4 = PrettyTable()

dos4.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos4.add_row(neededData121)
dos4.add_row(neededData122)
dos4.add_row(neededData123)
dos4.add_row(neededData124)

print (dos4)

#TABELA 5 ZESTAW 1

print ("TABELA 5 ZESTAW 1")
line5 = "$GPGSV,2,2,08,08,02,145,00,09,46,303,47,24,16,178,32,26,18,231,43*77"
line5 = line5.split(",")
if line3[1] == "A":
    sppozycji = "Automatyczny"
elif line3[1] == "M":
    sppozycji = "Manualny"
else:
    sppozycji = "-"
czas = datetime.strptime(line2[1], '%H%M%S')
czas = czas.time()
last5 = line5[19]
last5 = last5.split("*")
neededData13 = (data,czas,float(line[10]),float(line2[11]),sppozycji + "," + last3[1],float(line2[6]),last5[1])
neededData14 = ([line[3],line[5],line[7],line[8],line2[9],line3[15],last3[0],line3[16],line2[7],line3[3] + "," + line3[6] + "," + line3[8] + "," + line3[9] + "," + line3[10],status])
neededData151 = (["-","",line5[4],line5[5],line5[6],line5[7]])
neededData152 = (["-",line5[3],line5[8],line5[9],line5[10],line5[11]])
neededData153 = (["-","",line5[12],line5[13],line5[14],line5[15]])
neededData154 = (["-","",line5[16],line5[17],line5[18],last5[0]])

infsys5 = PrettyTable()

infsys5.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys5.add_row(neededData13)
print (infsys5)

pozurz5 = PrettyTable()

pozurz5.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz5.add_row(neededData14)
print (pozurz5)

dos5 = PrettyTable()

dos5.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos5.add_row(neededData151)
dos5.add_row(neededData152)
dos5.add_row(neededData153)
dos5.add_row(neededData154)

print (dos5)


#TABELA 6 ZESTAW 1

print ("TABELA 6 ZESTAW 1")
line6 = "$GPGLL,3907.360,N,12102.481,W,183730,A*33"
line6 = line6.split(",")
if line3[1] == "A":
    sppozycji = "Automatyczny"
elif line3[1] == "M":
    sppozycji = "Manualny"
else:
    sppozycji = "-"


czas = datetime.strptime(line2[1], '%H%M%S')
czas = czas.time()
czas61 = datetime.strptime(line6[5], '%H%M%S')
czas61 = czas61.time()
last6 = line6[6]
last6 = last6.split("*")
if last6[0] == "A":
    status = "Aktywny"
elif last6[0] == "V":
    status = "Nieaktywny"
else:
     status = "-"

neededData16 = (data,czas,float(line[10]),float(line2[11]),sppozycji + "," + last3[1],float(line2[6]),last6[1])
neededData17 = ([czas61,line6[3],line[7],line[8],line2[9],line3[15],last3[0],line3[16],line2[7],line3[3] + "," + line3[6] + "," + line3[8] + "," + line3[9] + "," + line3[10],status])
neededData181 = (["","",line5[4],line5[5],line5[6],line5[7]])
neededData182 = ([czas61,line5[3],line5[8],line5[9],line5[10],line5[11]])
neededData183 = (["","",line5[12],line5[13],line5[14],line5[15]])
neededData184 = (["","",line5[16],line5[17],line5[18],last5[0]])

infsys6 = PrettyTable()

infsys6.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys6.add_row(neededData16)
print (infsys6)

pozurz6 = PrettyTable()

pozurz6.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz6.add_row(neededData17)
print (pozurz6)

dos6 = PrettyTable()

dos6.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos6.add_row(neededData181)
dos6.add_row(neededData182)
dos6.add_row(neededData183)
dos6.add_row(neededData184)

print (dos6)

#TABELA 7 ZESTAW 1

print ("TABELA 7 ZESTAW 1")
line7 = "$GPRMC,183731,A,3907.482,N,12102.436,W,000.0,360.0,080301,015.5,E*67"
line7 = line7.split(",")
if line3[1] == "A":
    sppozycji = "Automatyczny"
elif line3[1] == "M":
    sppozycji = "Manualny"
else:
    sppozycji = "-"


czas7 = datetime.strptime(line7[1], '%H%M%S')
czas7 = czas7.time()
data7 = datetime.strptime(line7[9], '%d%m%y')
data7 = data7.date()
last7 = line7[11]
last7 = last7.split("*")
if last6[0] == "A":
    status = "Aktywny"
elif last6[0] == "V":
    status = "Nieaktywny"
else:
     status = "-"

neededData16 = (data,czas7,str(float(line7[10]))+  "°" +  last7[0],line2[11] + "m",sppozycji + "," + last3[1],float(line2[6]),last7[1])
neededData17 = ([line7[3],line7[5],line7[7],line7[8],line2[9],line3[15],last3[0],line3[16],line2[7],line3[3] + "," + line3[6] + "," + line3[8] + "," + line3[9] + "," + line3[10],status])
neededData181 = (["","",line5[4],line5[5],line5[6],line5[7]])
neededData182 = ([czas61,line5[3],line5[8],line5[9],line5[10],line5[11]])
neededData183 = (["","",line5[12],line5[13],line5[14],line5[15]])
neededData184 = (["","",line5[16],line5[17],line5[18],last5[0]])

infsys7 = PrettyTable()

infsys7.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys7.add_row(neededData16)
print (infsys7)

pozurz7 = PrettyTable()

pozurz7.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz7.add_row(neededData17)
print (pozurz7)

dos7 = PrettyTable()

dos7.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos7.add_row(neededData181)
dos7.add_row(neededData182)
dos7.add_row(neededData183)
dos7.add_row(neededData184)

print (dos7)

### KONIEC ZESTAWU 1 ########################################

#TABELA 1 ZESTAW 2
print ("\n\n\n\n\n\n\n\nTABELA 1 ZESTAW 2")
line21 = "$GPRMC,002454,A,3553.5295,N,13938.6570,E,0.0,43.1,180700,7.1,W,A*3F"
line21 = line21.split(",")
if line21[2] == "A":
    status = "Aktywny"
elif line21[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"
data21 = datetime.strptime(line21[9], '%d%m%y')
data21 = data21.date()
czas21 = datetime.strptime(line21[1], '%H%M%S')
czas21 = czas21.time()
last21 = line21[12]
last21 = last21.split("*")
neededData21 = (data21,czas21,str(float(line21[10]))+line21[11],"-","-","-",last21[1])
neededData22 = (line21[3] + "' " + line21[4], line21[5] + "' " + line21[6], float(line21[7]),str(float(line21[8])) + "º","-","-","-", "-","-","-",status)
neededData23 = ("-", "-", "-","-","-","-")





infsys21 = PrettyTable()

infsys21.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys21.add_row(neededData21)
print (infsys21)

pozurz21 = PrettyTable()

pozurz21.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz21.add_row(neededData22)
print (pozurz21)

dos21 = PrettyTable()

dos21.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos21.add_row(neededData23)
print (dos21)

#TABELA 2 ZESTAW 2
print ("TABELA 2 ZESTAW 2")
line22 = "$GPGGA,002454,3553.5295,N,13938.6570,E,1,05,2.2,18.3,M,39.0,M,,*7F"
line22 = line22.split(",")
if line21[2] == "A":
    status = "Aktywny"
elif line21[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"
data21 = datetime.strptime(line21[9], '%d%m%y')
data21 = data21.date()
czas22 = datetime.strptime(line22[1], '%H%M%S')
czas22 = czas22.time()
last22 = line22[14]
last22 = last22.split("*")
neededData24 = (data21,czas22,str(float(line21[10]))+line21[11],line22[11],"-",line22[6],last22[1])
neededData25 = (line22[2] + "' " + line22[3], line22[4] + "' " + line22[5], float(line21[7]),str(float(line21[8])) + "º",line22[9],line22[8],"-", "-",line22[7],"-",status)
neededData26 = ("-", "-", "-","-","-","-")





infsys22 = PrettyTable()

infsys22.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys22.add_row(neededData24)
print (infsys22)

pozurz22 = PrettyTable()

pozurz22.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz22.add_row(neededData25)
print (pozurz22)

dos22 = PrettyTable()

dos22.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos22.add_row(neededData26)
print (dos22)

#TABELA 3 ZESTAW 2
print ("TABELA 3 ZESTAW 2")
line23 = "$GPGSA,A,3,01,04,07,16,20,,,,,,,,3.6,2.2,2.7*35"
line23 = line23.split(",")
if line21[2] == "A":
    status = "Aktywny"
elif line21[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line23[1] == "A":
    sppozycji2 = "Automatyczny"
elif line23[1] == "M":
     sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data21 = datetime.strptime(line21[9], '%d%m%y')
data21 = data21.date()
czas22 = datetime.strptime(line22[1], '%H%M%S')
czas22 = czas22.time()
last23 = line23[17]
last23 = last23.split("*")

if line23[2] == "3":
    wymiar = "3D"
else:
     wymiar = "-"

neededData27 = (data21,czas22,str(float(line21[10]))+line21[11],line22[11],sppozycji2 + "," + wymiar,line22[6],last23[1])
neededData28 = (line22[2] + "' " + line22[3], line22[4] + "' " + line22[5], float(line21[7]),str(float(line21[8])) + "º",line22[9],line23[16],last23[0], line23[15],line22[7],line23[3] + ","+line23[4] + "," +line23[5] + "," +line23[6] + ","+line23[7],status)
neededData29 = ("-", "-", "-","-","-","-")





infsys23 = PrettyTable()

infsys23.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys23.add_row(neededData27)
print (infsys23)

pozurz23 = PrettyTable()

pozurz23.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz23.add_row(neededData28)
print (pozurz23)

dos23 = PrettyTable()

dos23.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos23.add_row(neededData29)
print (dos23)

#TABELA 4 ZESTAW 2
print ("TABELA 4 ZESTAW 2")
line24 = "$GPGSV,3,1,09,01,38,103,37,02,23,215,00,04,38,297,37,05,00,328,00*70"
line24 = line24.split(",")
if line21[2] == "A":
    status = "Aktywny"
elif line21[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line23[1] == "A":
    sppozycji2 = "Automatyczny"
elif line23[1] == "M":
     sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data21 = datetime.strptime(line21[9], '%d%m%y')
data21 = data21.date()
czas22 = datetime.strptime(line22[1], '%H%M%S')
czas22 = czas22.time()
last24 = line24[19]
last24 = last24.split("*")

if line23[2] == "3":
    wymiar = "3D"
else:
     wymiar = "-"

neededData30 = (data21,czas22,str(float(line21[10]))+line21[11],line22[11],sppozycji2 + "," + wymiar,line22[6],last24[1])
neededData31 = (line22[2] + "' " + line22[3], line22[4] + "' " + line22[5], float(line21[7]),str(float(line21[8])) + "º",line22[9],line23[16],last23[0], line23[15],line22[7],line23[3] + ","+line23[4] + "," +line23[5] + "," +line23[6] + ","+line23[7],status)
neededData321 = ("-", "", line24[4],line24[5],line24[6],line24[7])
neededData322 = ("-", line24[3], line24[8],line24[9],line24[10],line24[11])
neededData323 = ("-", "", line24[12],line24[13],line24[14],line24[15])
neededData324 = ("-", "", line24[16],line24[17],line24[18],last24[0])



infsys24 = PrettyTable()

infsys24.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys24.add_row(neededData30)
print (infsys24)

pozurz24 = PrettyTable()

pozurz24.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz24.add_row(neededData31)
print (pozurz24)

dos24 = PrettyTable()

dos24.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos24.add_row(neededData321)
dos24.add_row(neededData322)
dos24.add_row(neededData323)
dos24.add_row(neededData324)
print (dos24)

#TABELA 5 ZESTAW 2
print ("TABELA 5 ZESTAW 2")
line25 = "$GPGSV,3,2,09,07,77,299,47,11,07,087,00,16,74,041,47,20,38,044,43*73"
line25 = line25.split(",")
if line21[2] == "A":
    status = "Aktywny"
elif line21[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line23[1] == "A":
    sppozycji2 = "Automatyczny"
elif line23[1] == "M":
     sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data21 = datetime.strptime(line21[9], '%d%m%y')
data21 = data21.date()
czas22 = datetime.strptime(line22[1], '%H%M%S')
czas22 = czas22.time()
last25 = line25[19]
last25 = last25.split("*")

if line23[2] == "3":
    wymiar = "3D"
else:
     wymiar = "-"

neededData33 = (data21,czas22,str(float(line21[10]))+line21[11],line22[11],sppozycji2 + "," + wymiar,line22[6],last25[1])
neededData34 = (line22[2] + "' " + line22[3], line22[4] + "' " + line22[5], float(line21[7]),str(float(line21[8])) + "º",line22[9],line23[16],last23[0], line23[15],line22[7],line23[3] + ","+line23[4] + "," +line23[5] + "," +line23[6] + ","+line23[7],status)
neededData351 = ("-", "", line25[4],line25[5],line25[6],line25[7])
neededData352 = ("-", line25[3], line25[8],line25[9],line25[10],line25[11])
neededData353 = ("-", "", line25[12],line25[13],line25[14],line25[15])
neededData354 = ("-", "", line25[16],line25[17],line25[18],last25[0])



infsys25 = PrettyTable()

infsys25.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys25.add_row(neededData30)
print (infsys25)

pozurz25 = PrettyTable()

pozurz25.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz25.add_row(neededData31)
print (pozurz25)

dos25 = PrettyTable()

dos25.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos25.add_row(neededData351)
dos25.add_row(neededData352)
dos25.add_row(neededData353)
dos25.add_row(neededData354)
print (dos25)

#TABELA 6 ZESTAW 2
print ("TABELA 6 ZESTAW 2")
line26 = "$GPGSV,3,3,09,24,12,282,00*4D"
line26 = line26.split(",")
if line21[2] == "A":
    status = "Aktywny"
elif line21[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line23[1] == "A":
    sppozycji2 = "Automatyczny"
elif line23[1] == "M":
     sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data21 = datetime.strptime(line21[9], '%d%m%y')
data21 = data21.date()
czas22 = datetime.strptime(line22[1], '%H%M%S')
czas22 = czas22.time()
last26 = line26[7]
last26 = last26.split("*")

if line23[2] == "3":
    wymiar = "3D"
else:
     wymiar = "-"

neededData36 = (data21,czas22,str(float(line21[10]))+line21[11],line22[11],sppozycji2 + "," + wymiar,line22[6],last26[1])
neededData37 = (line22[2] + "' " + line22[3], line22[4] + "' " + line22[5], float(line21[7]),str(float(line21[8])) + "º",line22[9],line23[16],last23[0], line23[15],line22[7],line23[3] + ","+line23[4] + "," +line23[5] + "," +line23[6] + ","+line23[7],status)
neededData38 = ("-", line26[3], line26[4],line26[5],line26[6],last26[0])




infsys26 = PrettyTable()

infsys26.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys26.add_row(neededData36)
print (infsys26)

pozurz26 = PrettyTable()

pozurz26.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz26.add_row(neededData37)
print (pozurz26)

dos26 = PrettyTable()

dos26.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos26.add_row(neededData38)
print (dos26)

#TABELA 7 ZESTAW 2
print ("TABELA 7 ZESTAW 2")
line27 = "$GPGLL,3553.5295,N,13938.6570,E,002454,A,A*4F"
line27 = line27.split(",")
if line27[6] == "A":
    status = "Aktywny"
elif line27[6] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line23[1] == "A":
    sppozycji2 = "Automatyczny"
elif line23[1] == "M":
     sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data21 = datetime.strptime(line21[9], '%d%m%y')
data21 = data21.date()
czas22 = datetime.strptime(line22[1], '%H%M%S')
czas22 = czas22.time()
czas72 = datetime.strptime(line27[5], '%H%M%S')
czas72 = czas72.time()
last27 = line27[7]
last27 = last27.split("*")

if line23[2] == "3":
    wymiar = "3D"
else:
     wymiar = "-"

neededData39 = (data21,czas22,str(float(line21[10]))+line21[11],line22[11],sppozycji2 + "," + wymiar,line22[6],last27[1])
neededData40 = (line27[1] + "' " + line27[2], line27[3] + "' " + line27[4], float(line21[7]),str(float(line21[8])) + "º",line22[9],line23[16],last23[0], line23[15],line22[7],line23[3] + ","+line23[4] + "," +line23[5] + "," +line23[6] + ","+line23[7],status)
neededData41 = (czas72, line26[3], line26[4],line26[5],line26[6],last26[0])




infsys27 = PrettyTable()

infsys27.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys27.add_row(neededData39)
print (infsys27)

pozurz27 = PrettyTable()

pozurz27.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz27.add_row(neededData40)
print (pozurz27)

dos27 = PrettyTable()

dos27.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos27.add_row(neededData41)
print (dos27)

#TABELA 8 ZESTAW 2
print ("TABELA 8 ZESTAW 2")
line28 = "$GPRMC,002456,A,3553.5295,N,13938.6570,E,0.0,43.1,180700,7.1,W,A*3D"
line28 = line28.split(",")
if line28[2] == "A":
    status = "Aktywny"
elif line28[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line23[1] == "A":
    sppozycji2 = "Automatyczny"
elif line23[1] == "M":
     sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data28 = datetime.strptime(line28[9], '%d%m%y')
data28 = data28.date()
czas28 = datetime.strptime(line28[1], '%H%M%S')
czas28 = czas28.time()
last28 = line28[12]
last28 = last28.split("*")

if line23[2] == "3":
    wymiar = "3D"
else:
     wymiar = "-"

neededData42 = (data28,czas28,str(float(line28[10]))+line28[11],line22[11],sppozycji2 + "," + wymiar,line22[6],last28[1])
neededData43 = (line28[3] + "' " + line28[4], line28[5] + "' " + line28[6], float(line28[7]),str(float(line28[8])) + "º",line22[9],line23[16],last23[0], line23[15],line22[7],line23[3] + ","+line23[4] + "," +line23[5] + "," +line23[6] + ","+line23[7],status)
neededData44 = (czas72, line26[3], line26[4],line26[5],line26[6],last26[0])




infsys28 = PrettyTable()

infsys28.field_names = ["Data","Czas","Odchylenie magnetyczne Ziemi","Wysokość geoid","Sposób określenia pozycji","Jakość pomiaru","Suma kontrolna"]
infsys28.add_row(neededData42)
print (infsys28)

pozurz28 = PrettyTable()

pozurz28.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się", "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)", "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz28.add_row(neededData43)
print (pozurz28)

dos28 = PrettyTable()

dos28.field_names = ["Czas ustalania pozycji","Liczba widocznych satelitów","ID satelity (numer)","Wyniesienie nadrównik (w stopniach)","Azymut satelity (w stopniach)", "Stosunek sygnał/szum (SNR) satelity"]
dos28.add_row(neededData44)
print (dos28)


# TABELA 1 ZESTAW 3
print("\n\n\n\n\n\n\n\nTABELA 1 ZESTAW 3")
line30 = "$GPGGA,023042,3907.3837,N,12102.4684,W,1,04,2.3,507.3,M,-24.1,M,,*75"
line30 = line30.split(",")
if line28[2] == "A":
    status = "Aktywny"
elif line28[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line23[1] == "A":
    sppozycji2 = "Automatyczny"
elif line23[1] == "M":
    sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data28 = datetime.strptime(line28[9], '%d%m%y')
data28 = data28.date()
czas30 = datetime.strptime(line30[1], '%H%M%S')
czas30 = czas30.time()
last30 = line30[14]
last30 = last30.split("*")

if line23[2] == "3":
    wymiar = "3D"
else:
    wymiar = "-"

neededData45 = ("-", czas30,"-", line30[11], "-", line30[6], last30[1])
neededData46 = (line30[2] + "' " + line30[3], line30[4] + "' " + line30[5], "-","-", line30[9],line30[8], "-", "-", line30[7],"-", "-")
neededData47 = ("-", "-", "-", "-", "-", "-")

infsys30 = PrettyTable()

infsys30.field_names = ["Data", "Czas", "Odchylenie magnetyczne Ziemi", "Wysokość geoid", "Sposób określenia pozycji",
                        "Jakość pomiaru", "Suma kontrolna"]
infsys30.add_row(neededData45)
print(infsys30)

pozurz30 = PrettyTable()

pozurz30.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się",
                        "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)",
                        "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz30.add_row(neededData46)
print(pozurz30)

dos30 = PrettyTable()

dos30.field_names = ["Czas ustalania pozycji", "Liczba widocznych satelitów", "ID satelity (numer)",
                     "Wyniesienie nadrównik (w stopniach)", "Azymut satelity (w stopniach)",
                     "Stosunek sygnał/szum (SNR) satelity"]
dos30.add_row(neededData47)
print(dos30)

# TABELA 2 ZESTAW 3
print("TABELA 2 ZESTAW 3")
line32 = "$GPGSA,A,3,04,05,,,09,,,24,,,,,2.8,2.3,1.0*36"
line32 = line32.split(",")
if line28[2] == "A":
    status = "Aktywny"
elif line28[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line32[1] == "A":
    sppozycji2 = "Automatyczny"
elif line32[1] == "M":
    sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data28 = datetime.strptime(line28[9], '%d%m%y')
data28 = data28.date()
czas30 = datetime.strptime(line30[1], '%H%M%S')
czas30 = czas30.time()
last32 = line32[17]
last32 = last32.split("*")

if line32[2] == "3":
    wymiar = "3D"
else:
    wymiar = "-"

neededData48 = ("-", czas30,"-", line30[11], sppozycji2 + "," + wymiar, line30[6], last32[1])
neededData49 = (line30[2] + "' " + line30[3], line30[4] + "' " + line30[5], "-","-", line30[9],line32[16], last32[0], line32[15], "-",line32[3] + "," + line32[4] + "," + line32[7] + ","+ line32[10] ,"-")
neededData50 = ("-", "-", "-", "-", "-", "-")

infsys32 = PrettyTable()

infsys32.field_names = ["Data", "Czas", "Odchylenie magnetyczne Ziemi", "Wysokość geoid", "Sposób określenia pozycji",
                        "Jakość pomiaru", "Suma kontrolna"]
infsys32.add_row(neededData48)
print(infsys32)

pozurz32 = PrettyTable()

pozurz32.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się",
                        "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)",
                        "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz32.add_row(neededData49)
print(pozurz32)

dos32 = PrettyTable()

dos32.field_names = ["Czas ustalania pozycji", "Liczba widocznych satelitów", "ID satelity (numer)",
                     "Wyniesienie nadrównik (w stopniach)", "Azymut satelity (w stopniach)",
                     "Stosunek sygnał/szum (SNR) satelity"]
dos32.add_row(neededData50)
print(dos32)

# TABELA 3 ZESTAW 3
print("TABELA 3 ZESTAW 3")
line33 = "$GPVTG,156.1,T,140.9,M,0.0,N,0.0,K*41"
line33 = line33.split(",")
if line28[2] == "A":
    status = "Aktywny"
elif line28[2] == "V":
    status = "Nieaktywny"
else:
    status = "-"

if line32[1] == "A":
    sppozycji2 = "Automatyczny"
elif line32[1] == "M":
    sppozycji2 = "Manualny"
else:
    sppozycji2 = "-"

data28 = datetime.strptime(line28[9], '%d%m%y')
data28 = data28.date()
czas30 = datetime.strptime(line30[1], '%H%M%S')
czas30 = czas30.time()
last33 = line33[8]
last33 = last33.split("*")

if line32[2] == "3":
    wymiar = "3D"
else:
    wymiar = "-"

neededData51 = ("-", czas30,"-", line30[11] + "m", sppozycji2 + "," + wymiar, line30[6], last33[1])
neededData52 = (line30[2] + "' " + line30[3], line30[4] + "' " + line30[5], line33[5],"-", line30[9] + "m",line32[16], last32[0], line32[15], "-",line32[3] + "," + line32[4] + "," + line32[7] + ","+ line32[10] ,"-")
neededData53 = ("-", "-", "-", "-", "-", "-")

infsys33 = PrettyTable()

infsys33.field_names = ["Data", "Czas", "Odchylenie magnetyczne Ziemi", "Wysokość geoid", "Sposób określenia pozycji",
                        "Jakość pomiaru", "Suma kontrolna"]
infsys33.add_row(neededData51)
print(infsys33)

pozurz33 = PrettyTable()

pozurz33.field_names = ["Szerokość geograficzna", "Długość geograficzna", "Prędkość", "Kąt przemieszczania się",
                        "Wysokość n.p.m.", "Precyzja horyzontalna", "Precyzja wertykalna", "Precyzja (ogólnie)",
                        "Liczba śledzonych satelitów", "Numery satelitów do pozycji", "Status urządzenia"]
pozurz33.add_row(neededData52)
print(pozurz33)

print("Ścieżka poruszania się(w stopniach):" + line33[1])
print("Ścieżka poruszania się na podstawie danych magnetycznych(w stopniach):" + line33[3])
print("Prędkość (w km/h):" + line33[7])

dos33 = PrettyTable()

dos33.field_names = ["Czas ustalania pozycji", "Liczba widocznych satelitów", "ID satelity (numer)",
                     "Wyniesienie nadrównik (w stopniach)", "Azymut satelity (w stopniach)",
                     "Stosunek sygnał/szum (SNR) satelity"]
dos33.add_row(neededData53)
print(dos33)