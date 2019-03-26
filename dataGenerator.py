import random
import time

def randgenerate(randData,start,end,numbersub):
    type=[]
    for x in range(numbersub):
        type.append(random.randint(start,end))
    for i in range(0,10000000):
        randData.append(type[random.randrange(len(type))])

def randUserID(type,randData):
    for i in range(0,10000000):
        randData.append(type[random.randrange(len(type))])

def randService(type,start,end):
    randData=[]
    i = random.randint(start,end)
    for k in range(0,i):
        randData.append(type[random.randrange(len(type))])
    service =""
    for i in randData:
        service += "    <" + str(i) + ">1</"+ str(i) + ">\n";
    return service

if __name__ == '__main__':
    random_mdn=[]
    random_deviceID=[]
    random_dialedNumber=[]
    random_UserID=[]
    random_direction=[]
    random_callType=[]
    random_location=[]
    random_callingNumber=[]
    random_service=[]
    randgenerate(random_mdn,560000000,600000000,100000)
    randgenerate(random_deviceID,660000000,800000000,100000)
    randgenerate(random_dialedNumber,432000000,444000000,100000)
    type_device = ['apple','android','apple','apple','apple','apple','android']
    randUserID(type_device,random_UserID)
    type_direction = ['incoming','outgoing','incoming','incoming','incoming','outgoing','outgoing']
    randUserID(type_direction, random_direction)
    type_callType =['local' , 'non-local', 'national', 'international', 'interlata', 'interlatatoll' , 'nanpinternational', 'nanpinternational', 'international', 'international', 'international','local','local']
    randUserID(type_callType,random_callType)
    randgenerate(random_location, 311004000,322012220,500)
    randgenerate(random_callingNumber,432000000,444000000,100000)
    type_service=['FCD','DEFLECTION','CDIV','BARRING','DBL','MCID','CONF','COMWAIT','STOD','OIP','OIR','TIP','TIR','CNIP','FIP','OCNIP','SSC','MCID','ABDIAL','CAC','CARRIER_SELECTvCARRIER_PRE_SELECT','CC','FSFS','CUG',
               'UCD','IDPRES','PTY','SND','ANN','POLICING','ECT','CPC','PX','CAT','CR','HOTLINE','DNM','MSN','DR','OCT']
    val=100000
    for j in range(0,9):
      publishBody=""
      publishBody += "<call-event-info>\n";
      for i in range(j*val+1, (j+1)*val):
        service_string = randService(type_service,0,5)
        publishBody += "  <reason>\n";
        publishBody += "    <mdn>" + str(random_mdn[i]) + "</mdn>\n";
        publishBody += "    <deviceID>" + str(random_deviceID[i]) + "</deviceID>\n";
        publishBody += "    <dialedNumber>" + "+" + str(random_dialedNumber[i]) + "</dialedNumber>\n";
        publishBody += "    <userAgent>" + str(random_UserID[i]) + "</userAgent>\n";
        publishBody += "    <direction>" + str(random_direction[i]) + "</direction>\n";
        publishBody += "    <callType>" + str(random_callType[i]) + "</callType>\n";
        publishBody += "    <location>" + str(random_location[i]) + "</location>\n";
        publishBody += "    <callingNumber>" + str(random_callingNumber[i]) + "</callingNumber>\n";
        publishBody += "    <timestamp>" + str(time.time()) + "</timestamp>\n"
        publishBody += service_string
        publishBody += "  </reason>\n";
      publishBody += "</call-event-info>\n";
      with open("log" + str(j) + ".txt", "a") as myfile:
            myfile.write(publishBody)
