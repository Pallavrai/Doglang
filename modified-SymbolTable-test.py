from doglang.SymbolTable import SymbolTable

st = SymbolTable()
print(st) #should print "symbol table is empty"

st.insert("x","int","local",5) #inserts a identifier
print(st) #__repr__ testing

entry=st.lookup("x")
print(entry['value']) #printing the value of x

st.modify("x",10)
print(st.lookup("x")['value'])# printing the value of modified x

st2 = SymbolTable() #new table 
st2.insert("y","int","locla",20) # inserting a identifier to new table

print(st.lookup("y")) #testing if both tables are independent of each other.
