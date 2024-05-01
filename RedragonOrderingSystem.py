def menu():
    totalPrice = 0

    while True:
        print("\n\tMENU")
        print("1.) KEYBOARDS")
        print("2.) MOUSE")
        print("3.) COMBO")
        print("4.) MOUSEPAD")
        print("5.) MICROPHONE")
        print("6.) RACING WHEEL")
        print("7.) HEADSET")
        print("8.) GAMING CASE")
        print("9.) GAMEPAD")
        print("10.) WEBCAM")
        print("11.) SPEAKER")
        print("12.) GAMING BACKPACK")
        print("13.) ACCESORIES")
        print("14.) COOLING FAN")
        print("15.) GAMING PSU")
        print("16.) GAMING MONITOR")

        price = 0

        userChooseMenu = int(input("Enter what you want to buy : "))

        if userChooseMenu == 1:
            print("\nKEYBOARDS\t\t\t\tPRICE")
            print("1.) Redragon K618 Horus\t\t\tP 3,700")
            print("2.) Redragon K552-R Kumara\t\tP 2,500")
            print("3.) Redragon K617 Fizz    \t\tP 2,500")
            print("4.) Redragon K561-R       \t\tP 1,400")
            print("5.) Redragon K596 Vishnu  \t\tP 3,100")
            print("6.) Redragon K617 Fizz    \t\tP 3,700")
            print("7.) Redragon K686 Pro     \t\tP 3,100")

            userOrderKeyboard = int(input("Enter what keyboard do you want to buy : "))

            if userOrderKeyboard == 1:
                price += 3700

            elif userOrderKeyboard == 2:
                price += 2500

            elif userOrderKeyboard == 3:
                price += 2500

            elif userOrderKeyboard == 4:
                price += 1400

            elif userOrderKeyboard == 5:
                price += 3100

            elif userOrderKeyboard == 6:
                price += 3700

            elif userOrderKeyboard == 7:
                price += 3100

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 2:
            print("\nMOUSE\t\t\t\t\t\t PRICE")
            print("1.) Redragon M908 Impact\t\t\tP 1,800")
            print("2.) Redragon M913 Impact Elite\t\t\tP 2,700")
            print("3.) Redragon M916 Pro 1K      \t\t\tP 2,200")
            print("4.) Redragon M916 Pro 4K      \t\t\tP 2,800")
            print("5.) Redragon Predator M612    \t\t\tP 1,400")
            print("6.) Redragon Fyzu M995        \t\t\tP 2,000")
            print("7.) Redragon M686 Vampire     \t\t\tP 2,400")
            print("8.) Redragon M693             \t\t\tP 1,700")

            userOrderMouse = int(input("Enter what mouse you want to buy : "))

            if userOrderMouse == 1:
                price += 1800

            elif userOrderMouse == 2:
                price += 2700

            elif userOrderMouse == 3:
                price += 2200

            elif userOrderMouse == 4:
                price += 2800

            elif userOrderMouse == 5:
                price +=1400

            elif userOrderMouse == 6:
                price += 2000

            elif userOrderMouse == 7:
                price += 2400

            elif userOrderMouse == 8:
                price += 1700

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        
        elif userChooseMenu == 3:
            print("\nCOMBO\t\t\t\t PRICE")
            print("1.) Redragon S101-1\t\tP 2,500")
            print("2.) Redragon K530 B\t\tP 5,400")
            print("3.) Redragon K530 W\t\tP 7,400")
            print("4.) Redragon K582-BA\t\tP 4,000")
            print("5.) Redragon Caminic\t\tP 1,200")

            userOrderCombo = int(input("Enter what combo you want to buy : "))

            if userOrderCombo == 1:
                price += 2500

            elif userOrderCombo == 2:
                price += 5400

            elif userOrderCombo == 3:
                price += 7400
            
            elif userOrderCombo == 4:
                price += 4000

            elif userOrderCombo == 5:
                price += 1200

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue


        elif userChooseMenu == 4:
            print("\nMOUSEPAD\t\t\t PRICE")
            print("1.) Redragon P012\t\tP 1,100")
            print("2.) Redragon P015\t\tP 1,400")
            print("3.) Redragon P003\t\tP 1,100")
            print("4.) Redragon P011\t\tP 1,100")


            userOrderMousepad = int(input("Enter what mousepad you want to buy : "))

            if userOrderMousepad == 1:
                price += 1100

            elif userOrderMousepad == 2:
                price += 1400

            elif userOrderMousepad == 3:
                price += 1100

            elif userOrderMousepad == 4:
                price += 1100

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue


        elif userChooseMenu == 5:
            print("\nMICROPHONE\t\t\t\t PRICE")
            print("1.) Redragon GM300 Microphone\t\tP 2,800")
            print("2.) Redragon GM200 Microphone\t\tP 1,400")
            print("3.) Redragon GM100 Microphone\t\tP 1,100")


            userOrderMicrophone = int(input("Enter what microphone you want to buy : "))

            if userOrderMicrophone == 1:
                price += 2800

            elif userOrderMicrophone == 2:
                price += 1400

            elif userOrderMicrophone == 3:
                price += 1100

            else: 
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 6:
            print("\nRACING WHEEL\t\t\t\t PRICE")
            print("1.) Redragon GT-32 Racing Wheel\t\tP 40,000")

            userOrderRacingWheel = int(input("Enter what racing wheel you want to buy : "))

            if userOrderRacingWheel == 1:
                price += 40000

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        
        elif userChooseMenu == 7:
            print("\nHEADSETS\t\t\t PRICE")
            print("1.) H510 Zeus\t\t\tP 3,100")
            print("2.) Scream H231\t\t\tP 1,300")
            print("3.) Cronus H211\t\t\tP 1,200")
            print("4.) Pandora H350\t\tP 1,800")
            print("5.) Icon H520   \t\tP 2,900")

            userOrderHeadset = int(input("Enter what headset you want to buy : "))

            if userOrderHeadset == 1:
                price += 3100

            elif userOrderHeadset == 2:
                price += 1300

            elif userOrderHeadset == 3:
                price += 1200

            elif userOrderHeadset == 4:
                price += 1800

            elif userOrderHeadset == 5:
                price += 2900

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue


        elif userChooseMenu == 8:
            print("\nGAMING CASE\t\t\t PRICE")
            print("1.) Redragon MC211 Case\t\tP 3,500")
            print("2.) Redragon EB211 Case\t\tP 4,600")
            

            userOrderGamingCase = int(input("Enter what gaming case you want to buy : "))

            if userOrderGamingCase == 1:
                price += 3500

            elif userOrderGamingCase == 2:
                price += 4600

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 9:
            print("\nGAMING PAD\t\t\t PRICE")
            print("1.) Redragon G812 Ceres\t\tP 2,600")
            print("2.) Redragon G809 Jupiter\tP 2,300")


            userOrderGamingPad = int(input("Enter what you want to buy : "))

            if userOrderGamingPad == 1:
                price += 2600

            elif userOrderGamingPad == 2:
                price += 2300

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue
        
        elif userChooseMenu == 10:
            print("\nWEBCAM\t\t\t\t PRICE")
            print("1.) Redragon GW910\t\tP 2,400")
            print("2.) Redragon GW800\t\tP 2,100")
            print("3.) Redragon GW600\t\tP 1,700")

            userOrderWebCam = int(input("Enter what webcam you want to buy : "))

            if userOrderWebCam == 1:
                price += 2400

            elif userOrderWebCam == 2:
                price += 2100

            elif userOrderWebCam == 3:
                price += 1700

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 11:
            print("\nSPEAKER\t\t\t\t\t\t PRICE")
            print("1.) Redragon GS590 Wireless\t\t\tP 1,100")
            print("2.) Redragon GS813 Wireless\t\t\tP 2,000")
            print("3.) Redragon GS812 Wireless\t\t\tP 3,500")
            print("4.) Redragon GS560 Adiemus\t\t\tP 2,300")
            print("5.) Redragon GS520 RGB\t\t\t\tP 2,000")
            print("6.) Redragon GS510 Waltz\t\t\tP 1,100")
            print("7.) Redragon GS520 Anvil\t\t\tP 1,900")

            userOrderSpeaker = int(input("Enter what speaker you want to buy : "))

            if userOrderSpeaker == 1:
                price += 1100

            elif userOrderSpeaker == 2:
                price += 2000

            elif userOrderSpeaker == 3:
                price += 3500

            elif userOrderSpeaker == 4:
                price += 2300

            elif userOrderSpeaker == 5:
                price += 2000

            elif userOrderSpeaker == 6:
                price += 1100

            elif userOrderSpeaker == 7:
                price += 1900

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue
        
        elif userChooseMenu == 12:
            print("\nGAMING BACKPACK\t\t\t\t PRICE")
            print("1.) Redragon GB-94 Backpack\t\tP 1,100")
            print("2.) Redragon GB-93 Backpack\t\tP 1,100")
            print("3.) Redragon GB-82 Backpack\t\tP 1,100")
            print("4.) Redragon GB-76 Backpack\t\tP 1,100")
            
            userOrderGamingBackpack = int(input("Enter what gaming backpack you wannt to buy : "))

            if (userOrderGamingBackpack == 1 or userOrderGamingBackpack == 2 or userOrderGamingBackpack == 3 or userOrderGamingBackpack == 4):
                price += 1100

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 13:
            print("\nACCESSORIES\t\t\t\t\t PRICE")
            print("1.) Redragon AA13 Tactile Mechanical Switch\t P 800")
            print("2.) Redragon Computer Keyboard Wrist Rest Pad\t P 750")
            print("3.) Redragon GA250 Keyboard and Mouse Adapter\t 2,300")
            print("4.) Redragon HA300 Headset Stand             \tP 950")
            
            userOrderAccessories = int(input("Enter what accessories you want to buy : "))

            if userOrderAccessories == 1:
                price += 800

            elif userOrderAccessories == 2:
                price += 750

            elif userOrderAccessories == 3:
                price += 2300

            elif userOrderAccessories == 4:
                price += 950

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 14:
            print("\nCOOLING FAN\t\t\t\t\t PRICE")
            print("1.) Redragon C218 CPU Air Cooler\t\tP 2,400")
            print("2.) Redragon HL240/HL360 RGB Cooling System\tP 3,400")
            print("3.) Redragon GCP500 Laptop CPU Cooler      \tP 1,300")
            
            userOrderCoolingFan = int(input("Enter what cooling fan you want to buy : "))

            if userOrderCoolingFan == 1:
                price += 2400

            elif userOrderCoolingFan == 2:
                price += 3400

            elif userOrderCoolingFan == 3:
                price += 1300

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 15:
            print("\nGAMING PSU\t\t\t\t\t PRICE")
            print("1.) Redragon 80+ Platinum 1000 Watt     \tP 11,500")
            print("2.) Redragon PSU014 80+ Gold 650 Watt   \tP 7,500")
            print("3.) Redragon PSU015 80+ Platium 750 Watt\tP 8,000")
            print("4.) Redragon PSU007 80+ Gold 850 Watt   \tP 6,600")
            print("5.) Redragon PSU006 80+ Gold 750 Watt   \tP 6,600")
            print("6.) Redragon PSU013 80+ Gold 650 Watt   \tP 6,600")
            print("7.) Redragon PSU007 80+ Gold 850 Watt   \tP 6,600")
            
            userOrderPSU = int(input("Enter what psu you want to buy : "))

            if userOrderPSU == 1:
                price += 11500

            elif userOrderPSU == 2:
                price += 7500

            elif userOrderPSU == 3:
                price += 8000

            elif userOrderPSU == 4:
                price += 6600

            elif userOrderPSU == 5:
                price += 6600

            elif userOrderPSU == 6:
                price += 6600

            elif userOrderPSU == 7:
                price += 6600

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        elif userChooseMenu == 16:
            print("\nGAMING MONITOR\t\t\t\t PRICE")
            print("1.) Redragon OPAL 27` 144hz\t\tP 15,500")
            print("2.) Redragon BM27V9 monitor 75hz\tP 7,200")
            print("3.) Redragon Jade 144hz         \tP 15,500")
            print("4.) Redragon GM3CA237 165hz     \tP 18,900")
            print("5.) Redragon GM3CB238 RUBY 165hz\tP 5,700")

            userOrderGamingMonitor = int(input("Enter what monitor you want to buy : "))

            if userOrderGamingMonitor == 1:
                price += 15500

            elif userOrderGamingMonitor == 2:
                price += 7200

            elif userOrderGamingMonitor == 3:
                price += 15500

            elif userChoose == 4:
                price += 18900

            elif userOrderGamingMonitor == 5:
                price += 5700

            else:
                input("\nInvalid Order, Press Enter To Try Again!: ")
                continue

        quantity = int(input("Enter quantity here : "))
        totalPrice += quantity * price   

        userOrderAgain = str(input("Do you want to order more (y/n)?: ")).lower()

        if userOrderAgain != "y":
            print("Total Price : P " + str(totalPrice))

            userMoney = int(input("Enter your payment here : P "))

            if userMoney < totalPrice:
                print("Insufficient Money, Please Try Again!")
                continue

            else:
                change = userMoney - totalPrice
                print("Change : P " + str(change))
                print("Thank You For Ordering Please Come Again!")

        elif userOrderAgain == "y":
            continue

        else:
            print("Invalid Option, Please Try Again!")
            continue

        break

def aboutUs():
    print("\n\t\t\tABOUT US")
    print("\nEastern Times Technology Co., Ltd was established in 1996, the top 5 factory for Mouse and keyboard in China. We have a professional R&D teams")
    print("with 15 good experienced engineers and more than 10 years professional QC team , over 1400 employees in total , offering a one - stop production")
    print("service to meet your various needs.")
    


def userChoose():
    userName = input("Enter your name here: ")

    while True:
        print("\nHello, " + userName + "! Welcome To Redragon Ordering System!")
        print("1.) MENU")
        print("2.) ABOUT US")
        print("3.) EXIT")

        userChoice = int(input("Enter your choice here: "))

        if userChoice == 1:
            menu()

        elif userChoice == 2:
            aboutUs()
            break
        elif userChoice == 3:
            print("Thank you for visiting. Goodbye!")
            break
        else:
            input("Invalid Choice, Please Enter To Try Again!: ")
            continue
        break

userChoose()
