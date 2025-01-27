from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.raw import GL
from ctypes import BigEndianStructure
from sys import flags
import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU
import math

def hurufG():
    glBegin(GL_LINE_LOOP)
    glColor3ub(227, 7, 7)
    glVertex2f(120,280)
    glVertex2f(60,280)
    glVertex2f(60,220)
    glVertex2f(120,220)
    glVertex2f(120,240)
    glVertex2f(87.668095703125,239.7838281249982)
    glVertex2f(87.668095703125,233.8077343749982)
    glVertex2f(111.8884082031251,233.8242968749981)
    glVertex2f(111.946689453125,225.8899218749982)
    glVertex2f(68.190126953125,225.7316406249982)
    glVertex2f(68.231845703125,273.8053906249984)
    glVertex2f(119.8896582031251,273.7636718749985)
    glEnd()

def hurufA():
    glBegin(GL_LINE_LOOP)
    glColor3ub(227, 7, 7)
    glVertex2f(149.2,280)
    glVertex2f(149.2,220)
    glVertex2f(157.160239257812,219.9734912109364)
    glVertex2f(157.080600585937,240.0358935546864)
    glVertex2f(177.102280273437,240.0155322265614)
    glVertex2f(177.122641601562,220.0734912109364)
    glVertex2f(185.4334814453121,220.0938525390614)
    glVertex2f(185.392758789062,279.9606982421863)
    glEnd()

def kotakA():
    glBegin(GL_LINE_LOOP)
    glColor3ub(227, 7, 7)
    glVertex2f(161.8342871093745,267.9539355468735)
    glVertex2f(161.8342871093745,256.0073535156235)
    glVertex2f(172.8672949218745,255.9937792968736)
    glVertex2f(172.8537207031245,268.0403613281235)
    glEnd()

def hurufM():
    glBegin(GL_LINE_LOOP)
    glColor3ub(227, 7, 7)  
    glVertex2f(210.2,280)
    glVertex2f(210.2,220)
    glVertex2f(218.358759751389,219.9134037189073)
    glVertex2f(218.358759751389,239.8616716728522)
    glVertex2f(230.0372207116659,229.0918646791842)
    glVertex2f(242.298373738725,239.8616716728522)
    glVertex2f(242.4766429454032,219.9134037189073)
    glVertex2f(250.2,219.9)
    glVertex2f(250.2,280)
    glVertex2f(242.298373738725,279.93647678742)
    glVertex2f(230.0502975383788,269.6618634264535)
    glVertex2f(218.158759751389,280.0147459940981)
    glEnd()  

def hurufE():
    glBegin(GL_LINE_LOOP)
    glColor3ub(227, 7, 7) 
    glVertex2f(280,280)
    glVertex2f(280,220)
    glVertex2f(340,220)
    glVertex2f(340.1533805625374,227.735328836334)
    glVertex2f(289.7771944710805,227.735328836334)
    glVertex2f(289.7562243711337,247.8354750330441)
    glVertex2f(339.8324104625905,247.956445132991)
    glVertex2f(339.8324104625905,255.8387574317705)
    glVertex2f(289.8771944710805,255.9806976316645)
    glVertex2f(289.7562243711337,272.0292026290113)
    glVertex2f(340,272.0082325290644)
    glVertex2f(340,280)
    glEnd()

def hurufO():
    glBegin(GL_LINE_LOOP)
    glColor3ub(56, 25, 255)
    glVertex2f(78.2,180)
    glVertex2f(78.2,120)
    glVertex2f(138.2,120)
    glVertex2f(138.2,180)
    glEnd()

def kotakO():
    glBegin(GL_LINE_LOOP)
    glColor3ub(56, 25, 255)  
    glVertex2f(101.9584308634801,168.0659446818844)
    glVertex2f(101.9451549665081,131.9387077003506)
    glVertex2f(114.100843190658,131.9254318033787)
    glVertex2f(114.100843190658,168.0526687849125)
    glEnd()  

def hurufV():
    glBegin(GL_LINE_LOOP)
    glColor3ub(56, 25, 255)
    glVertex2f(148.8,180.1)
    glVertex2f(148.8248800163725,131.9376445194583)
    glVertex2f(168.8,120.1)
    glVertex2f(188.8,120.1)
    glVertex2f(208.8,132.3106995398362)
    glVertex2f(208.8,180.1)
    glVertex2f(188.6489776451199,180.1617421482057)
    glVertex2f(188.7489776451199,140.2873597843706)
    glVertex2f(178.5967960963997,131.7376445194583)
    glVertex2f(168.7356956888422,140.2143047639927)
    glVertex2f(168.7356956888422,179.9886871278278)
    glEnd()

