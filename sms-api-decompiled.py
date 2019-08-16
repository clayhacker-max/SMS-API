import os
import time
import random
import smtplib

os.system('apt install termux-api')
os.system('clear')
logo = "\n\x1b[1;33m ____            ____          _    ____ ___\n/ ___| _ __ ___ / ___|        / \\  |  _ \\_ _|\n \\___ \\| '_ ` _ \\___ \\ _____ / _ \\ | |_) | |\n ___) | | | | | |___) |_____/ ___ \\|  __/| |\n|____/|_| |_| |_|____/     /_/   \\_\\_|  |___| By JustAHacker\n\nGithub = \x1b[1;92m\x1b[4mhttps://github.com/JustAHackers/SmS-API\x1b[0m\n\x1b[1;39mInstagram = Agung_Rafasyah\n\x1b[1;36mYoutube = JustA Hacker"
print logo
e = raw_input('\x1b[1;38m \nTekan Enter Untuk Melanjutkan ')
if e == '':
    os.system('clear')
    print logo
    time.sleep(2)
    print ''
    print ''
    nope = raw_input('\x1b[1;33mMasukan Nomor Tujuan : ')
    pesan = raw_input('\x1b[1;36mMasukan Pesan : ')
    time.sleep(2)
    kode = random.randint(232658, 947364)
    fadd = 'rafasyahagung@gmail.com'
    tadd = raw_input('Masukkan Gmail Anda : ')
    print 'Kode Verifikasi 6 Angka Telah Dikirim ke ' + str(tadd)
    SUBJECT = 'Kode Verifikasi Sms-Api  '
    TEXT = 'Kode Verifikasi Script SmS-API anda adalah ' + str(kode) + '\n\n\n\n\n\n\n\n Subscribe Channel JustA Hacker \n Youtube.com/RezondeGrowtopia'
    message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
    username = 'justabotsubs12@gmail.com'
    password = 'ebknurbqygdvplsc'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fadd, tadd, message)
else:
    os.system('clear')
    print '\x1b[1;33mKalo Gamau Pake Ya Udah :('
    os.sys.exit()

def verif():
    os.system('clear')
    print logo
    print '\x1b[1;35mMasukkan Kode Yang Telah Dikirim ke ' + str(tadd)
    print ''
    kodev = raw_input('\x1b[1;33mKode = ')
    if kodev == str(kode):
        print 'Verifikasi Berhasil... '
        time.sleep(2)
        kirim()
    else:
        print 'Kode Yang Anda Masukkan Salah,Silahkan Cek Gmail anda Untuk kodenya'
        time.sleep(5)


def kirim():
    os.system('clear')
    print logo
    print 'Apakah Anda Yakin Ingin Mengirim Pesan Ke ' + str(nope) + ' ' + 'isi pesannya adalah ' + str(pesan)
    konfir = raw_input('\x1b[1;31mTekan Enter Untuk Mengirim pesan')
    if konfir == '':
        os.system('clear')
        os.system('termux-sms-send -n ' + str(nope) + ' ' + str(pesan))
        print 'Berhasil'
        time.sleep(1)
        os.sys.exit()
    else:
        os.sys.exit()


if __name__ == '__main__':
    verif()
