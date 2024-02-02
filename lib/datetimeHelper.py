
from datetime import datetime
from enum import Enum
from PyQt6 import QtCore 
from PyQt6.QtCore import QDateTime,Qt



class ThaiMonthLongName(Enum): 
    Jan = 1,"มกราคม","ม.ค."
    Feb = 2,"กุมภาพันธุ์","ก.พ."
    Mar = 3,"มีนาคม","มี.ค."
    Apr = 4,"เมษายน","เมย."
    May = 5,"พฤษภาคม","พ.ค."
    Jun = 6,"มิถุนายน","มิ.ย."
    Jul = 7,"กรกฏาคม","ก.ค."
    Aug = 8,"สิงหาคม","ส.ค."
    Sep = 9,"กันยายน","ก.ย."
    Oct = 10,"ตุลาคม","ต.ค."
    Nov = 11,"พฤศจิกายน","พ.ย."
    Dec = 12,"ธันวาคม","ธ.ค."

class ShowTime():
    NotShow = 1
    Long = 2
    Short = 3


class ThaiDateTime(QDateTime):

    def __init__(self):
        super().__init__()
        self.now = self.currentDateTime()
        self.today = self.now.date().currentDate()
        self.totime = self.now.time().currentTime() 
        self.localDateTime = self.now.toString(Qt.DateFormat.ISODate)
        self.dtToUTC = self.now.toUTC().toString(Qt.DateFormat.ISODate)
        self.dtToOffsetUTC = self.now.offsetFromUtc()


    def set2digit(self,value):

        if len(str(value)) < 2:
            return f"0{value}"
        else:
            return value
        
    def getMonthLongName(self,monthNo : int,showLongName: bool = True):

        for item in list(ThaiMonthLongName):
            if item.value[0] == monthNo:
                if showLongName == True:
                    return item.value[1]
                else:
                    return item.value[2]
        
        return "NOT_FOUNT[{monthNo}]"

    def toThaiDate(self) -> str : 
        _year   = self.now.date().year()
        _month  = self.set2digit(self.now.date().month())
        _day    = self.set2digit(self.now.date().day())
        
        _yearThai = _year + 543

        return f"{_day}/{_month}/{_yearThai}"
    

    def toThaiDateTime(self):
        _year   = self.now.date().year()
        _month  = self.set2digit(self.now.date().month())
        _day    = self.set2digit(self.now.date().day())
        
        _yearThai = _year + 543

        _hr   = self.set2digit(self.now.time().hour())
        _min  = self.set2digit(self.now.time().minute())
        _sec  = self.set2digit(self.now.time().second())

        return f"{_day}/{_month}/{_yearThai} {_hr}:{_min}:{_sec}"


    def toThaiDateTimeName(self,
                        showTime : ShowTime = ShowTime.NotShow,
                        showLongName = True,
                        delimieter : str = " "
                        ):
        _year   = self.now.date().year()
        _month  = self.getMonthLongName(self.now.date().month(),showLongName=showLongName)
        _day    = self.set2digit(self.now.date().day())
        
        _yearThai = _year + 543

        _hr   = self.set2digit(self.now.time().hour())
        _min  = self.set2digit(self.now.time().minute())
        _sec  = self.set2digit(self.now.time().second())

        if showTime == ShowTime.NotShow:
            return f"{_day}{delimieter}{_month}{delimieter}{_yearThai}"    
        elif  showTime == ShowTime.Long:
            return f"{_day}{delimieter}{_month}{delimieter}{_yearThai} {_hr}:{_min}:{_sec}"
        else:
            return f"{_day}{delimieter}{_month}{delimieter}{_yearThai} {_hr}:{_min}"            



    def formatDateTime(self,format):
        _datetime = self.now.toString(format)
        return _datetime
        

    def toPyDateTime(self) -> datetime:
        return self.now.toPyDateTime()


    def toPyDate(self) -> datetime.date:
        return self.today.toPyDate()


dt=ThaiDateTime()

print(f"now = {dt.now}")
print(f"date = {dt.date}")
print(f"time = {dt.time}")
print(f"localDateTime = {dt.localDateTime}")
print(f"datetimeUTC = {dt.dtToUTC}")
print(f"datetimeSecond = {dt.dtToOffsetUTC}")
print(f"toThaiDate = {dt.toThaiDate()}")
print(f"toThaiDateTime = {dt.toThaiDateTime()}")
print(f"toThaiDateTimeFormat = {dt.formatDateTime('dd-MM-yyyy')}")
print(f"toPyDateTime = {dt.toPyDateTime()}")
print(f"toPyDate = {dt.toPyDate()}")

print(f"toThaiDateTimeName = {dt.toThaiDateTimeName()}")
print(f"toThaiDateTimeName = {dt.toThaiDateTimeName(showLongName=False)}")
print(f"toThaiDateTimeName = {dt.toThaiDateTimeName(ShowTime.Long)}")
print(f"toThaiDateTimeName = {dt.toThaiDateTimeName(ShowTime.Short)}")