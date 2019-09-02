####################defining length of all the parameters in dat file###################
routeHead_len=8
routeCount_len=4
offset_route_len=4
signCount_len=4
routeString_len=8
offset_sign_len=4
pageCount_len=4
signID_len=1
pageAddress_len=4
disp_style_1_attributes=12
disp_style_2_attributes=20
disp_style_3_attributes=20
disp_style_4_attributes=28

#######################Read DAT file########################
def readDAT(filename):
    with open(filename,'rb') as f:
        global data
        data=f.read()
    return data
#
#print(readDAT('RouteDB1.dat'))


# with open('RouteDB1.dat','rb') as f:
#     data=f.read()
#     for i in range(0,8):
#         print(data[i])

###################Read Route Head(first 8 bytes)####################
def readRouteHead():                            #This API will return the content of RouteHead in a list in int form
    route_Head=[]
    for i in range(routeHead_len):
        route_Head.append(data[i])
    return route_Head

#a=readRouteHead()
#print("Route Head: ",a)                         #52 6f 75 74 65 44 42 31
#print(hex(a[1]))
#print(len(readRouteHead()))

#################Read Route Count(next 4 bytes)########################
def readRouteCount():
    route_Count=[]
    for i in range(routeHead_len,routeHead_len+routeCount_len):
        route_Count.append(data[i])
    return route_Count

#b=readRouteCount()
#print("Route Count: ",b)                         #02 00 00 00

#################Read Offset Route(number of routes*4 bytes)###############
def readOffsetRoute():
    offset_route=[]
    for i in range(routeHead_len+routeCount_len,routeHead_len+routeCount_len+sum(readRouteCount())*(routeCount_len)):
        offset_route.append(data[i])
    return offset_route

#c=readOffsetRoute()
#print("Offset Route: ",c)



###############Read Sign Count(next 4 bytes)############################
def readSignCount():
    sign_Count=[]
    for i in range(routeHead_len+routeCount_len+len(readOffsetRoute()),routeHead_len+routeCount_len+len(readOffsetRoute())+signCount_len):
        sign_Count.append(data[i])
    return sign_Count

#d=readSignCount()
#print("Sign Count: ",d)                         # 02 00 00 00
#print("sum sign count:",sum(d))

###############Read Route String(next 8 bytes)##########################
def readRouteString():
    route_String=[]
    for i in range(routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount()),routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount())+routeString_len):
        route_String.append(data[i])
    return route_String

#e=readRouteString()
#print("Route String: ",e)

#########################Read Offset Sign(No. of sign counts*4 bytes)###########################
def readOffsetSign():
    offset_Sign=[]
    for i in range(routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount())+routeString_len,routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount())+routeString_len+sum(readSignCount())*offset_sign_len):
        offset_Sign.append(data[i])
    return offset_Sign

# f=readOffsetSign()
# print("Offset sign: ",f)

#####################################Read Page Count(4 bytes)###################################
def readPageCount():
    page_count=[]
    for i in range(routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount())+routeString_len+len(readOffsetSign()),routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount())+routeString_len+sum(readSignCount())*offset_sign_len+pageCount_len):
        page_count.append(data[i])
    return page_count

# g=readPageCount()
# print("Page Count: ",g)

###################################Read Sign ID(1 byte)#########################################
def readSignID():
    sign_id=[]
    start=routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount())+routeString_len+len(readOffsetSign())+len(readPageCount())
    end=routeHead_len+routeCount_len+len(readOffsetRoute())+len(readSignCount())+routeString_len+len(readOffsetSign())+len(readPageCount())+signID_len
    #print(start)
    #print(end)
    for i in range(start,end):
        sign_id.append(data[i])
    return sign_id

# h=readSignID()
# print("Sign ID: ",h)

##################################Read Offset Page################################################
def readOffsetPage():
    offset_page=[]
    start = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
        readOffsetSign()) + len(readPageCount())+signID_len
    end = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
        readOffsetSign()) + len(readPageCount()) + signID_len+(sum(readPageCount())*pageAddress_len)
    for i in range(start,end):
        offset_page.append(data[i])
    return offset_page

