#Boa:Frame:Frame1

import wx,MySQLdb,datetime,os,locale,time
import wx.grid
import select
import socket
from threading import Thread
from wx.lib.pubsub import Publisher

netdb = ["",""]
netcl = ["",""]


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_CON, wxID_FRAME1BTN_MES, wxID_FRAME1BTN_START, 
 wxID_FRAME1GRID1, wxID_FRAME1MIP, wxID_FRAME1NOTEBOOK1, wxID_FRAME1NOTEBOOK2, 
 wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, 
 wxID_FRAME1PV_CL, wxID_FRAME1PV_IP, wxID_FRAME1PV_PORT, wxID_FRAME1PV_SV, 
 wxID_FRAME1RB_PRIV, wxID_FRAME1RB_PUB, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICBOX2, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1TX_DNS, wxID_FRAME1TX_MES, 
 wxID_FRAME1TX_NICK, wxID_FRAME1TX_PORT, 
] = [wx.NewId() for _init_ctrls in range(30)]



class IPCThread(Thread):
    def __init__(self):
        """Initialize"""
        Thread.__init__(self)
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.socket.bind((netdb[0], int(netdb[1])))
        self.socket.listen(5)
        self.setDaemon(True)
        self.start()
        
    def run(self):
        
        while True:
            try:
                client, addr = self.socket.accept()
                
                ready = select.select([client,],[],[],2)
                if ready[0]:
                    received = client.recv(4096)
                    print received
                    wx.CallAfter(Publisher().sendMessage,"update", received)
            except socket.error, msg:
                print "Socket error! %s" % msg
                break
        
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        
        except:
            pass
        
        self.socket.close()
        
        
        
[wxID_FRAME1TIMER1] = [wx.NewId() for _init_utils in range(1)]