def hurufe():
    glBegin(GL_LINE_LOOP)
    glColor3ub(56, 25, 255)
    glVertex2f(220.4,180)
    glVertex2f(220.4,120)
    glVertex2f(260.4,120)
    glVertex2f(260.4,136.1)
    glVertex2f(240.4,136.1)
    glVertex2f(240.438776731135,140.0962691868322)
    glVertex2f(260.2664973467387,140.0962691868322)
    glVertex2f(260.4,180)
    glEnd()

def kotake():
    glBegin(GL_LINE_LOOP)
    glColor3ub(56, 25, 255)
    glVertex2f(231.5846642119603,167.1632539237781)
    glVertex2f(231.5846642119603,160.0489469443287)
    glVertex2f(245.3413236492925,159.9849242051102)
    glVertex2f(245.3233350189017,167.0992311845596)
    glEnd()

def hurufR():
    glBegin(GL_LINE_LOOP)
    glColor3ub(56, 25, 255)
    glVertex2f(273.6,180)
    glVertex2f(273.6,120)
    glVertex2f(293.5999999999894,120)
    glVertex2f(293.5999999999894,160.1)
    glVertex2f(300.6092042326914,160.0621847851)
    glVertex2f(300.6092042326914,148.1663541364676)
    glVertex2f(321.7853570164467,148.1079049878185)
    glVertex2f(321.7438061650959,180.0305833121012)
    glEnd()

def garis():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 219, 102)
    glVertex2f(4.1006355831095,208.1914454303304)
    glVertex2f(396.2625928532671,208.5218591874964)
    glVertex2f(396.2972650783873,192.34898164708)
    glVertex2f(4.0919977509034,192.24898164708)
    glEnd()

def lawan():
    glBegin(GL_POLYGON)
    glColor3ub(230, 151, 5)
    glVertex2f(195.3840770953681,193.4984491624837)
    glVertex2f(195.5290105585204, 199.8227412877697)
    glVertex2f(195.5,200.5999999999693)
    glVertex2f(195.6448565052546,201.293554173665)
    glVertex2f(195.8333717413171,201.9219382938732)
    glVertex2f(196.2104022134421,202.4246455900397)
    glVertex2f(196.6502710975879,202.9273528862063)
    glVertex2f(197.0901399817338,203.4300601823728)
    glVertex2f(197.6556856899213,203.8070906544977)
    glVertex2f(198.1840698101297,204.1469595386435)
    glVertex2f(198.812453930338,204.4983131867268)
    glVertex2f(199.4151612265047,204.74966683481)
    glVertex2f(200.043545346713,204.8125052468308)
    glVertex2f(200.797606290963,204.74966683481)
    glVertex2f(201.4888288231923,204.6868284227892)
    glVertex2f(202.1800513554214,204.3726363626851)
    glVertex2f(202.8084354756298,204.1212827146018)
    glVertex2f(203.3739811838173,203.7442522424769)
    glVertex2f(203.876688479984,203.2415449463104)
    glVertex2f(204.253718952109,202.7388376501438)
    glVertex2f(204.630749424234,202.1732919419565)
    glVertex2f(204.9449414843382,201.5449078217483)
    glVertex2f(205.2,200.8999999999693)
    glVertex2f(205.4,200.1999999999693)
    glVertex2f(205.384810368484,199.4712402250613)
    glVertex2f(205.4476487805048,193.5644294951044)
    glEnd()

def mataLawan1():
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3ub(0,0,0)
    glVertex2f(198.9833614333042,199.9712915978218)
    glEnd()

def mataLawan2():
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3ub(0,0,0)
    glVertex2f(202.9332519427099,199.9248222977111)
    glEnd()

def lawan2():
    glBegin(GL_POLYGON)
    glColor3ub(21, 171, 235)
    glVertex2f(215.8840770953669,193.4984491624837)
    glVertex2f(216.0290105585193,199.8227412877697)
    glVertex2f(216,200.5999999999693)
    glVertex2f(216.1448565052534,201.293554173665)
    glVertex2f(216.3333717413159,201.9219382938732)
    glVertex2f(216.7104022134409,202.4246455900397)
    glVertex2f(217.1502710975867,202.9273528862063)
    glVertex2f(217.5901399817326,203.4300601823728)
    glVertex2f(218.1556856899201,203.8070906544977)
    glVertex2f(218.6840698101285,204.1469595386435)
    glVertex2f(219.3124539303368,204.4983131867268)
    glVertex2f(219.9151612265035,204.74966683481)
    glVertex2f(220.5435453467118,204.8125052468308)
    glVertex2f(221.2976062909618,204.74966683481)
    glVertex2f(221.9888288231911,204.6868284227892)
    glVertex2f(222.6800513554202,204.3726363626851)
    glVertex2f(223.3084354756286,204.1212827146018)
    glVertex2f(223.8739811838161,203.7442522424769)
    glVertex2f(224.3766884799828,203.2415449463104)
    glVertex2f(224.7537189521078,202.7388376501438)
    glVertex2f(225.1307494242328,202.1732919419565)
    glVertex2f(225.444941484337,201.5449078217483)
    glVertex2f(225.7,200.8999999999693)
    glVertex2f(225.9,200.1999999999693)
    glVertex2f(225.8848103684828,199.4712402250613)
    glVertex2f(225.9476487805036,193.5644294951044)
    glEnd()

