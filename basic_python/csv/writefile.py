import csv


with open('fin2.csv','a') as csvfile:
   fieldnames = ['first_name','last_name']
   my_writeer = csv.DictWriter(csvfile,fieldnames=fieldnames)

   my_writeer.writeheader()
   my_writeer.writerow({
       'first_name' : "james",
       'last_name': "james2"
   })