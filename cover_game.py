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


def latarBelakang():
    glBegin(GL_POLYGON)
    glColor3ub(164, 203, 247)
    glVertex2f(0, 100)
    glVertex2f(0, 700)
    glVertex2f(700, 700)
    glVertex2f(700, 100)
    glVertex2f(0, 100)
    glVertex2f(700, 100)
    glVertex2f(700, 0)
    glVertex2f(0, 0)
    glEnd()

def coba():
    glBegin(GL_POLYGON)
    glColor3ub(247, 240, 12)
    glVertex2f(100,300)
    glVertex2f(300,300)
    glVertex2f(300,100)
    glVertex2f(100,100)
    glEnd()

def hurufS():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(100,280.0212109374983)
    glVertex2f(100,269.5703124999976)
    glVertex2f(60,269.5133593749981)
    glVertex2f(60,240)
    glVertex2f(100,240.0401171874984)
    glVertex2f(100,209.7980078124986)
    glVertex2f(50,210)
    glVertex2f(50,220)
    glVertex2f(80,220)
    glVertex2f(79.9794238281251,229.5322656249983)
    glVertex2f(49.993603515625,229.7885546874985)
    glVertex2f(49.993603515625,280.0212109374983)
    glVertex2f(100,280.0212109374983)
    glEnd()

def hurufN():
    glBegin(GL_LINE_LOOP)
    glColor3ub(212, 36, 36)
    glVertex2f(103.845495256697,240.1011383928545)
    glVertex2f(103.9539773995541,210.1600669642834)
    glVertex2f(107.9678166852684,210.1600669642834)
    glVertex2f(108.0762988281256,235.7618526785689)
    glVertex2f(116,210)
    glVertex2f(120,210)
    glVertex2f(120,240)
    glVertex2f(115.8870131138399,240.1011383928545)
    glVertex2f(116.2667006138399,224.9949999999983)
    glVertex2f(110,240)
    glEnd()

def hurufA():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 238, 0)
    glVertex2f(125,240)
    glVertex2f(125,210)
    glVertex2f(130,210)
    glVertex2f(130,220)
    glVertex2f(137.31826311384,219.9777008928557)
    glVertex2f(137.4629059709829,209.9973437499986)
    glVertex2f(142.3807631138401,209.9250223214272)
    glVertex2f(142.1637988281258,239.8660937499985)
    glEnd()

def kotakA():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 238, 0)
    glVertex2f(130,225)
    glVertex2f(137.31826311384,225.0402008928557)
    glVertex2f(137.31826311384,232.9835044642847)
    glVertex2f(129.9896916852686,232.9835044642847)
    glEnd()

def hurufK():
    glBegin(GL_LINE_LOOP)
    glColor3ub(25, 230, 35)
    glVertex2f(145.9925803407316,240.1000748424357)
    glVertex2f(145.9925803407316,210.0441399684862)
    glVertex2f(150,210)
    glVertex2f(150.012800928967,222.5514929096626)
    glVertex2f(152.5015089121603,224.9125748424357)
    glVertex2f(156.840794626446,210.0441399684862)
    glVertex2f(160.7972021894712,209.9803269432761)
    glVertex2f(156.075038323925,226.8907786239483)
    glVertex2f(161.1800803407318,239.9086357668054)
    glVertex2f(157.3512988281267,240.1000748424357)
    glVertex2f(150.076613954177,227.0184046743685)
    glVertex2f(150,240)
    glEnd()

def hurufE():
    glBegin(GL_LINE_LOOP)
    glColor3ub(212, 36, 36)
    glVertex2f(165.9056818440426,240.0204803065044)
    glVertex2f(165.9056818440427,209.9895385039463)
    glVertex2f(185,210)
    glVertex2f(185.0062440934641,212.9705511093473)
    glVertex2f(170.9844440606518,212.9705511093473)
    glVertex2f(170.9844440606518,225.0050094052253)
    glVertex2f(185,225)
    glVertex2f(185.0062440934641,228.0412259477634)
    glVertex2f(170.9844440606518,228.0412259477634)
    glVertex2f(171.0396479977888,236.9290598268293)
    glVertex2f(184.951040156327,236.9290598268293)
    glVertex2f(185,240)
    glEnd()

def hurufM():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(200,280)
    glVertex2f(200.0318875719915,208.1154275698907)
    glVertex2f(219.7218145820979,207.7978481019858)
    glVertex2f(220,240)
    glVertex2f(240,220)
    glVertex2f(260,240)
    glVertex2f(259.7368275381205,208.1789434634717)
    glVertex2f(279.9348816968747,208.1789434634717)
    glVertex2f(280,280)
    glVertex2f(260,280)
    glVertex2f(240,260)
    glVertex2f(220,280)
    glEnd()