def mataLawan21():
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3ub(0,0,0)
    glVertex2f(219.483361433303,199.9712915978218)
    glEnd()

def mataLawan22():
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3ub(0,0,0)
    glVertex2f(223.4332519427087,199.9248222977111)
    glEnd()

def lawan3():
    glBegin(GL_POLYGON)
    glColor3ub(191, 2, 134)
    glVertex2f(171.0840770953694,193.4984491624837)
    glVertex2f(171.2290105585218,199.8227412877697)
    glVertex2f(171.2,200.5999999999693)
    glVertex2f(171.3448565052559,201.293554173665)
    glVertex2f(171.5333717413184,201.9219382938732)
    glVertex2f(171.9104022134434,202.4246455900397)
    glVertex2f(172.3502710975892,202.9273528862063)
    glVertex2f(172.7901399817351,203.4300601823728)
    glVertex2f(173.3556856899226,203.8070906544977)
    glVertex2f(173.884069810131,204.1469595386435)
    glVertex2f(174.5124539303393,204.4983131867268)
    glVertex2f(175.115161226506,204.74966683481)
    glVertex2f(175.7435453467143,204.8125052468308)
    glVertex2f(176.4976062909643,204.74966683481)
    glVertex2f(177.1888288231936,204.6868284227892)
    glVertex2f(177.8800513554227,204.3726363626851)
    glVertex2f(178.5084354756311,204.1212827146018)
    glVertex2f(179.0739811838186,203.7442522424769)
    glVertex2f(179.5766884799853,203.2415449463104)
    glVertex2f(179.9537189521103,202.7388376501438)
    glVertex2f(180.3307494242353,202.1732919419565)
    glVertex2f(180.6449414843395,201.5449078217483)
    glVertex2f(180.9,200.8999999999693)
    glVertex2f(181.1,200.1999999999693)
    glVertex2f(181.0848103684853,199.4712402250613)
    glVertex2f(181.1476487805061,193.5644294951044)
    glEnd()

def mataLawan31():
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3ub(0,0,0)
    glVertex2f(174.6833614333055,199.9712915978218)
    glEnd()

def mataLawan32():
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3ub(0,0,0)
    glVertex2f(178.6332519427112,199.9248222977111)
    glEnd()

def titik():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(110,200)
    glEnd()

def titik1():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(110,200)
    glEnd()

def titik2():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(120,200)
    glEnd()

def titik3():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(130,200)
    glEnd()

def titik4():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(140,200)
    glEnd()

def titik5():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(150,200)
    glEnd()

def titik6():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(160,200)
    glEnd()

def titik7():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(240,200)
    glEnd()

def titik8():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(250,200)
    glEnd()

def titik9():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(260,200)
    glEnd()

def titik10():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(270,200)
    glEnd()

def titik11():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(280,200)
    glEnd()

def titik12():
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3ub(255,255,255)
    glVertex2f(290,200)
    glEnd()    

def iterate():
    # ke kanan, atas, kiri, bawah
    glViewport(-50, -20, 705, 638)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 400, 0, 400, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # untuk membersihkan layar
    glLoadIdentity() # untuk mereset semua posisi grafik/bentuk
    iterate() # fungsi looping
    glColor3f(1.0, 0.0, 0.0)
    hurufG()
    hurufA()
    kotakA()
    hurufM()
    hurufE()
    hurufO()
    kotakO()
    hurufV()
    hurufe()
    kotake()
    hurufR()
    garis()
    lawan()
    mataLawan1()
    mataLawan2()
    lawan2()
    mataLawan21()
    mataLawan22()
    lawan3()
    mataLawan31()
    mataLawan32()
    titik1()
    titik2()
    titik3()
    titik4()
    titik5()
    titik6()
    titik7()
    titik8()
    titik9()
    titik10()
    titik11()
    titik12()

    glutSwapBuffers()

glutInit(sys.argv)  # inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) # mengatur layar supaya berwarna
glutInitWindowSize(600, 600) # mengatur ukuran layar/window
glutInitWindowPosition(750, 0) # mangatur posisi window
glutCreateWindow("Snake Man") # untuk memberi nama window
glutDisplayFunc(showScreen) # untuk menampilkan objek pada layar
glutIdleFunc(showScreen) # untuk menuruh opengl untuk selalu menampilkan dan membuka objek
glutMainLoop() #untuk memulai segalanya