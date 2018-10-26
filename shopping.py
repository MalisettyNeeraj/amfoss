print("welcome to the shopping mall ")
shopping_list=[]
shopping_list_cost=[]
z=1
cnt=0
user=""
print("Press 'ENTER' continue")
x=input()

while(z!=0):     
	print("1 Mens wear")
	print("2 Mobiles and laptops")
	print("3 Books")
	print("4 Groceries")

	user=input()
	if(user=="1"):  
		gst=0
		print("1 T-shirt ")
		print("2 shirts")
		print("3 Jeans")

		user=input()
		if(user=="1"):   
			f=0
			shopping_list.append("t-shirt")
			print("select the size")
			user=input().lower()
			if(user=="s"):
				shopping_list[cnt]=shopping_list[cnt]+" S"
				f=1
				gst=50
			elif(user=="l"):
				shopping_list[cnt]=shopping_list[cnt]+" L"	
				f=1
				gst=100
			elif(user=="m"):
				shopping_list[cnt]=shopping_list[cnt]+" M"
				f=1
				gst=150
			elif(user=="xl"):
				shopping_list[cnt]=shopping_list[cnt]+" XL"	
				f=1
				gst=200
			elif(user=="xxl"):
				shopping_list[cnt]=shopping_list[cnt]+" XXL"	
				f=1
				gst=250
			else:
				shopping_list.pop(cnt)
			if(f==1):
				print("Choose the brand")
				print("1 US polo             RS."+str(gst+450))
				print("2 Tommy hilfiger      RS."+str(gst+500))
				print("3 Arrow               RS."+str(gst+600))
			
				user=input()	
				if(user=="1"):
					shopping_list[cnt]=shopping_list[cnt]+" US polo"	
					shopping_list_cost.append(gst+450)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list[cnt]=shopping_list[cnt]+" Tommy hilfiger"	
					shopping_list_cost.append(gst+500)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list[cnt]=shopping_list[cnt]+" Arrow"
					shopping_list_cost.append(gst+600)
					cnt=cnt+1
					print("Successfully added to cart.")
				else:
					shopping_list.pop(cnt)
		elif(user=="2"):   
			f=0
			shopping_list.append("formal_shirt")
			print("select the size")
			user=input()
			if(user=="s"):
				shopping_list[cnt]=shopping_list[cnt]+" S"
				f=1
				gst=50
			elif(user=="l"):
				shopping_list[cnt]=shopping_list[cnt]+" L"	
				f=1
				gst=100
			elif(user=="m"):
				shopping_list[cnt]=shopping_list[cnt]+" M"
				f=1
				gst=150
			elif(user=="xl"):
				shopping_list[cnt]=shopping_list[cnt]+" XL"	
				f=1
				gst=200
			elif(user=="xxl"):
				shopping_list[cnt]=shopping_list[cnt]+" XXL"	
				f=1
				gst=250
			else:
				shopping_list.pop(cnt)
			if(f==1):
				print("Choose the brand")
				print("1 US polo    RS."+str(gst+450))
				print("2 Arrow      RS."+str(gst+500))
				print("3 UCB        RS."+str(gst+600))
				
				user=input()
				if(user=="1"):
					shopping_list[cnt]=shopping_list[cnt]+" US polo"	
					shopping_list_cost.append(gst+450)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list[cnt]=shopping_list[cnt]+" Arrow"	
					shopping_list_cost.append(gst+500)
					print("Successfully added to cart.")
					cnt=cnt+1
				elif(user=="3"):
					shopping_list[cnt]=shopping_list[cnt]+" UCB"
					shopping_list_cost.append(gst+600)
					cnt=cnt+1
					print("Successfully added to cart.")
				else:
					shopping_list.pop(cnt)
		elif(user=="3"):  
			shopping_list.append("jeans")
			print("Choose the brand")
			print("1 US polo       RS.750")
			print("2 Pepe Jeans    RS.700")
			print("4 Lee           RS.600")
			user=input()	
			if(user=="1"):
				shopping_list[cnt]=shopping_list[cnt]+" US polo"	
				shopping_list_cost.append(750)
				print("Successfully added to cart.")
				cnt=cnt+1
			elif(user=="2"):
				shopping_list[cnt]=shopping_list[cnt]+" Baffalo"	
				shopping_list_cost.append(700)
				cnt=cnt+1
				print("Successfully added to cart.")
			
			elif(user=="4"):
				shopping_list[cnt]=shopping_list[cnt]+" Lee"
				shopping_list_cost.append(600)
				cnt=cnt+1
				print("Successfully added to cart.")
			
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()

	
	elif(user=="2"):  
		print("1 Mobiles")
		print("2 Laptops")
		user=input()
		if(user=="1"):
			print("1 MI phone")
			print("2 Apple iphone")
			print("3 Oneplus")
			print("4 Samsung Galaxy")	
			user=input()
			if(user=="1"):   
				print("1 Redmi 5                          RS.7999")
				print("2 Redmi Note 5                     RS.12999")
				print("3 Redmi Note 5 Pro                 RS.16999")
				if(user=="1"):
					shopping_list.append("Redmi 5")
					shopping_list_cost.append(7999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append("Redmi Note 5")
					shopping_list_cost.append(12999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append("Redmi Note 5 Pro")
					shopping_list_cost.append(16999)		
					cnt=cnt+1
					print("Successfully added to cart.")
			elif(user=="2"):   
				print("1 Iphone 7                     RS.49999")
				print("2 Iphone 8                     RS.71999")
				print("3 Iphone X                     RS.90999")
				print("4 Iphone XS                    RS.100999")
				print("5 Iphone X Max                 RS.119999")
				user=input()
				if(user=="1"):
					shopping_list.append("Iphone 7")
					shopping_list_cost.append(49999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append("Iphone 8")
					shopping_list_cost.append(71999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append("Iphone X")
					shopping_list_cost.append(90999)	
					cnt=cnt+1
					print("Successfully added to cart.")	
				elif(user=="4"):
					shopping_list.append("Iphone XS")
					shopping_list_cost.append(100999)	
					cnt=cnt+1	
					print("Successfully added to cart.")
				elif(user=="5"):
					shopping_list.append("Iphone X Max")
					shopping_list_cost.append(119999)
					cnt=cnt+1
					print("Successfully added to cart.")
			elif(user=="3"):   
				print("1  Oneplus  3          RS.15999")
				print("2  Oneplus 5           RS.22999")
				print("3  Oneplus 5t          RS.29999")
				print("4  Oneplus 6           RS.32999")
				print("5  Oneplus 6t          RS.39999")
				user=input()
				if(user=="1"):
					shopping_list.append(" Oneplus 3 ")
					shopping_list_cost.append(15999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append(" Oneplus 5 ")
					shopping_list_cost.append(22999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append(" Oneplus 5t  ")
					shopping_list_cost.append(29999)		
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="4"):
					shopping_list.append(" Oneplus 6 ")
					shopping_list_cost.append(32999)	
					cnt=cnt+1	
					print("Successfully added to cart.")
				elif(user=="5"):
					shopping_list.append(" Oneplus 6t ")
					shopping_list_cost.append(39999)
					cnt=cnt+1
					print("Successfully added to cart.")
			elif(user=="4"):     
				print("1 Samsung Galaxy Note 9                   RS.68999")
				print("2 Galaxy S9                               RS.57999")
				print("3 Galaxy A7                               RS.23999")
				user=input()
				if(user=="1"):
					shopping_list.append(" Galaxy Note 9")
					shopping_list_cost.append(68999)
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="2"):
					shopping_list.append(" Galaxy S9")
					shopping_list_cost.append(57999)	
					cnt=cnt+1
					print("Successfully added to cart.")
				elif(user=="3"):
					shopping_list.append(" Galaxy A7")
					shopping_list_cost.append(23999)		
					cnt=cnt+1
					print("Successfully added to cart.")
			user=""
		elif(user=="2"):   
			print("1 Dell i3 5thgen")
			print("2 Dell i5 5thgen")
			print("3 Dell i7 8thgen")
			print("4 Apple MacBook pro")
			user=input()
			if(user=="1"):
				shopping_list.append(" Dell i3 5thgen")
				shopping_list_cost.append(30000)
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="2"):
				shopping_list.append(" Dell i5 5thgen")
				shopping_list_cost.append(40000)	
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="3"):
				shopping_list.append(" Dell i7 8thgen")
				shopping_list_cost.append(80000)				
				cnt=cnt+1
				print("Successfully added to cart.")
			elif(user=="4"):
				shopping_list.append(" Apple MacBook Laptop")
				shopping_list_cost.append(250000)			
				cnt=cnt+1
				print("Successfully added to cart.")		
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
	if(user=="3"):   #books
		print("1 Engineering drawing             RS.650")
		print("2 Modern Physics                  RS.430")
		print("3 Calculus                        RS.600")
		print("4 Matrix Algebra                  RS.440")
		user=input()
		if(user=="1"):
			shopping_list.append(" Engineering Drawing")
			shopping_list_cost.append(650)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="2"):
			shopping_list.append(" Modern Physics")
			shopping_list_cost.append(430)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="3"):
			shopping_list.append(" Calculus")
			shopping_list_cost.append(600)
			cnt=cnt+1
			print("Successfully added to cart.")
		elif(user=="4"):
			shopping_list.append(" Matrix Algebra")
			shopping_list_cost.append(440)
			cnt=cnt+1
			print("Successfully added to cart.")
		user=""
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
	elif(user=="4"):
		print("""1. Duppatas           Rs.250
			 2.  Pillows            Rs.150
			 3.  Utensils           Rs.300
			 4.  Soaps              Rs.40""")
			 
			
		grocery_cost=[0,250,150,300,40]
		print("Select your product")
		user=input()
		print(grocery[int(user)])
		shopping_list.append(grocery[int(user)])
		shopping_list_cost.append(grocery_cost[int(user)])
		cnt=cnt+1
		print("Successfully added to cart.")		
		print("If you want to continue shopping  press 'Enter' .\n To exit press '0'   "  )
		e=input()
		if(e=="0"):
			z=0
		else:
			z=1
		for i in range(10):
			for j in range(10):
				print()
		else:        
			
			for i in range(10):
				for j in range(10):
					print()	
		print("please enter a valid key")
