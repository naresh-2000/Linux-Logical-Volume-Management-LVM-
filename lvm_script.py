import os
status = 'y'
while status == 'y' :
        print("""\n.........Menu..........
        1 : Create a Logical Volume(LV)
        2 : Display Logical Volume
        3 : Extend the size of LV
        4 : Format Logical Volume
        5 : Format Logical Volume
        6 : Mount LV to a drive
        7 : Exit Program""")
        lv=input("Enter your choice : ")
        if lv == "1" :
                size=input("Enter the size of partition : ")
                name=input("Enter the name to be allocated : ")
                vna=input("Enter the name of VG to create LV partition : ")
                os.system("clear")
                os.system("lvcreate --size " + size + " --name " + name + " " + vna)
        elif lv == "2" :
        	vg=input("Enter the name of VG : ")
        	lv=input("Enter the name of LV : ")
        	os.system("clear")
        	os.system("lvdisplay " + vg + "/" + lv)
        elif lv == "3" :
        	size=input("Enter the size required : ")
        	lv=input("Enter the name of LV : ")
        	os.system("clear")
        	os.system("lvextend --size " + size + " " + lv)
        elif lv == "4" :
        	lv=input("Enter the name of LV : ")
        	os.system("clear")
        	os.system("mkfs.ext4 " + lv)
        elif lv == "5" :
        	lv=input("Enter the name of LV : ")
        	os.system("clear")
        	os.system("resize2fs " + lv)
        elif lv == "6" :
        	lv=input("Enter the name of LV : ")
       		drive=input("Enter the path of driver : ")
        	os.system("clear")
        	os.system("mount " + lv + " " + drive)
        elif lv == "7" :
        	os.system("clear")
        	exit()
        status = input("\nDo you want to continue (Y/N):").casefold()

print("Have a good day....")
	