def hurufA2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 238, 0)
    glVertex2f(292.0891440470528,239.2378092770281)
    glVertex2f(292.0891440470528,209.2378092770281)
    glVertex2f(297.0891440470528,209.2378092770281)
    glVertex2f(297.0891440470528,219.2378092770281)
    glVertex2f(304.4074071608927,219.2155101698839)
    glVertex2f(304.5520500180356,209.2351530270268)
    glVertex2f(309.4699071608928,209.1628315984554)
    glVertex2f(309.2529428751785,239.1039030270267)
    glEnd()

def kotakA2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(255, 238, 0)
    glVertex2f(297.0891440470527,224.2378092770281)
    glVertex2f(304.4074071608927,224.2780101698839)
    glVertex2f(304.4074071608927,232.2213137413129)
    glVertex2f(297.0788357323213,232.2213137413129)
    glEnd()

def hurufN2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(212, 36, 36)
    glVertex2f(320.5349073724348,239.3106753748914)
    glVertex2f(320.5349073724348,209.3738022820341)
    glVertex2f(324.9482006083052,209.3738022820341)
    glVertex2f(324.861341266656,234.3024333353584)
    glVertex2f(332.6894121157378,209.2095369820369)
    glVertex2f(336.6894121157378,209.2095369820369)
    glVertex2f(336.6894121157378,239.2095369820369)
    glVertex2f(332.5764252295777,239.3106753748914)
    glVertex2f(332.9561127295777,224.2045369820352)
    glVertex2f(326.6894121157378,239.2095369820369)
    glEnd()

def labirin():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(30,250)
    glVertex2f(37.9368168942501,250.117846426271)
    glVertex2f(37.9368168942501,297.7550332339527)
    glVertex2f(189.9885031756385,297.7550332339527)
    glVertex2f(190,295)
    glVertex2f(40.8097318904695,294.9353203672934)
    glVertex2f(40.8097318904695,247.7237505960871)
    glVertex2f(30,247.7237505960871)
    glEnd()

def labirin2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex(370, 250)
    glVertex(361.8828707858499,249.9310287524296)
    glVertex(361.8828707858499,297.796256212529)
    glVertex(189.9654568137909,297.7306254878853)
    glVertex(190,295)
    glVertex(359.305774499644,295.145641698005)
    glVertex(359.4819332085392,247.8110926272403)
    glVertex(370.0338244718801,247.8875556074095)
    glEnd()    

def labirin3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(30,240)
    glVertex2f(37.90370248052,240.0793087242017)
    glVertex2f(37.90370248052,159.9123057046984)
    glVertex2f(129.9415671877084,159.9206000266868)
    glVertex2f(129.9531664218872,161.9134994521965)
    glVertex2f(40.5970602894756,162.2887978890706)
    glVertex2f(40.5970602894756,241.9805024716998)
    glVertex2f(30,241.9805024716998)
    glEnd()

def labirin4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex(370,240)
    glVertex(362.2299170573797,239.9918619329592)
    glVertex(362.1742779812288,159.8994118129034)
    glVertex(130,160)
    glVertex(129.9367741249504,161.9024185543567)
    glVertex(359.169767869048,161.9024185543567)
    glVertex(359.281046021351,241.9226882124882)
    glVertex(369.9637486424352,241.9114100601852)
    glEnd()

def kotak():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(48,188)
    glVertex2f(48,184)
    glVertex2f(54,184)
    glVertex2f(54,188)
    glEnd()

def kotak2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(62,188)
    glVertex2f(62,184)
    glVertex2f(94,184)
    glVertex2f(94,188)
    glEnd()

def kotak3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(106,184)
    glVertex2f(122,184)
    glVertex2f(122,172)
    glVertex2f(126,172)
    glVertex2f(126,184)
    glVertex2f(142,184)
    glVertex2f(142,188)
    glVertex2f(106,188)
    glEnd()

def kotak4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(113.8648339339726,276.3353499362257)
    glVertex2f(113.8648339339726,272.3353499362257)
    glVertex2f(142.4788306396927,272.3547934087275)
    glVertex2f(142.4311899648308,276.468495187454)
    glEnd()

def kotak5():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(154.2527383918463,276.5039162300916)
    glVertex2f(154.2660472246916,272.599539365163)
    glVertex2f(189.0806568669568,272.5871615927259)
    glVertex2f(189.1255998303104,276.5411541579805)
    glEnd()

def kotak6():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(158,161.9024185543567)
    glVertex2f(162,161.9024185543567)
    glVertex2f(162,196)
    glVertex2f(158,196)
    glEnd()

def kotak7():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(183,178)
    glVertex2f(183,174)
    glVertex2f(213,174)
    glVertex2f(213,178)
    glEnd()

