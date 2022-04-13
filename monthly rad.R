
setwd("C:\\Users\\wchc3a\\OneDrive - AdventHealth\\ead\\R")
library(readxl)
Book8 = read_excel("H:\\Qa\\QA_SHARED\\vicky chen\\data\\monthly financial report - Rad\\Book8.xlsx", 
                          col_types = c("text", "text", "text", 
                                                 "text", "text", "text", "text", "text", 
                                                "text", "text", "text", "text", "text", 
                                                "text", "numeric", "text", "numeric", 
                                                "numeric", "numeric", "numeric"))
a=data.frame(Book8)
a["MTD/YTD"]="MTD"
str(a)
summary(a)

library(dplyr)

a=mutate(a,key=paste(Unit,Descr...2 ,Dept,Descr...4,Tree.Name,
                     Tree.Node,Parent.Node,Oper.Unit,Descr...9,
                     Account,Descr...11,Director.OPRID,Descr...13,
                     Fiscal.Year))
str(a)
a18=filter(a,Fiscal.Year ==2018)
a19=filter(a,Fiscal.Year ==2019)
a20=filter(a,Fiscal.Year ==2020)
#a18=mutate(a18,Period1 = as.numeric(Period))
#a19=mutate(a19,Period1 = as.numeric(Period))
#a20=mutate(a20,Period1 = as.numeric(Period))

#keep2018=c("key","Period1" ,"ACTUAL" ,"BUDGET","BUDGETFLEX","MTD/YTD")
#a18 = a2018[keep2018]
#keep2019=c("key","Period1" ,"ACTUAL" ,"BUDGET","BUDGETFLEX","MTD/YTD")
#a19 = a2019[keep2019]
#keep2020=c("key","Period1" ,"ACTUAL" ,"BUDGET","BUDGETFLEX","MTD/YTD")
#a20 = a2020[keep2020]

b1812=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 12],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 12],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 12],na.rm=T))

b1812["MTD/YTD"]="YTD"
b1812["Peroid"]="12"

b1811=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 11],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 11],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 11],na.rm=T))

b1811["MTD/YTD"]="YTD"
b1811["Peroid"]="11"

b1810=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 10],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 10],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 10],na.rm=T))

b1810["MTD/YTD"]="YTD"
b1810["Peroid"]="10"


b189=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 9],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 9],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 9],na.rm=T))

b189["MTD/YTD"]="YTD"
b189["Peroid"]="9"

b188=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 8],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 8],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 8],na.rm=T))

b188["MTD/YTD"]="YTD"
b188["Peroid"]="8"  

b187=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 7],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 7],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 7],na.rm=T))

b187["MTD/YTD"]="YTD"
b187["Peroid"]="7" 

b186=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 6],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 6],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 6],na.rm=T))

b186["MTD/YTD"]="YTD"
b186["Peroid"]="6"   

b185=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 5],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 5],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 5],na.rm=T))

b185["MTD/YTD"]="YTD"
b185["Peroid"]="5"  

b184=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 4],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 4],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 4],na.rm=T))

b184["MTD/YTD"]="YTD"
b184["Peroid"]="4"

b183=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 3],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 3],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 3],na.rm=T))

b183["MTD/YTD"]="YTD"
b183["Peroid"]="3"


b182=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 2],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 2],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 2],na.rm=T))

b182["MTD/YTD"]="YTD"
b182["Peroid"]="2"

b181=a18 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 1],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 1],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 1],na.rm=T))

b181["MTD/YTD"]="YTD"
b181["Peroid"]="1"

b1912=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 12],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 12],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 12],na.rm=T))

b1912["MTD/YTD"]="YTD"
b1912["Peroid"]="12"

b1911=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 11],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 11],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 11],na.rm=T))

b1911["MTD/YTD"]="YTD"
b1911["Peroid"]="11"

b1910=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 10],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 10],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 10],na.rm=T))

b1910["MTD/YTD"]="YTD"
b1910["Peroid"]="10"


b199=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 9],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 9],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 9],na.rm=T))

b199["MTD/YTD"]="YTD"
b199["Peroid"]="9"

b198=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 8],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 8],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 8],na.rm=T))

b198["MTD/YTD"]="YTD"
b198["Peroid"]="8"  

b197=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 7],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 7],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 7],na.rm=T))

b197["MTD/YTD"]="YTD"
b197["Peroid"]="7" 

b196=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 6],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 6],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 6],na.rm=T))

b196["MTD/YTD"]="YTD"
b196["Peroid"]="6" 

b195=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 5],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 5],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 5],na.rm=T))

b195["MTD/YTD"]="YTD"
b195["Peroid"]="5"   

b194=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 4],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 4],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 4],na.rm=T))

b194["MTD/YTD"]="YTD"
b194["Peroid"]="4"  

b193=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 3],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 3],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 3],na.rm=T))

b193["MTD/YTD"]="YTD"
b193["Peroid"]="3"  

b192=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 2],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 2],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 2],na.rm=T))

b192["MTD/YTD"]="YTD"
b192["Peroid"]="2"  

b191=a19 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 1],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 1],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 1],na.rm=T))

b191["MTD/YTD"]="YTD"
b191["Peroid"]="1"  

b202=a20 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 2],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 2],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 2],na.rm=T))

b202["MTD/YTD"]="YTD"
b202["Peroid"]="2"  

b201=a20 %>% 
  group_by(key) %>% 
  summarise(
    ACTUAL = sum(ACTUAL[Period <= 1],na.rm=T), 
    BUDGET = sum(BUDGET[Period <= 1],na.rm=T),
    BUDGETFLEX = sum(BUDGETFLEX[Period <= 1],na.rm=T))

b201["MTD/YTD"]="YTD"
b201["Peroid"]="1"  

YTD18=rbind(b181,b182,b183,b184,b185,b186,b187,b188,b189,b1810,b1811,b1812)
YTD19=rbind(b191,b192,b193,b194,b195,b196,b197,b198,b199,b1910,b1911,b1912)
YTD20=rbind(b201,b202)

keepytd=c("Unit","Descr...2","Dept","Descr...4","Tree.Name",
           "Tree.Node","Parent.Node","Oper.Unit","Descr...9",
           "Account","Descr...11","Director.OPRID","Descr...13",
          "Fiscal.Year","key")
a18ytd = a18[keepytd]
a18ytddis=unique(a18ytd)
a19ytd = a19[keepytd]
a19ytddis=unique(a19ytd)
a20ytd = a20[keepytd]
a20ytddis=unique(a20ytd)

a18YTD=right_join(a18ytddis,YTD18,by=c("key"))
a18YTD["Ledger"]=NA
a18YTD["Sum.Total.Amt"]=NA
a19YTD=right_join(a19ytddis,YTD19,by=c("key"))
a19YTD["Ledger"]=NA
a19YTD["Sum.Total.Amt"]=NA
a20YTD=right_join(a20ytddis,YTD20,by=c("key"))
a20YTD["Ledger"]=NA
a20YTD["Sum.Total.Amt"]=NA

aYTD=rbind(a18YTD,a19YTD,a20YTD)
aYTD=mutate(aYTD,Period = as.numeric(Peroid))

drops=c("key","Peroid")
aYTD1=aYTD[,!(names(aYTD) %in% drops)]
a1=a[,!(names(a) %in% drops)]

aall=bind_rows(a1,aYTD1)



write.csv(aall,"H:\\Qa\\QA_SHARED\\vicky chen\\data\\monthly financial report - Rad\\Monthly_RAD_Financial_report_1.csv") 
          