t=0
tcnt=cnt
print("######       To see your items and proceed to payment  , Press 'Enter'")
print("########     To cancel you order ,Press '0' ")
print("##########   To remove any item , Press 'r'  ")
user1=input()
if(user1=="0"):   
	for i in range(cnt):
		print(str(i+1)+"                "+str(shopping_list[i])+"                                                    "+str(shopping_list_cost[i]))
		i=i+1
	print()
	print()
	print("your total price")
	print(sum(shopping_list_cost))
	print("Total number of items in your cart = "+str(cnt))
	print("Press any key to remove items from your cart")
	user=input()
	t=1
	if(t==1):
		print("Your cart is empty now")
		print("Thanks for shopping with us. :)")
		t=0
	
elif(user1=="r"):      
	z=1
	while(z!=0):
		for i in range(tcnt):
			print(str(i+1)+"                "+str(shopping_list[i])+"                                                   "+str(shopping_list_cost[i]))
			i=i+1
		print("Please enter the serial number to be removed")
		user=input()
		shopping_list.pop(int(user)-1)
		shopping_list_cost.pop(int(user)-1)
		print("successfully removed.")
		print("To remove another item, Press 'r'  again")
		print("Else Press any key to continue for payment")
		user=input()
		if(user=="r"):
			z=1	
			tcnt=tcnt-1
		else :
			z=0
			t=1
			tcnt=tcnt-1
