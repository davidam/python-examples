import re  
text = "PHP Exercises"  
print("Original Text: ",text)  
redata = re.compile(re.escape('php'), re.IGNORECASE)  
new_text = redata.sub('Python', 'PHP Exercises')  
print("Using 'php' replace PHP")   
print("New Text: ",new_text) 