# i=readOffsetPage()
# print("Offset Page: ",i)



###################################################################################################
                #*****************BIT MAP DATA starts here*************#
###################################################################################################
def checkDisplayStyle():
    disp_style=[]
    start = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
        readOffsetSign()) + len(readPageCount()) + signID_len + len(readOffsetPage())
    end=start+1
    for i in range(start,end):
        disp_style.append(data[i])
    return disp_style

# print("Display style: ",checkDisplayStyle())

########################Read Page Attributes##############################

def readPageAttributes():
    if checkDisplayStyle()[0]==1:
        page_attributes=[]
        start = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
            readOffsetSign()) + len(readPageCount()) + signID_len + len(readOffsetPage())
        end=start+disp_style_1_attributes
        for i in range(start,end):
            page_attributes.append(data[i])
        return page_attributes

    elif checkDisplayStyle()[0]==2:
        page_attributes = []
        start = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
            readOffsetSign()) + len(readPageCount()) + signID_len + len(readOffsetPage())
        end = start + disp_style_2_attributes
        for i in range(start, end):
            page_attributes.append(data[i])
        return page_attributes

    elif checkDisplayStyle()[0]==3:
        page_attributes = []
        start = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
            readOffsetSign()) + len(readPageCount()) + signID_len + len(readOffsetPage())
        end = start + disp_style_3_attributes
        for i in range(start, end):
            page_attributes.append(data[i])
        return page_attributes

    elif checkDisplayStyle()[0]==4:
        page_attributes = []
        start = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
            readOffsetSign()) + len(readPageCount()) + signID_len + len(readOffsetPage())
        end = start + disp_style_4_attributes
        for i in range(start, end):
            page_attributes.append(data[i])
        return page_attributes

    else:
        print("Display style othen than 1,2,3,4")

# print("Page Attributes: ",readPageAttributes())

####################Read Data Width####################
def readDataWidth(page_attributes):
    if checkDisplayStyle()[0]==1:
        data_width=str(readPageAttributes()[10])+str(readPageAttributes()[9])
        return int(data_width)

    elif checkDisplayStyle()[0]==2:
        data_width1=str(readPageAttributes()[11])+str(readPageAttributes()[10])
        data_width2=str(readPageAttributes()[18])+str(readPageAttributes()[17])
        return int(data_width1)+int(data_width2)

    elif checkDisplayStyle()[0]==3:
        data_width1=str(readPageAttributes()[11])+str(readPageAttributes()[10])
        data_width2=str(readPageAttributes()[18])+str(readPageAttributes()[17])
        return int(data_width1)+int(data_width2)

    elif checkDisplayStyle()[0]==2:
        data_width1=str(readPageAttributes()[12])+str(readPageAttributes()[11])
        data_width2=str(readPageAttributes()[19])+str(readPageAttributes()[18])
        data_width3=str(readPageAttributes()[27])+str(readPageAttributes()[26])
        return int(data_width1)+int(data_width2)+int(data_width3)

# x=str(readPageAttributes()[10])+str(readPageAttributes()[9])
# print("x=",x)
#
# y=int(x)
# print("y=",y)

# print(readDataWidth(readPageAttributes()))

##################Read BitMap data########################
def readBitMap():
    bit_map=[]
    start = routeHead_len + routeCount_len + len(readOffsetRoute()) + len(readSignCount()) + routeString_len + len(
        readOffsetSign()) + len(readPageCount()) + signID_len + len(readOffsetPage())
    end=start+readDataWidth(readPageAttributes())+disp_style_1_attributes
    for i in range(start,end):
        bit_map.append(data[i])
    return bit_map

# print(readBitMap())
# print(len(readBitMap()))

#############################################################
#------------------Functions Execution----------------------#
#############################################################
readDAT('RouteDB1.dat')







