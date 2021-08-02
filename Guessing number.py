import random
import pywhatkit as pyw

print("Permainan meneka nombor. Teka nombor 1 sehinnga 10")
print("Masukkan nombor tepon anda")
no_tepon = input("Nom tepon: 60")
print("Saved", "+60"+no_tepon)


tempoh_teko = 10

while True:
    nombor_teko = input("Masukkan satu nombor : ")
    num = random.randint(1, 10)

    if nombor_teko.isdigit():
        nombor_teko = int(nombor_teko)
        if nombor_teko == num:
            print("Demo telah berjayo")
            tempoh_teko += 1
            print("Tambah satu mato " + str(tempoh_teko))
            pyw.sendwhatmsg("+60"+no_tepon,"ANDA MENANG HADIAH PERMAINAN",6,43)

        else:
            print("Demo saloh teko nombor, cuba lagi")
            tempoh_teko -= 1
            print("Baki hanyo tinggal: " + str(tempoh_teko))
            if tempoh_teko == 0:
                print("Mu Kaloh")
                break

    else:
        print("Invalid value, try Again!")


