import pygame
from pygame import mixer
import random
from os import environ
from sys import platform as _sys_platform

def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return "android"
    elif _sys_platform in ('linux', 'linux2', 'linux3'):
        return "linux"
    elif _sys_platform in ('win32', 'cygwin'):
        return 'win'

pygame.init()
mixer.init()
pygame.display.init()

infoObject = pygame.display.Info()
breite = infoObject.current_w//100*100
hoehe  = infoObject.current_h//100*100

groeße = 50
nochmal = 0

screen = pygame.display.set_mode((breite, hoehe),pygame.FULLSCREEN)

pygame.display.set_caption('Schnaeggelz')

if platform() == "android":
    path = "/data/data/org.beezi.schnaeggelz/files/app/"
elif platform() == "linux":
    path = "./"

bgstart = (15, 50, 15)
screen.fill(bgstart)  
waitmessage = pygame.font.Font(path+'UbuntuMono-R.ttf', 90).render(f'Schnaeggelz', False, (200, 150, 42))
waitmessage_rect = waitmessage.get_rect(center=(breite/2, hoehe/2))
screen.blit(waitmessage, waitmessage_rect)
pygame.display.update()
pygame.time.wait(2000)
neustart = True
while neustart == True:
    neustart = False
    # Start-Variablen
    multi = 1
    score = 0
    tempo = 40
    richtungx = 1
    richtungy = 0
    richtungen = {pygame.K_UP:(0,-1), pygame.K_DOWN:(0,1), pygame.K_LEFT:(-1,0), pygame.K_RIGHT:(1,0)}
    invert = {pygame.K_UP:(0,1), pygame.K_DOWN:(0,-1), pygame.K_LEFT:(1,0), pygame.K_RIGHT:(-1,0)}
    bonusx = 400
    bonusy = 300
    bonusx2 = -100
    bonusy2 = -110
    bonus2ran = 20
    bonus2int = 0
    snake = [(breite//2, hoehe//2)]
    farbe = 0, 255, 0
    superbonus = 0
    ende = True
    bgint = 0
    schade = 0
    x, y = snake[-1]
    x, y = x + richtungx * groeße, y + richtungy * groeße
    letztex, letztey = richtungx, richtungy
    letztesnake = x, y
    sbzeit = 52
    bg = (20, 20, 20)
    bg2 = (40, 40, 40)
    run = True
    cash = 20
    clock = pygame.time.Clock()
    dbclock = pygame.time.Clock()
    verzoegert = True
    DOUBLECLICKTIME = 190
    wait = False
    alarmton = pygame.mixer.Sound(path+'alarm.ogg')
    endeton = pygame.mixer.Sound(path+'ende.ogg')
    halloton = pygame.mixer.Sound(path+'hallo.ogg')
    huiton = pygame.mixer.Sound(path+'hui.ogg')
    jamjamton = pygame.mixer.Sound(path+'jamjam.ogg')
    newgameton = pygame.mixer.Sound(path+'newgame.ogg')
    tatuetata2ton = pygame.mixer.Sound(path+'hieergs.ogg')
    pauseton = pygame.mixer.Sound(path+'pause.ogg')
    startton = pygame.mixer.Sound(path+'start.ogg')
    tatuetataton = pygame.mixer.Sound(path+'tatuetata.ogg')
    dummesau = pygame.mixer.Sound(path+'dummesau.ogg')
    amarsch = pygame.mixer.Sound(path+'amarsch.ogg')
    gratain = pygame.mixer.Sound(path+'gratain.ogg')
    nesch = pygame.mixer.Sound(path+'nesch.ogg')
    sobloed = pygame.mixer.Sound(path+'sobloed.ogg')
    wegschaffen = pygame.mixer.Sound(path+'wegschaffen.ogg')
    nichtnormal = pygame.mixer.Sound(path+'nichtnormal.ogg')
    ichgehejetzt = pygame.mixer.Sound(path+'ichgehejetzt.ogg')
    peng = pygame.mixer.Sound(path+'peng.ogg')
    channel1 = pygame.mixer.Channel(1)
    channel2 = pygame.mixer.Channel(2)
    channel3 = pygame.mixer.Channel(3)
    channel4 = pygame.mixer.Channel(4)
    channel5 = pygame.mixer.Channel(5)
    channel6 = pygame.mixer.Channel(6)
    channel7 = pygame.mixer.Channel(7)
    channel8 = pygame.mixer.Channel(6)
    channel9 = pygame.mixer.Channel(2)
    channel12 = pygame.mixer.Channel(7)
    alarmcheck = 0
    tatuetatacheck1 = 0
    tatuetatacheck2 = 0
    tatuetatacheck3 = 0
    tatuetatacheck4 = 0
    hallocheck = 0
    mposx = x
    mposy = y
    mx = mposx
    my = mposy
    mxdif = 0
    mydif = 0
    mrichtung = (x, y)
    doublecheck = True
    verlaengern = 0
    multibonusint=0
    multibonusx1 = -50
    multibonusy1 = -60
    multibonusx2 = -60
    multibonusy2 = -70
    multibonusx3 = -70
    multibonusy3 = -80
    multibonus1dauer = 0
    speedup = 0
    m1fwechsel = 0
    m1farbe1 = 138,43,226
    m1farbe2 = 255,0,255
    verhungern = 465
    hungerfarbe1 = 0
    hungerfarbe2 = 255
    hungerfarbe3 = 0
    hfarbe = (hungerfarbe1,hungerfarbe2,hungerfarbe3)
    tot = 0

    # Startposition-Schlaenggler
    ran1 = random.randrange(4)
    if ran1 == 1:
        richtungx = 1
        richtungy = 0
        invertx = (-1, 0)
    if ran1 == 2:
        richtungx = -1
        richtungy = 0
        invertx = (1, 0)
    if ran1 == 3:
        richtungx = 0
        richtungy = 1
        inverty = (0, -1)
    if ran1 == 0:
        richtungx = 0
        richtungy = -1
        inverty = (0, 1)

    # Startposition Bonus-Item
    bonusx = random.randrange(breite) // groeße * groeße
    bonusy = random.randrange(hoehe) // groeße * groeße


    pygame.mouse.set_visible(False)
    #pygame.mouse.set_pos(mposx)
    #pygame.mouse.set_pos(mposx, mposy)

    pygame.mouse.set_visible(True)
    #pygame.mouse.set_pos(mposx, mposy)
    #pygame.mouse.set_visible(False)

    while verzoegert == True:
        screen.fill(bg)
        startmessage = pygame.font.Font(path+'UbuntuMono-R.ttf', 90).render(f'LOS GEHTS!', False, (150, 100, 50))
        startmessage_rect = startmessage.get_rect(center=(breite/2, hoehe/2))
        screen.blit(startmessage, startmessage_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                verzoegert = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_AC_BACK or event.key == pygame.K_ESCAPE:
                    verzoegert = False
                    run = False
                    ende = False
                    neustart = False
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    verzoegert = False
        pygame.display.update()

    if nochmal == 0:
        channel6.play(newgameton)
    if nochmal >= 1:
        channel6.play(ichgehejetzt)

    while run:
        clock.tick(tempo // 5)
        
        screen.fill(bg)
        vorletztesnake = letztesnake[0], letztesnake[1]
        letztesnake = x, y

        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False

            # Tastatureingabe abfragen (z.16)

            # Mauseingabe abfragen
            if event.type == pygame.MOUSEBUTTONDOWN:
                mposx, mposy = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                if dbclock.tick() < DOUBLECLICKTIME and doublecheck == True:
                    doublecheck = False
                    mx, my = pygame.mouse.get_pos()
                    if letztex == 1:
                        letztex, letztey = richtungx, richtungy
                        richtungx, richtungy = (-1, 0)
                        invertx = (1, 0)
                    elif letztex == -1:
                        letztex, letztey = richtungx, richtungy
                        richtungx, richtungy = (1, 0)
                        invertx = (-1, 0)
                    elif letztey == 1:
                        letztex, letztey = richtungx, richtungy
                        richtungx, richtungy = (0, -1)
                        inverty = (0, 1)
                    elif letztey == -1:
                        letztex, letztey = richtungx, richtungy
                        richtungx, richtungy = (0, 1)
                        inverty = (0, -1)
                else:
                    doublecheck = True
                    mx, my = pygame.mouse.get_pos()
                    # links
                    if mx < mposx:
                        mxdif = mposx - mx
                        mxrichtung = (-1, 0)
                        invertx = (1, 0)
                    # rechts
                    if mx > mposx:
                        mxdif = mx - mposx
                        mxrichtung = (1, 0)
                        invertx = (-1, 0)
                    # hoch
                    if my < mposy:
                        mydif = mposy - my
                        myrichtung = (0, -1)
                        inverty = (0, 1)
                    # runter
                    if my > mposy:
                        mydif = my - mposy
                        myrichtung = (0, 1)
                        inverty = (0, -1)

                    if mxdif > mydif and (richtungx, richtungy) != invertx:
                        letztex, letztey = richtungx, richtungy
                        richtungx, richtungy = mxrichtung
                    if mydif > mxdif and (richtungx, richtungy) != inverty:
                        letztex, letztey = richtungx, richtungy
                        richtungx, richtungy = myrichtung

                    #pygame.mouse.set_pos(mposx, mposy)

            if event.type == pygame.KEYDOWN and event.key in richtungen and (richtungx, richtungy) != invert[event.key]:
                    letztex, letztey = richtungx, richtungy
                    richtungx, richtungy = richtungen[event.key]

            # # Ende
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_AC_BACK or event.key == pygame.K_ESCAPE:
                    channel8.play(pauseton)
                    wait = True

        # Pause
        while wait == True:
            screen.fill(bg2)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    wait = False
                    channel9.play(startton)
                    screen.fill(bg)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_AC_BACK or event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        wait = False
                        run = False
                        ende = True
                        neustart = False
                    if event.key == pygame.K_RETURN:
                        wait = False
                        channel9.play(startton)
                        screen.fill(bg)
            farbe = (255, 0, 0)
            for x, y in snake:
                pygame.draw.rect(screen, (farbe), (x, y, groeße, groeße))
            pygame.draw.rect(screen, (255, 0, 0), (bonusx, bonusy, groeße, groeße))
            pygame.draw.rect(screen, (255, 0, 0), (bonusx2, bonusy2, groeße, groeße))
            pygame.draw.rect(screen, (255, 0, 0), (multibonusx1, multibonusy1, groeße, groeße))
            pygame.display.update()

        x, y = snake[-1]
        x, y = x + richtungx * groeße, y + richtungy * groeße
        if (x, y) == (vorletztesnake[0], vorletztesnake[1]):
            x, y = snake[-1]
            x, y = x + letztex * groeße, y + letztey * groeße

        laenge = len(snake)

        #verhungern
        if verhungern < 300 and verhungern > 0:
            if hungerfarbe2 > 35:
                hungerfarbe2 = hungerfarbe2 - 1
            elif hungerfarbe2 <= 35:
                if hungerfarbe2 >= 0 and hungerfarbe1 <= 253:
                    if hungerfarbe2 > 0:
                        hungerfarbe2 = hungerfarbe2 - 1
                    hungerfarbe1 = hungerfarbe1 + 2
                if hungerfarbe1 >= 245:
                    hungerfarbe1 = hungerfarbe1 + 1
            if hungerfarbe1 >= 255:
                hungerfarbe1 = 255
                score = score -10
                if score <= -1:
                    tot = 1
            if hungerfarbe2 >= 255:
                hungerfarbe2 = 255
            hfarbe = (hungerfarbe1,hungerfarbe2,hungerfarbe3)
            
        if verhungern >= 0:
            verhungern = verhungern - 1

        # Superbonus Features und Zeit
        if superbonus > 0:
            if x < 0:
                x = breite - groeße
            if x + groeße > breite:
                x = 0
            if y < 0:
                y = hoehe - groeße
            if y + groeße > hoehe:
                y = 0
            bg = (0, 12, 2)
            if superbonus < sbzeit and bgint == 0:
                bg = (100, 0, 0)
                bgint = 2
                if alarmcheck == 0:
                    channel1.play(alarmton)
                    alarmcheck = 1
            else:
                if superbonus < sbzeit and bgint > 0:
                    bg = (20, 20, 20)
                    bgint = bgint - 1

        else:
            bg = (20, 20, 20)

        # Gueltigkeitspruefung
        if x < 0 or x + groeße > breite or y < 0 or y + groeße > hoehe or (x, y) in snake and superbonus == 0 or tot == 1:
            ende = True
            run = False
            if laenge > 12 and tot == 0:
                ranups = random.randrange(3)
                if ranups == 0:
                    channel6.play(dummesau)
                if ranups == 1:
                    channel6.play(amarsch)
                if ranups == 2:
                    channel6.play(gratain)
            if laenge <= 12  and tot == 0:
                ranups = random.randrange(2)
                if ranups == 0:
                    channel6.play(sobloed)
                if ranups == 1:
                    channel6.play(wegschaffen)
            if tot == 1:
                score = 0
                channel6.play(wegschaffen)


        snake.append((x, y))
        # Bonus essen
        if x == bonusx and y == bonusy:
            score += cash
            tempo += 1
            cash += multi
            if verhungern < 460:
                verhungern = 460
            if hungerfarbe2 < 195:
                hungerfarbe2 = hungerfarbe2 + 60
            elif hungerfarbe2 >= 195:
                hungerfarbe2 = 255
            if hungerfarbe1 > 0:
                hungerfarbe1 = 0
            hfarbe = (hungerfarbe1,hungerfarbe2,hungerfarbe3)
            farbe = hfarbe
            multibonusint = multibonusint + 1
            bonusx = random.randrange(breite) // groeße * groeße
            bonusy = random.randrange(hoehe) // groeße * groeße
            while (bonusx, bonusy) in snake or (bonusx, bonusy) in (bonusx2, bonusy2) or (bonusx, bonusy) in (multibonusx1, multibonusy1) or (bonusx, bonusy) in (multibonusx2, multibonusy2) or (bonusx, bonusy) in (multibonusx3, multibonusy3):
                bonusx = random.randrange(breite) // groeße * groeße
                bonusy = random.randrange(hoehe) // groeße * groeße
            
            # Superbonus
            laenge = len(snake)
            # hier
            if laenge > 12 and bonus2int == 0:
                bonus2ran = random.randrange(18)  # 17
                if bonus2ran == 3:
                    bonus2ran = bonus2ran - 1
                    bonus2int = 120
                    hallocheck = 1
                    schade = 1
                    bonusx2 = random.randrange(breite) // groeße * groeße
                    bonusy2 = random.randrange(hoehe) // groeße * groeße
                    while (bonusx2, bonusy2) in snake or (bonusx2, bonusy2) in (bonusx, bonusy) or (bonusx2, bonusy2) in (multibonusx1, multibonusy1) or (bonusx2, bonusy2) in (multibonusx2, multibonusy2) or (bonusx2, bonusy2) in (multibonusx3, multibonusy3):
                        bonusx2 = random.randrange(breite) // groeße * groeße
                        bonusy2 = random.randrange(hoehe) // groeße * groeße
            if hallocheck == 0:
                if multibonusint < 10:
                    channel5.play(jamjamton)
                else:
                    channel7.play(peng)
            else:
                channel3.play(halloton)
                hallocheck = 0

        # superbonus essen
        elif x == bonusx2 and y == bonusy2:
            while (bonusx2, bonusy2) in snake:
                bonusx2 = random.randrange(breite) // groeße * groeße
                bonusy2 = random.randrange(hoehe) // groeße * groeße
            verhungern = 460
            hungerfarbe1 = 0
            hungerfarbe2 = 255
            hungerfarbe3 = 0
            bonus2int = 0
            schade = 0
            superbonus = 450
            score = score + (cash * 2)
            tempo = tempo + 2
            multi += 0.5
            bonusx2 = -100
            bonusy2 = -110
            ranups = random.randrange(2)
            if ranups == 0:
                channel4.play(huiton)
            if ranups == 1:
                channel4.play(nichtnormal)
            verlaengern = 3
            alarmcheck = 0
        
        #Multibonus1 essen
        elif x == multibonusx1 and y == multibonusy1:
            multibonusx1 = -50
            multibonusy1 = -60
            tempo = tempo - 6
            score = score + cash
            multi = multi + 0.1
            cash = cash + multi
            if verhungern < 460:
                verhungern = 460
            if hungerfarbe2 < 195:
                hungerfarbe2 = hungerfarbe2 + 60
            elif hungerfarbe2 >= 195:
                hungerfarbe2 = 255
            if hungerfarbe1 > 0:
                hungerfarbe1 = 0
            hfarbe = (hungerfarbe1,hungerfarbe2,hungerfarbe3)
            farbe = hfarbe
            channel7.play(nesch)
            

        else:
            if laenge >= 5 and verlaengern == 0:
                del snake[0]
            if verlaengern > 0:
                verlaengern = verlaengern - 1

        # Draw the Schnaeggler =)
        for x, y in snake:
            pygame.draw.rect(screen, (farbe), (x, y, groeße, groeße))
         # Draw the Bonus =)
        pygame.draw.rect(screen, (255, 0, 0),
                            (bonusx, bonusy, groeße, groeße))

        if score >= 1000 and tatuetatacheck1 == 0:
            channel7.play(tatuetata2ton)
            tatuetatacheck1 = 1
            tempo = tempo - 1

        if score >= 2000 and tatuetatacheck2 == 0:
            channel7.play(tatuetataton)
            tatuetatacheck2 = 1
            tempo = tempo - 2

        if score >= 4000 and tatuetatacheck3 == 0:
            channel7.play(tatuetata2ton)
            tatuetatacheck3 = 1
            tempo = tempo - 4

        if score >= 8000 and tatuetatacheck4 == 0:
            channel7.play(tatuetataton)
            tatuetatacheck4 = 1
            tempo = tempo - 8

        # Draw the superbonus blinken
        if bonus2int > 0:
            ff1 = random.randrange(255)
            ff2 = random.randrange(255)
            ff3 = random.randrange(255)
            ffarbe = ff1, ff2, ff3
            pygame.draw.rect(screen, (ffarbe),
                                (bonusx2, bonusy2, groeße, groeße))
            bonus2int = bonus2int - 1
            hungerfarbe1 = 0
            hungerfarbe2 = 255

        # Superbonus verpasst
        elif bonus2int == 0:
            if schade == 1:
                channel7.play(endeton)
                schade = 0
            bonusx2 = -100
            bonusy2 = -110

        # Multibonus
        if multibonus1dauer > 0:
            multibonus1dauer = multibonus1dauer - 1
        else:
            multibonusx1 = -50
            multibonusy1 = -60
        if multibonusint == 10:
            multibonusint = 0
            multibonus1dauer = 250
            multibonusx1 = random.randrange(breite) // groeße * groeße
            multibonusy1 = random.randrange(hoehe) // groeße * groeße
            while (multibonusx1, multibonusy1) in snake or (multibonusx1, multibonusy1) in (bonusx, bonusy) or (multibonusx1, multibonusy1) in (bonusx2, bonusy2):
                multibonusx1 = random.randrange(breite) // groeße * groeße
                multibonusy1 = random.randrange(hoehe) // groeße * groeße

        # Draw the Multibonus blinken
        if m1fwechsel == 0:
            m1fwechsel = 1
        elif m1fwechsel == 1:
            m1fwechsel = 0
        if m1fwechsel == 0:
            m1f = m1farbe1
        elif m1fwechsel == 1:
            m1f = m1farbe2
        pygame.draw.rect(screen, (m1f), (multibonusx1, multibonusy1, groeße, groeße))

        # superbonus schlange blinken
        if superbonus > 0:
            f1 = random.randrange(255)
            f2 = random.randrange(255)
            f3 = random.randrange(255)
            farbe = f1, f2, f3
            superbonus = superbonus - 1
        else:
            farbe = (hfarbe)

        if score > 0:
            score = score // 1
            score = int(score)

        ergebnis = pygame.font.Font(path+'simple_small_pixels.ttf', 24).render(
            f'Laenge: {laenge}, Tempo: {tempo -39}, Punkte: {score}', False, (250, 250, 250))
        screen.blit(ergebnis, (breite - ergebnis.get_width(), 5))

        pygame.display.flip()

    # Highscore
    while ende:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                neustart = True
                run = True
                ende = False
                nochmal = nochmal + 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_AC_BACK or event.key == pygame.K_ESCAPE:
                    ende = False
                    neustart = False
                    pygame.quit()
                    ende = False
                    neustart = False
        screen.fill(bg2)
        farbe = (255, 0, 0)
        for x, y in snake:
            pygame.draw.rect(screen, (farbe), (x, y, groeße, groeße))
        pygame.draw.rect(screen, (255, 0, 0), (bonusx, bonusy, groeße, groeße))
        datei = open(path+'hscore.txt', 'r')
        hscore = datei.read()
        datei.close()
        hscore = hscore.rstrip()
        hscore = int(hscore)
        score = int(score)
        hscore1 = pygame.font.Font(path+'DejaVuSansMono.ttf', 88).render(f'Highscore: {hscore}', False, (250, 50, 50))
        hscore1_rect = hscore1.get_rect(center=(breite/2, hoehe/3))
        screen.blit(hscore1, hscore1_rect)
        ergebnis1 = pygame.font.Font(path+'DejaVuSansMono.ttf', 88).render(f'dein Score: {score}', False, (250, 250, 250))
        ergebnis1_rect = ergebnis1.get_rect(center=(breite/2, hoehe/2))
        screen.blit(ergebnis1, ergebnis1_rect)
        if score >= hscore:
            newHscore = pygame.font.Font(path+'DejaVuSansMono.ttf', 88).render(f'NEUER REKORD!', False, (150, 100, 50))
            newHscore_rect = newHscore.get_rect(center=(breite/2, hoehe/3*2))
            screen.blit(newHscore, newHscore_rect)
        if score > hscore:
            score = str(score)
            datei = open(path+'hscore.txt', 'w')
            datei.write(score)
            datei.close()
        pygame.display.update()

pygame.quit()