def kotak8():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(298,280)
    glVertex2f(298,252)
    glVertex2f(338,252)
    glVertex2f(338,256)
    glVertex2f(302,256)
    glVertex2f(302,280)
    glEnd()

def kotak9():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(246,162)
    glVertex2f(246,174)
    glVertex2f(250,174)
    glVertex2f(250,162)
    glEnd()

def kotak10():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(286,162)
    glVertex2f(290,162)
    glVertex2f(290,174)
    glVertex2f(286,174)
    glEnd()

def kotak11():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(288,194)
    glVertex2f(288,190)
    glVertex2f(306,190)
    glVertex2f(306,180)
    glVertex2f(310,180)
    glVertex2f(310,190)
    glVertex2f(328,190)
    glVertex2f(328,194)
    glEnd()

def kotak12():
    glBegin(GL_LINE_LOOP)
    glColor3ub(38, 56, 222)
    glVertex2f(238,200)
    glVertex2f(238,196)
    glVertex2f(254,196)
    glVertex2f(254,200)
    glEnd()

def kotak13():
    glBegin(GL_LINE_LOOP)
    glColor3ub(2, 166, 166)
    glVertex2f(0,320)
    glVertex2f(400,320)
    glVertex2f(400,340)
    glVertex2f(0,340)
    glEnd()

def kotak14():
    glBegin(GL_LINE_LOOP)
    glColor3ub(2, 166, 166)
    glVertex2f(0,140)
    glVertex2f(0,120)
    glVertex2f(400,120)
    glVertex2f(400,140)
    glEnd()

def play():
    glBegin(GL_TRIANGLES)
    glColor3ub(200, 0, 0)
    glVertex2f(180,100)
    glVertex2f(180,60)
    glVertex2f(220,80)
    glEnd() 

def makanan():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(328.5,278.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def karakter():
    glBegin(GL_POLYGON)
    glColor3ub(247, 240, 12)
    glVertex2f(200.23179,204.91379)
    glVertex2f(204.38224,202.59345)
    glVertex2f(204,202)
    glVertex2f(203.50933,201.38194)
    glVertex2f(202.88346,200.88912)
    glVertex2f(202.19172,200.51951)
    glVertex2f(201.58233,200.25257)
    glVertex2f(201.00588,200.15257)
    glVertex2f(200.39649,200.1115)
    glVertex2f(199.70999,200.12096)
    glVertex2f(198.75542,200.33098)
    glVertex2f(198.02547,200.667)
    glVertex2f(197.39658,201.01703)
    glVertex2f(196.70031,201.68909)
    glVertex2f(196.29194,202.3147)
    glVertex2f(195.87694,202.86345)
    glVertex2f(195.638,203.58467)
    glVertex2f(195.51225,204.47836)
    glVertex2f(195.4871,205.38773)
    glVertex2f(195.56255,206.01488)
    glVertex2f(195.77634,206.67338)
    glVertex2f(196.12846,207.33189)
    glVertex2f(196.5183,207.92768)
    glVertex2f(197.05906,208.57051)
    glVertex2f(197.70041,209.04087)
    glVertex2f(198.48011,209.44852)
    glVertex2f(199.10889,209.69938)
    glVertex2f(199.7754,209.80913)
    glVertex2f(200.49221,209.84048)
    glVertex2f(201.13357,209.74641)
    glVertex2f(201.74978,209.57395)
    glVertex2f(202.37856,209.29173)
    glVertex2f(203,209)
    glVertex2f(203.64871,208.35101)
    glVertex2f(204,208)
    glVertex2f(204.32779,207.37892)
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
    hurufS()
    hurufN()
    hurufA()
    kotakA()
    hurufK()
    hurufE()
    hurufM()
    hurufA2()
    kotakA2()
    hurufN2()
    labirin()
    labirin2()
    labirin3()
    labirin4()
    kotak()
    kotak2()
    kotak3()
    kotak4()
    kotak5()
    kotak6()
    kotak7()
    kotak8()
    kotak9()
    kotak10()
    kotak11()
    kotak12()
    kotak13()
    kotak14()
    karakter()
    makanan()
    play()
    glutSwapBuffers()

glutInit(sys.argv)  # inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) # mengatur layar supaya berwarna
glutInitWindowSize(600, 600) # mengatur ukuran layar/window
glutInitWindowPosition(750, 0) # mangatur posisi window
glutCreateWindow("Snake Man") # untuk memberi nama window
glutDisplayFunc(showScreen) # untuk menampilkan objek pada layar
glutIdleFunc(showScreen) # untuk menuruh opengl untuk selalu menampilkan dan membuka objek
glutMainLoop() #untuk memulai segalanya