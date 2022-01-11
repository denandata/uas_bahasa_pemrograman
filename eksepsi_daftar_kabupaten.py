import time
    f= open('coba.txt')
    while True:
        baris = f.redline ()
        if len(baris) == 0:
                #EOF
                break
              print baris,
              time.sleep(2)     # delay 2 detik
 except KeyboardInterrupt :
    print '\nAnda membatalkan operasi'
    f.close ()
    print '\nfile ditutup.'
