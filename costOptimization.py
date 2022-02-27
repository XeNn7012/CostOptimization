class Data_Refined():
    def __init__(self,machines,c,h,country):
        self.c=c
        self.machines=machines
        self.h=h
        self.country=country
    def calc(self,c1,price):
        cost=[]
        cost=(c1*price)
        return cost    
       
    def split_the_parts(self):
        region=""
        machine_cost = {}
        tcost,cost,making_units,quoitent_storage,cost_old,sorted_costrecord_number,sorted_machine=[],[],[],[],[],[],[],[]
        for i,j in self.machines.items():
            for value in j:
                if value=="cost":
                    if j[value] =="":
                        cost_old.append(0)
                    else:
                        cost_old.append(j[value])
                else:
                    making_units.append(j[value])
        
        for i in range(len(cost_old)):
            cost.append(cost_old[i]/self.h)
        serial_number=0
        i=0
        temp=self.c
        cost.reverse()
        making_units.reverse()
        making_units.append(0)
        cost.append(0)
        for i in range(len(cost)-1):
            if (making_units[i]<=temp) and ((i==5) or cost[i]<(cost[i+1]*2)):
                if cost[i]==0:
                    serial_number+=1
                    pass
                else:
                    quoitent=temp//making_units[i]
                    temp=temp%making_units[i]
                    quoitent_storage.append(quoitent)
                    
  
                    combined_quoitent_storage.append(quoitent*making_units[i])
                    record_number.append(serial_number)
                    serial_number+=1
                    i+=1
            else:
                serial_number+=1
                pass
            
        cost.pop(6)
        for ele in sorted(record_number, reverse = True):
            sorted_cost.append(cost[ele])
        sorted_cost.reverse() 
        for i in range(len(quoitent_storage)):
            tcost.append(self.calc(quoitent_storage[i],sorted_cost[i]))
            optimum=sum(tcost)
        Machine_type=["10XLarge","8XLarge","4XLarge","2XLarge","XLarge","Large"]
        for ele in sorted(record_number, reverse = True):
            sorted_machine.append(Machine_type[ele])
        sorted_machine.reverse()    
        for key in sorted_machine:
            for value in sorted_cost:
                machine_cost[key] = value
                sorted_cost.remove(value)
                break 
        (print("{"+"\n   \"region\":{0},\n   \"total_cost\":{1},\
        \n   \"machines\":[\n".format(self.country,optimum)+"  ",("\n   ".join(("["+key+":"+str(value)+"]") for key,value in machine_cost.items())),"\t \n] \n}"))


 
NewYork={
    "Large":{"cost":120,"making_units":10},
    "XLarge":{"cost":230,"making_units":20},
    "2XLarge":{"cost":450,"making_units":40},
    "4XLarge":{"cost":774,"making_units":80},
    "8XLarge":{"cost":1400,"making_units":160},
    "10XLarge":{"cost":2820,"making_units":320},
    }
    
India={
    "Large":{"cost":140,"making_units":10},
    "XLarge":{"cost":0,"making_units":20},
    "2XLarge":{"cost":413,"making_units":40},
    "4XLarge":{"cost":890,"making_units":80},
    "8XLarge":{"cost":1300,"making_units":160},
    "10XLarge":{"cost":2970,"making_units":320},
    }
China={
    "Large":{"cost":110,"making_units":10},
    "XLarge":{"cost":200,"making_units":20},
    "2XLarge":{"cost":0,"making_units":40},
    "4XLarge":{"cost":670,"making_units":80},
    "8XLarge":{"cost":1180,"making_units":160},
    "10XLarge":{"cost":0,"making_units":320},
    }

n=int(input("Number of units required: "))
h=int(input("Hours: "))


c=Data_Refined(NewYork,n,h,country="NewYork")
c.split_the_parts()
c2=Data_Refined(India,n,h,country="India")
c2.split_the_parts()
c3=Data_Refined(China,n,h,country="China")
c3.split_the_parts()

