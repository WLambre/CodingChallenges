#String of data to be rearranged

data = "Food,Attribute,Apple,Fruit,Carrot,Vegetable,Spinach,Vegetable,Spinach,Leafy Green,Carrot,Root,Apple,Sweet,Apple,Cider,Apple,Tree,Carrot,Vitamin K,Spinach,Flowers,Spinach,Iron"
#The alternate count will be used to see whether the string is for a food or an attribute
alternate_count = 0
#The cell str will be used to create the whole string between commas
cell_str = ""
#The data dict will be used to store attributes against the food
data_dict = {}

#For each character in the string
for character in data:
    
    #If its not a comma, add it to the cell string
    if character != ',':
        cell_str += character
    #If it is a comma, we know we've reached the end of the cell string so we add it to the dictionary
    else:
        #If the alternate count % 2 is 0 we know its an even number and thus its a food not an attribute
        if alternate_count % 2 == 0:
            food = cell_str
            #If the food isn't already in the dictionary we add it. If it is in the dictionary, we do nothing
            if food not in data_dict:
                data_dict[food] = []
        #If the alternate count is odd we know it isn't even, and is thus an attribute
        else:
            #We add the attribute against the right food
            data_dict[food].append(cell_str)
        #We then add the count up and clear the str
        alternate_count+=1
        cell_str = ""

#Printing the end result
print(data_dict)