else:
	t=1
if(t!=0):
	bank=""
	address=""
	dis=0
	for i in range(10):     #payment
		for j in range(10):
			print()
	i=0
	for i in range(tcnt):
		print(str(i+1)+"                "+str(shopping_list[i])+"                                                                 "+str(shopping_list_cost[i]))
		i=i+1
	print()
	print()
	print("your total price")
	fp=sum(shopping_list_cost)
	print(fp)
	print("Total number of items in your cart = "+str(tcnt))
	print("Since this is your first order , you  are provided with a coupon 'ENS'  .\n Enter the code to get a discount of 25% on your products.\n Else press any  key to proceed for payment.")
	user=input()
	for i in range(10):     
		for j in range(10):
			print()
	if(user=="ENS"):
		print("Final amount ="+str(fp))
		dis=fp*(25/100)
		print("discount         =  -"+str(dis))
		print("Final amount (After discount)  ="+str(fp-dis))
		print("you got a discount of 25% on your products")
		
		print("Please enter your delivery address")
		address=input()	
		print("Please select the type of payment")
		print("1 Net banking")
		print("2 Cash on delivery")
		print("Press any key to exit payment ")
		user=input()
		if(user=="1"):
			print("Please enter your Bank Name")
			bank=input().upper()
			print("Please enter your Password")
			user=input()
			for i in range(10):     
				for j in range(10):
					print()
			print(bank)
			print("Amount payable ="+str(fp))
			print("REMARKS  :",end="")
			user=input()
			print("\nPress 'n' to cancel payment. \n Press 'enter' to preceed for payment")
			user=input()
			if(user=='n'):
				print("Your payment has been cancelled . Your items in your cart are also removed .")
				print("Your cart is empty now")
				print("Thanks for shopping with us.   :)")
			else:
				print("Your payment is successful.")
				print("Your order will deliver to :")
				print(address)
				print("In the next 5 days .\n Thanks for shopping with us.   :)")
		elif(user=="2"):
			print("Your order will deliver to :")
			print(address)
			print("In the next 5 days .\n Thanks for shopping with us.  :) ")
		else:
			print("Your cart is empty now")
			print("Thanks for shopping with us.   :)")
	else:
		print("Final amount ="+str(fp))
		print("Please enter your delivery address")
		address=input()	
		print("Please select the type of payment")
		print("1 Net banking")
		print("2 Credit card")                                    
		print("3 Cash on delivery")
		print("press any key to exit payment")
		user=input()
		if(user=="1" or user=="2"):
			print("Please enter your Bank Name")
			bank=input().upper()
			print("Please enter your Password")
			user=input()
			for i in range(10):     
				for j in range(10):
					print()
			print(bank)
			print("Amount payable ="+str(fp))
			print("REMARKS  :",end="")
			user=input()
			print("\nPress 'n' to cancel payment. \n Press 'enter' to preceed for payment")
			user=input()
			if(user=='n'):
				print("Your payment has been cancelled . Your items in your cart are also removed .")
				print("Your cart is empty now")
				print("Thanks for shopping with us.   :)")
			else:
				print("Your payment is successful.")
				print("Your order will deliver to :")
				print(address)
				print("In the next 5 days .\n Thanks for shopping with us.  :)")
		elif(user=="3"):
			print("Your order will deliver to :")
			print(address)
			print("In the next 5 days .\n Thanks for shopping with us.  :)")
		else:
			print("Your cart is empty now")
			print("Thanks for shopping with us.   :)")
