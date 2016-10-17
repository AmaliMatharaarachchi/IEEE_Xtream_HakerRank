
num_test_case=input()
c=0
while (c!=num_test_case):
    c=c+1
    ds=raw_input().split(" ")
    num_words=int(ds[0])
    num_string=int(ds[1])
    count=0
    count2=0
    prop_list=[]
    full_list=[]
    
    while(count!=num_words):
        count=count+1
        dic_string=list(raw_input())
        prop_list.append(dic_string)    
        full_list.extend(dic_string)
    while(count2<num_string):
        count2=count2+1
        search=list(raw_input())
        temp=[]
        a2=0
        try:
            for word in prop_list:
                temp2=[]
                for letter in word:
                    
                    try:
                        index=temp.index(letter)                    
                        temp2.append(temp.pop(index))
                            
                    except ValueError:                            
                        index=search.index(letter)
                        temp2.append(search.pop(index))
                            
                temp.extend(temp2)
                        
            print ("yes")
            
            if(len(search)==0):
                print ("yes")
                
            else:
                print ("no")
                
        except ValueError:
                a2=a2+1
                continue
        finally:
            if a2!=0:
                print ("no", a2)
        