class Frame1(wx.Frame):
    def _init_utils(self):
        # generated method, don't edit
        self.timer1 = wx.Timer(id=wxID_FRAME1TIMER1, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimer1Timer, id=wxID_FRAME1TIMER1)


    def _init_coll_notebook2_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel3, select=True,
              text='Network')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text='Setting')
        parent.AddPage(imageId=-1, page=self.panel4, select=False, text='My IP')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(673, 161), size=wx.Size(438, 631),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self._init_utils()
        self.SetClientSize(wx.Size(422, 593))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(8, 32), size=wx.Size(422, 593),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(46, 46, 46))

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self.panel1, pos=wx.Point(24, 16), size=wx.Size(376, 112),
              style=wx.RAISED_BORDER)

        self.rb_pub = wx.RadioButton(id=wxID_FRAME1RB_PUB, label='Public Chat',
              name='rb_pub', parent=self.notebook1, pos=wx.Point(80, 80),
              size=wx.Size(81, 13), style=0)
        self.rb_pub.SetValue(True)
        self.rb_pub.Bind(wx.EVT_RADIOBUTTON, self.OnRb_pubRadiobutton,
              id=wxID_FRAME1RB_PUB)

        self.rb_priv = wx.RadioButton(id=wxID_FRAME1RB_PRIV,
              label='Privat Chat', name='rb_priv', parent=self.notebook1,
              pos=wx.Point(240, 80), size=wx.Size(81, 13), style=0)
        self.rb_priv.SetValue(True)
        self.rb_priv.Bind(wx.EVT_RADIOBUTTON, self.OnRb_privRadiobutton,
              id=wxID_FRAME1RB_PRIV)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Raflesia Chat', name='staticText1', parent=self.notebook1,
              pos=wx.Point(96, 16), size=wx.Size(192, 35), style=0)
        self.staticText1.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD, True,
              'Tahoma'))
        self.staticText1.SetForegroundColour(wx.Colour(237, 24, 78))

        self.notebook2 = wx.Notebook(id=wxID_FRAME1NOTEBOOK2, name='notebook2',
              parent=self.panel1, pos=wx.Point(24, 144), size=wx.Size(376, 144),
              style=0)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook2, pos=wx.Point(0, 0), size=wx.Size(368, 118),
              style=wx.TAB_TRAVERSAL)

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook2, pos=wx.Point(0, 0), size=wx.Size(368, 118),
              style=wx.TAB_TRAVERSAL)

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook2, pos=wx.Point(0, 0), size=wx.Size(368, 118),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='Join Chat', name='staticBox1', parent=self.panel3,
              pos=wx.Point(16, 8), size=wx.Size(336, 100), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Insert IP Address/ DNS SERVER', name='staticText2',
              parent=self.panel3, pos=wx.Point(40, 32), size=wx.Size(153, 13),
              style=0)

        self.tx_dns = wx.TextCtrl(id=wxID_FRAME1TX_DNS, name='tx_dns',
              parent=self.panel3, pos=wx.Point(40, 48), size=wx.Size(184, 21),
              style=0, value='localhost')

        self.btn_con = wx.Button(id=wxID_FRAME1BTN_CON, label='Connect',
              name='btn_con', parent=self.panel3, pos=wx.Point(40, 80),
              size=wx.Size(75, 23), style=0)
        self.btn_con.Bind(wx.EVT_BUTTON, self.OnBtn_conButton,
              id=wxID_FRAME1BTN_CON)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Port', name='staticText3', parent=self.panel3,
              pos=wx.Point(256, 32), size=wx.Size(21, 13), style=0)

        self.tx_port = wx.TextCtrl(id=wxID_FRAME1TX_PORT, name='tx_port',
              parent=self.panel3, pos=wx.Point(256, 48), size=wx.Size(64, 21),
              style=0, value='')

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label='Server Privat Chat', name='staticBox2', parent=self.panel2,
              pos=wx.Point(24, 8), size=wx.Size(320, 80), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='My IP', name='staticText4', parent=self.panel2,
              pos=wx.Point(32, 28), size=wx.Size(28, 13), style=0)

        self.pv_ip = wx.TextCtrl(id=wxID_FRAME1PV_IP, name='pv_ip',
              parent=self.panel2, pos=wx.Point(64, 24), size=wx.Size(144, 21),
              style=0, value='')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='Port', name='staticText5', parent=self.panel2,
              pos=wx.Point(248, 28), size=wx.Size(21, 13), style=0)

        self.pv_port = wx.TextCtrl(id=wxID_FRAME1PV_PORT, name='pv_port',
              parent=self.panel2, pos=wx.Point(272, 24), size=wx.Size(56, 21),
              style=0, value='')

        self.btn_start = wx.Button(id=wxID_FRAME1BTN_START,
              label='Start Server Privat', name='btn_start', parent=self.panel2,
              pos=wx.Point(136, 56), size=wx.Size(104, 24), style=0)
        self.btn_start.Bind(wx.EVT_BUTTON, self.OnBtn_startButton,
              id=wxID_FRAME1BTN_START)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label='My Nickname', name='staticText6', parent=self.panel2,
              pos=wx.Point(48, 96), size=wx.Size(63, 13), style=0)

        self.tx_nick = wx.TextCtrl(id=wxID_FRAME1TX_NICK, name='tx_nick',
              parent=self.panel2, pos=wx.Point(128, 96), size=wx.Size(184, 18),
              style=0, value='Nick 1')

        self.pv_sv = wx.RadioButton(id=wxID_FRAME1PV_SV, label='Server',
              name='pv_sv', parent=self.panel2, pos=wx.Point(32, 120),
              size=wx.Size(81, 13), style=0)
        self.pv_sv.SetValue(True)
        self.pv_sv.Show(False)

        self.pv_cl = wx.RadioButton(id=wxID_FRAME1PV_CL, label='Client',
              name='pv_cl', parent=self.panel2, pos=wx.Point(176, 120),
              size=wx.Size(81, 13), style=0)
        self.pv_cl.SetValue(True)
        self.pv_cl.Show(False)

        self.mip = wx.StaticText(id=wxID_FRAME1MIP, label='My IP', name='mip',
              parent=self.panel4, pos=wx.Point(64, 40), size=wx.Size(55, 18),
              style=0)
        self.mip.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Terminal'))

        self.grid1 = wx.grid.Grid(id=wxID_FRAME1GRID1, name='grid1',
              parent=self.panel1, pos=wx.Point(24, 304), size=wx.Size(376, 232),
              style=0)

        self.tx_mes = wx.TextCtrl(id=wxID_FRAME1TX_MES, name='tx_mes',
              parent=self.panel1, pos=wx.Point(24, 544), size=wx.Size(256, 32),
              style=wx.TE_MULTILINE, value='')

        self.btn_mes = wx.Button(id=wxID_FRAME1BTN_MES, label='Send Message >>',
              name='btn_mes', parent=self.panel1, pos=wx.Point(296, 544),
              size=wx.Size(104, 31), style=0)
        self.btn_mes.Bind(wx.EVT_BUTTON, self.OnBtn_mesButton,
              id=wxID_FRAME1BTN_MES)

        self._init_coll_notebook2_Pages(self.notebook2)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.grid1.CreateGrid(0,3)
        self.grid1.SetRowLabelSize(0)
        self.grid1.SetColLabelSize(0)
        self.grid1.SetColSize(0, 100);
        self.grid1.SetColSize(1, 190);
        self.grid1.SetColSize(2, 120);
        
        Publisher().subscribe(self.updateDisplay, "update")
        
        self.grid1.editor = wx.grid.GridCellAutoWrapStringEditor()
        self.grid1.SetDefaultEditor(self.grid1.editor)
        self.grid1.SetDefaultRenderer(wx.grid.GridCellAutoWrapStringRenderer())
        
        self.rb_pub.SetValue(True)
        self.pv_cl.Show(False)
        self.pv_sv.Show(False)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        hbox.Add((0,0), proportion = 0, flag=wx.EXPAND)
        vbox.Add(self.notebook1, proportion = 0 , flag=wx.CENTER | wx.ALL, border=5)
        vbox.Add(self.notebook2, proportion = 0 , flag=wx.CENTER | wx.ALL, border=5)
        hbox.Add(self.grid1, proportion = 1, flag=wx.EXPAND | wx.ALL, border=8)
        vbox.Add(hbox, proportion = 2, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.tx_mes, proportion = 0, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.btn_mes, proportion = 0, flag = wx.RIGHT | wx.ALL, border=5)
        self.panel1.SetSizer(vbox)
        vbox.SetSizeHints(self)
        
        try:
            local_ip_address = ((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP Found"])[0])   
            mip = "My IP >>>>" + str(local_ip_address)
            
            self.mip.SetLabel("MyIP:"+str(local_ip_address))
            self.pv_ip.SetValue(local_ip_address)
            
            
        except:
            
            mip = "My IP >>>>  Localhost 127.0.0.1"
            self.mip.SetLabel(mip)
            
    def updateDisplay(self, msg):
        
        now = datetime.datetime.now()
        waktu = now.strftime("%d-%m-%Y %H:%M:%S")
        nick  = self.tx_nick.GetValue()
        mes   = msg.data.split("|")
        a  = self.grid1.GetNumberRows()
        
        self.grid1.InsertRows(a,1)
        self.grid1.SetReadOnly(a,0,True)
        self.grid1.SetReadOnly(a,1,True)
        self.grid1.SetReadOnly(a,2,True)
        try:
            self.grid1.SetCellValue(a,0  , str(mes[0]))
            self.grid1.SetCellValue(a,1  , str(mes[1]))
            self.grid1.SetCellValue(a,2  , str(waktu))
        except:
            self.grid1.SetCellValue(a,0  , str("Reply"))
            self.grid1.SetCellValue(a,1  , str(msg.data))
            self.grid1.SetCellValue(a,2  , str(waktu))
             
            
             

    def OnRb_pubRadiobutton(self, event):
        self.tx_port.Show(False)
        
    def OnRb_privRadiobutton(self, event):
        self.tx_port.Show(True)
        

    def OnBtn_conButton(self, event):
        dns = self.tx_dns.GetValue()
        prt = self.tx_port.GetValue()
        if self.rb_pub.GetValue() == True:
            try:
                conn = MySQLdb.connect(host=dns, user='root',passwd='Satellite1',db='raf_chat')
                cur  = conn.cursor()
                self.pesan = wx.MessageDialog(self,"Connected Succesfully!!", "INFO",wx.OK)
                self.pesan.ShowModal()
                self.tampil()
                self.timer1.Start(5000)
                conn.close()
            except:
                self.pesan = wx.MessageDialog(self,"Connection Fail!!", "INFO",wx.ICON_ERROR)
                self.pesan.ShowModal()
                self.timer1.Stop()
        elif self.rb_priv.GetValue() == True:
            #if self.pv_sv.GetValue() == True:
            netcl[0] = dns
            netcl[1] = prt
            #print netcl[0] , netcl[1]
            message = "Chat Joined"
            nick = self.tx_nick.GetValue()
            try:
                client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                client.connect((netcl[0], int(netcl[1])))
                client.send(nick+"|"+message)
                client.shutdown(socket.SHUT_RDWR)
                client.close()
                self.tx_mes.SetValue("")
                self.tx_mes.SetFocus()
                self.pesan = wx.MessageDialog(self,"Privat Chat Connected Succesfully", "INFO",wx.OK)
                self.pesan.ShowModal()
            except Exception, msg:
                print msg
                self.pesan = wx.MessageDialog(self,str(msg), "INFO",wx.ICON_ERROR)
                self.pesan.ShowModal()
                    
            #elif self.pv_cl.GetValue() == True:
            #    self.pesan = wx.MessageDialog(self,"Privat Chat Client Running Succesfully", "INFO",wx.OK)
            #    self.pesan.ShowModal()
                
    def tampil(self):
        q = self.grid1.GetNumberRows()
        ka = 0
        dns = self.tx_dns.GetValue()
        conn = MySQLdb.connect(host=dns, user='root', passwd='Satellite1', db='raf_chat')
        cur  = conn.cursor()
        sql  = "select * from publik order by id desc"
        cur.execute(sql)
        hasil = cur.fetchall()
        bat = int(len(hasil)) - int(q)
        bat1= 0
        if int(len(hasil)) != int(q) :
            if cur.rowcount > 0 :
                bat1 = 0
                for k in hasil:
                    if bat1 == bat :
                        break
                    else:
                        a = self.grid1.GetNumberRows()
                        self.grid1.InsertRows(a,1)
                        self.grid1.SetReadOnly(a,0,True)
                        self.grid1.SetReadOnly(a,1,True)
                        self.grid1.SetReadOnly(a,2,True)
                        bat1 = bat1 + 1
            if cur.rowcount > 0 :
                bat1 = 0
                for i in hasil:
                    if bat1 == bat :
                        break
                    else:
                        self.grid1.SetCellValue(ka,0 ,str(i[1]))
                        self.grid1.SetCellValue(ka,1 ,str(i[2]))
                        self.grid1.SetCellValue(ka,2 ,str(i[3]))
                        ka = ka + 1
        elif int(len(hasil)) == int(q) :
            a =0
        conn.close()
    def OnBtn_startButton(self, event):
        dns = self.pv_ip.GetValue()
        prt = self.pv_port.GetValue()
        netdb[0] = dns
        netdb[1] = prt
        
        self.ipc = IPCThread()
        self.pesan = wx.MessageDialog(self,"Privat Chat Server Running Succesfully", "INFO", wx.OK)
        self.pesan.ShowModal()
        

    def OnBtn_mesButton(self, event):
        if self.rb_pub.GetValue() == True:
            try:
                dns = self.tx_dns.GetValue()
                conn = MySQLdb.connect(host=dns, user='root',passwd='Satellite1',db='raf_chat')
                cur = conn.cursor()
                
                message = self.tx_mes.GetValue()
                now = datetime.datetime.now()
                waktu = now.strftime("%d-%m-%Y %H:%M:%S")
                nick = self.tx_nick.GetValue()
                
                if self.rb_pub.GetValue() == True:
                    conn = MySQLdb.connect(host=dns, user='root',passwd='Satellite1',db='raf_chat')
                    cur = conn.cursor()
                    sql = "insert into publik (nickname,pesan,waktu)values('%s','%s','%s')"\
                        %(nick,message,str(waktu))
                    cur.execute(sql)
                    conn.commit()
                    conn.close()
                    self.tx_mes.SetValue("")
                    self.tampil()
                    self.tx_mes.SetFocus()
                elif self.rb_priv.GetValue() == True():
                    a=0
                conn.close()
            except:
                self.timer1.Stop()
        elif self.rb_priv.GetValue() == True:
            #if self.pv_sv.GetValue() == True:
            message = self.tx_mes.GetValue()
            nick = self.tx_nick.GetValue()
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((netcl[0], int(netcl[1])))
                client.send(nick+"|"+message)
                client.shutdown(socket.SHUT_RDWR)
                client.close()
                        
                now = datetime.datetime.now()
                waktu = now.strftime("%d-%m-%Y %H:%M:%S")
                nick  = self.tx_nick.GetValue()
                
                a     = self.grid1.GetNumberRows()
                
                self.grid1.InsertRows(a, 1)
                self.grid1.SetReadOnly(a,0,True)
                self.grid1.SetReadOnly(a,1,True)
                self.grid1.SetReadOnly(a,2,True)
                
                self.grid1.SetCellValue(a,0 , str(nick))
                self.grid1.SetCellValue(a,1 , str(message))
                self.grid1.SetCellValue(a,2 , str(waktu))        
                
                self.tx_mes.SetValue("")
                self.tx_mes.SetFocus()
                
            except Exception, msg:
                print msg
                
                now = datetime.datetime.now()
                waktu = now.strftime("%d-%m-%Y %H:%M:%S")
                nick = self.tx_nick.GetValue()
                
                a = self.grid1.GetNumberRows()
                
                self.grid1.InsertRows()
                self.grid1.SetReadOnly(a,0,True)
                self.grid1.SetReadOnly(a,1,True)
                self.grid1.SetReadOnly(a,2,True)
                
                self.grid1.SetCellValue(a,0 ,str(nick))
                self.grid1.SetCellValue(a,1 ,str(message))
                self.grid1.SetCellValue(a,2 ,str(waktu))
                
                self.tx_mes.SetValue("")
                self.tx_mes.SetFocus()
                
    def OnTimer1Timer(self, event):
        try:
            q = self.grid1.GetNumberRows()
            ka = 0 
            dns = self.tx_dns.GetValue()
            conn = MySQLdb.connect(host=dns,user='root',passwd='Satellite1', db='raf_chat')
            cur = conn.cursor()
            sql = "select * from publik order by id desc"
            cur.execute(sql)
            hasil = cur.fetchall()
            bat = int(len(hasil)) - int(q)
            bat1 = 0
            print int(len(hasil)), int(q)
            if int(len(hasil)) != int(q):
                if cur.rowcount > 0 :
                    bat1 = 0
                    for k in hasil:
                        if bat1 == bat :
                            break
                        else:
                            a = self.grid1.GetNumberRows()
                            self.grid1.InsertRows(a,1)
                            self.grid1.SetReadOnly(a,0,True)
                            self.grid1.SetReadOnly(a,1,True)
                            self.grid1.SetReadOnly(a,2,True)
                            bat1 = bat1 + 1
                
                if cur.rowcount > 0 :
                    bat1 = 0 
                    for i in hasil:
                        if bat1 == bat :
                            break
                        else:
                            self.grid1.SetCellValue(ka,0 ,str(i[1]))
                            self.grid1.SetCellValue(ka,1 ,str(i[2]))
                            self.grid1.SetCellValue(ka,2 ,str(i[3]))
                            ka = ka + 1
            elif int(len(hasil)) == int(q) :
                a = 0
            
            conn.close()
        except:
            self.timer1.Stop()
            
                            
            
                    
