from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(990, 592)
        Dialog.setStyleSheet("setbase color rgb(252, 175, 62)")
        self.H = QtWidgets.QPushButton(parent=Dialog)
        self.H.setGeometry(QtCore.QRect(50, 50, 51, 51))
        self.H.setObjectName("H")
        self.Li = QtWidgets.QPushButton(parent=Dialog)
        self.Li.setGeometry(QtCore.QRect(50, 100, 51, 51))
        self.Li.setObjectName("Li")
        self.Na = QtWidgets.QPushButton(parent=Dialog)
        self.Na.setGeometry(QtCore.QRect(50, 150, 51, 51))
        self.Na.setObjectName("Na")
        self.K = QtWidgets.QPushButton(parent=Dialog)
        self.K.setGeometry(QtCore.QRect(50, 200, 51, 51))
        self.K.setObjectName("K")
        self.Rb = QtWidgets.QPushButton(parent=Dialog)
        self.Rb.setGeometry(QtCore.QRect(50, 250, 51, 51))
        self.Rb.setObjectName("Rb")
        self.Cs = QtWidgets.QPushButton(parent=Dialog)
        self.Cs.setGeometry(QtCore.QRect(50, 300, 51, 51))
        self.Cs.setObjectName("Cs")
        self.Fr = QtWidgets.QPushButton(parent=Dialog)
        self.Fr.setGeometry(QtCore.QRect(50, 350, 51, 51))
        self.Fr.setObjectName("Fr")
        self.Mg = QtWidgets.QPushButton(parent=Dialog)
        self.Mg.setGeometry(QtCore.QRect(100, 150, 51, 51))
        self.Mg.setObjectName("Mg")
        self.Sr = QtWidgets.QPushButton(parent=Dialog)
        self.Sr.setGeometry(QtCore.QRect(100, 250, 51, 51))
        self.Sr.setObjectName("Sr")
        self.Ra = QtWidgets.QPushButton(parent=Dialog)
        self.Ra.setGeometry(QtCore.QRect(100, 350, 51, 51))
        self.Ra.setObjectName("Ra")
        self.Ba = QtWidgets.QPushButton(parent=Dialog)
        self.Ba.setGeometry(QtCore.QRect(100, 300, 51, 51))
        self.Ba.setObjectName("Ba")
        self.Ca = QtWidgets.QPushButton(parent=Dialog)
        self.Ca.setGeometry(QtCore.QRect(100, 200, 51, 51))
        self.Ca.setObjectName("Ca")
        self.Be = QtWidgets.QPushButton(parent=Dialog)
        self.Be.setGeometry(QtCore.QRect(100, 100, 51, 51))
        self.Be.setObjectName("Be")
        self.Sc = QtWidgets.QPushButton(parent=Dialog)
        self.Sc.setGeometry(QtCore.QRect(150, 200, 51, 51))
        self.Sc.setObjectName("Sc")
        self.H_18 = QtWidgets.QPushButton(parent=Dialog)
        self.H_18.setGeometry(QtCore.QRect(150, 300, 51, 51))
        self.H_18.setText("")
        self.H_18.setObjectName("H_18")
        self.Y = QtWidgets.QPushButton(parent=Dialog)
        self.Y.setGeometry(QtCore.QRect(150, 250, 51, 51))
        self.Y.setObjectName("Y")
        self.H_21 = QtWidgets.QPushButton(parent=Dialog)
        self.H_21.setGeometry(QtCore.QRect(150, 350, 51, 51))
        self.H_21.setText("")
        self.H_21.setObjectName("H_21")
        self.Ti = QtWidgets.QPushButton(parent=Dialog)
        self.Ti.setGeometry(QtCore.QRect(200, 200, 51, 51))
        self.Ti.setObjectName("Ti")
        self.Hf = QtWidgets.QPushButton(parent=Dialog)
        self.Hf.setGeometry(QtCore.QRect(200, 300, 51, 51))
        self.Hf.setObjectName("Hf")
        self.Zr = QtWidgets.QPushButton(parent=Dialog)
        self.Zr.setGeometry(QtCore.QRect(200, 250, 51, 51))
        self.Zr.setObjectName("Zr")
        self.Rf = QtWidgets.QPushButton(parent=Dialog)
        self.Rf.setGeometry(QtCore.QRect(200, 350, 51, 51))
        self.Rf.setObjectName("Rf")
        self.V = QtWidgets.QPushButton(parent=Dialog)
        self.V.setGeometry(QtCore.QRect(250, 200, 51, 51))
        self.V.setObjectName("V")
        self.Ta = QtWidgets.QPushButton(parent=Dialog)
        self.Ta.setGeometry(QtCore.QRect(250, 300, 51, 51))
        self.Ta.setObjectName("Ta")
        self.Nb = QtWidgets.QPushButton(parent=Dialog)
        self.Nb.setGeometry(QtCore.QRect(250, 250, 51, 51))
        self.Nb.setObjectName("Nb")
        self.Db = QtWidgets.QPushButton(parent=Dialog)
        self.Db.setGeometry(QtCore.QRect(250, 350, 51, 51))
        self.Db.setObjectName("Db")
        self.Cr = QtWidgets.QPushButton(parent=Dialog)
        self.Cr.setGeometry(QtCore.QRect(300, 200, 51, 51))
        self.Cr.setObjectName("Cr")
        self.W = QtWidgets.QPushButton(parent=Dialog)
        self.W.setGeometry(QtCore.QRect(300, 300, 51, 51))
        self.W.setObjectName("W")
        self.Mo = QtWidgets.QPushButton(parent=Dialog)
        self.Mo.setGeometry(QtCore.QRect(300, 250, 51, 51))
        self.Mo.setObjectName("Mo")
        self.Sg = QtWidgets.QPushButton(parent=Dialog)
        self.Sg.setGeometry(QtCore.QRect(300, 350, 51, 51))
        self.Sg.setObjectName("Sg")
        self.Mn = QtWidgets.QPushButton(parent=Dialog)
        self.Mn.setGeometry(QtCore.QRect(350, 200, 51, 51))
        self.Mn.setObjectName("Mn")
        self.Re = QtWidgets.QPushButton(parent=Dialog)
        self.Re.setGeometry(QtCore.QRect(350, 300, 51, 51))
        self.Re.setObjectName("Re")
        self.Tc = QtWidgets.QPushButton(parent=Dialog)
        self.Tc.setGeometry(QtCore.QRect(350, 250, 51, 51))
        self.Tc.setObjectName("Tc")
        self.Bh = QtWidgets.QPushButton(parent=Dialog)
        self.Bh.setGeometry(QtCore.QRect(350, 350, 51, 51))
        self.Bh.setObjectName("Bh")
        self.Fe = QtWidgets.QPushButton(parent=Dialog)
        self.Fe.setGeometry(QtCore.QRect(400, 200, 51, 51))
        self.Fe.setObjectName("Fe")
        self.Os = QtWidgets.QPushButton(parent=Dialog)
        self.Os.setGeometry(QtCore.QRect(400, 300, 51, 51))
        self.Os.setObjectName("Os")
        self.Ru = QtWidgets.QPushButton(parent=Dialog)
        self.Ru.setGeometry(QtCore.QRect(400, 250, 51, 51))
        self.Ru.setObjectName("Ru")
        self.Hs = QtWidgets.QPushButton(parent=Dialog)
        self.Hs.setGeometry(QtCore.QRect(400, 350, 51, 51))
        self.Hs.setObjectName("Hs")
        self.Co = QtWidgets.QPushButton(parent=Dialog)
        self.Co.setGeometry(QtCore.QRect(450, 200, 51, 51))
        self.Co.setObjectName("Co")
        self.Ir = QtWidgets.QPushButton(parent=Dialog)
        self.Ir.setGeometry(QtCore.QRect(450, 300, 51, 51))
        self.Ir.setObjectName("Ir")
        self.Rh = QtWidgets.QPushButton(parent=Dialog)
        self.Rh.setGeometry(QtCore.QRect(450, 250, 51, 51))
        self.Rh.setObjectName("Rh")
        self.Mt = QtWidgets.QPushButton(parent=Dialog)
        self.Mt.setGeometry(QtCore.QRect(450, 350, 51, 51))
        self.Mt.setObjectName("Mt")
        self.Ni = QtWidgets.QPushButton(parent=Dialog)
        self.Ni.setGeometry(QtCore.QRect(500, 200, 51, 51))
        self.Ni.setObjectName("Ni")
        self.Pt = QtWidgets.QPushButton(parent=Dialog)
        self.Pt.setGeometry(QtCore.QRect(500, 300, 51, 51))
        self.Pt.setObjectName("Pt")
        self.Pd = QtWidgets.QPushButton(parent=Dialog)
        self.Pd.setGeometry(QtCore.QRect(500, 250, 51, 51))
        self.Pd.setObjectName("Pd")
        self.Ds = QtWidgets.QPushButton(parent=Dialog)
        self.Ds.setGeometry(QtCore.QRect(500, 350, 51, 51))
        self.Ds.setObjectName("Ds")
        self.Cu = QtWidgets.QPushButton(parent=Dialog)
        self.Cu.setGeometry(QtCore.QRect(550, 200, 51, 51))
        self.Cu.setObjectName("Cu")
        self.Au = QtWidgets.QPushButton(parent=Dialog)
        self.Au.setGeometry(QtCore.QRect(550, 300, 51, 51))
        self.Au.setObjectName("Au")
        self.Ag = QtWidgets.QPushButton(parent=Dialog)
        self.Ag.setGeometry(QtCore.QRect(550, 250, 51, 51))
        self.Ag.setObjectName("Ag")
        self.Rg = QtWidgets.QPushButton(parent=Dialog)
        self.Rg.setGeometry(QtCore.QRect(550, 350, 51, 51))
        self.Rg.setObjectName("Rg")
        self.Zn = QtWidgets.QPushButton(parent=Dialog)
        self.Zn.setGeometry(QtCore.QRect(600, 200, 51, 51))
        self.Zn.setObjectName("Zn")
        self.Hg = QtWidgets.QPushButton(parent=Dialog)
        self.Hg.setGeometry(QtCore.QRect(600, 300, 51, 51))
        self.Hg.setObjectName("Hg")
        self.Cd = QtWidgets.QPushButton(parent=Dialog)
        self.Cd.setGeometry(QtCore.QRect(600, 250, 51, 51))
        self.Cd.setObjectName("Cd")
        self.Cn = QtWidgets.QPushButton(parent=Dialog)
        self.Cn.setGeometry(QtCore.QRect(600, 350, 51, 51))
        self.Cn.setObjectName("Cn")
        self.Ga = QtWidgets.QPushButton(parent=Dialog)
        self.Ga.setGeometry(QtCore.QRect(650, 200, 51, 51))
        self.Ga.setObjectName("Ga")
        self.Al = QtWidgets.QPushButton(parent=Dialog)
        self.Al.setGeometry(QtCore.QRect(650, 150, 51, 51))
        self.Al.setObjectName("Al")
        self.Tl = QtWidgets.QPushButton(parent=Dialog)
        self.Tl.setGeometry(QtCore.QRect(650, 300, 51, 51))
        self.Tl.setObjectName("Tl")
        self.In = QtWidgets.QPushButton(parent=Dialog)
        self.In.setGeometry(QtCore.QRect(650, 250, 51, 51))
        self.In.setObjectName("In")
        self.Nh = QtWidgets.QPushButton(parent=Dialog)
        self.Nh.setGeometry(QtCore.QRect(650, 350, 51, 51))
        self.Nh.setObjectName("Nh")
        self.B = QtWidgets.QPushButton(parent=Dialog)
        self.B.setGeometry(QtCore.QRect(650, 100, 51, 51))
        self.B.setObjectName("B")
        self.Ge = QtWidgets.QPushButton(parent=Dialog)
        self.Ge.setGeometry(QtCore.QRect(700, 200, 51, 51))
        self.Ge.setObjectName("Ge")
        self.Si = QtWidgets.QPushButton(parent=Dialog)
        self.Si.setGeometry(QtCore.QRect(700, 150, 51, 51))
        self.Si.setObjectName("Si")
        self.Pb = QtWidgets.QPushButton(parent=Dialog)
        self.Pb.setGeometry(QtCore.QRect(700, 300, 51, 51))
        self.Pb.setObjectName("Pb")
        self.Sn = QtWidgets.QPushButton(parent=Dialog)
        self.Sn.setGeometry(QtCore.QRect(700, 250, 51, 51))
        self.Sn.setObjectName("Sn")
        self.Fl = QtWidgets.QPushButton(parent=Dialog)
        self.Fl.setGeometry(QtCore.QRect(700, 350, 51, 51))
        self.Fl.setObjectName("Fl")
        self.C = QtWidgets.QPushButton(parent=Dialog)
        self.C.setGeometry(QtCore.QRect(700, 100, 51, 51))
        self.C.setObjectName("C")
        self.As = QtWidgets.QPushButton(parent=Dialog)
        self.As.setGeometry(QtCore.QRect(750, 200, 51, 51))
        self.As.setObjectName("As")
        self.P = QtWidgets.QPushButton(parent=Dialog)
        self.P.setGeometry(QtCore.QRect(750, 150, 51, 51))
        self.P.setObjectName("P")
        self.Bi = QtWidgets.QPushButton(parent=Dialog)
        self.Bi.setGeometry(QtCore.QRect(750, 300, 51, 51))
        self.Bi.setObjectName("Bi")
        self.Sb = QtWidgets.QPushButton(parent=Dialog)
        self.Sb.setGeometry(QtCore.QRect(750, 250, 51, 51))
        self.Sb.setObjectName("Sb")
        self.Mc = QtWidgets.QPushButton(parent=Dialog)
        self.Mc.setGeometry(QtCore.QRect(750, 350, 51, 51))
        self.Mc.setObjectName("Mc")
        self.N = QtWidgets.QPushButton(parent=Dialog)
        self.N.setGeometry(QtCore.QRect(750, 100, 51, 51))
        self.N.setObjectName("N")
        self.Se = QtWidgets.QPushButton(parent=Dialog)
        self.Se.setGeometry(QtCore.QRect(800, 200, 51, 51))
        self.Se.setObjectName("Se")
        self.S = QtWidgets.QPushButton(parent=Dialog)
        self.S.setGeometry(QtCore.QRect(800, 150, 51, 51))
        self.S.setObjectName("S")
        self.Po = QtWidgets.QPushButton(parent=Dialog)
        self.Po.setGeometry(QtCore.QRect(800, 300, 51, 51))
        self.Po.setObjectName("Po")
        self.Te = QtWidgets.QPushButton(parent=Dialog)
        self.Te.setGeometry(QtCore.QRect(800, 250, 51, 51))
        self.Te.setObjectName("Te")
        self.Lv = QtWidgets.QPushButton(parent=Dialog)
        self.Lv.setGeometry(QtCore.QRect(800, 350, 51, 51))
        self.Lv.setObjectName("Lv")
        self.O = QtWidgets.QPushButton(parent=Dialog)
        self.O.setGeometry(QtCore.QRect(800, 100, 51, 51))
        self.O.setObjectName("O")
        self.Br = QtWidgets.QPushButton(parent=Dialog)
        self.Br.setGeometry(QtCore.QRect(850, 200, 51, 51))
        self.Br.setObjectName("Br")
        self.Cl = QtWidgets.QPushButton(parent=Dialog)
        self.Cl.setGeometry(QtCore.QRect(850, 150, 51, 51))
        self.Cl.setObjectName("Cl")
        self.At = QtWidgets.QPushButton(parent=Dialog)
        self.At.setGeometry(QtCore.QRect(850, 300, 51, 51))
        self.At.setObjectName("At")
        self.I = QtWidgets.QPushButton(parent=Dialog)
        self.I.setGeometry(QtCore.QRect(850, 250, 51, 51))
        self.I.setObjectName("I")
        self.Ts = QtWidgets.QPushButton(parent=Dialog)
        self.Ts.setGeometry(QtCore.QRect(850, 350, 51, 51))
        self.Ts.setObjectName("Ts")
        self.F = QtWidgets.QPushButton(parent=Dialog)
        self.F.setGeometry(QtCore.QRect(850, 100, 51, 51))
        self.F.setObjectName("F")
        self.Kr = QtWidgets.QPushButton(parent=Dialog)
        self.Kr.setGeometry(QtCore.QRect(900, 200, 51, 51))
        self.Kr.setObjectName("Kr")
        self.Ar = QtWidgets.QPushButton(parent=Dialog)
        self.Ar.setGeometry(QtCore.QRect(900, 150, 51, 51))
        self.Ar.setObjectName("Ar")
        self.Rn = QtWidgets.QPushButton(parent=Dialog)
        self.Rn.setGeometry(QtCore.QRect(900, 300, 51, 51))
        self.Rn.setObjectName("Rn")
        self.He = QtWidgets.QPushButton(parent=Dialog)
        self.He.setGeometry(QtCore.QRect(900, 50, 51, 51))
        self.He.setObjectName("He")
        self.Xe = QtWidgets.QPushButton(parent=Dialog)
        self.Xe.setGeometry(QtCore.QRect(900, 250, 51, 51))
        self.Xe.setObjectName("Xe")
        self.Og = QtWidgets.QPushButton(parent=Dialog)
        self.Og.setGeometry(QtCore.QRect(900, 350, 51, 51))
        self.Og.setObjectName("Og")
        self.Ne = QtWidgets.QPushButton(parent=Dialog)
        self.Ne.setGeometry(QtCore.QRect(900, 100, 51, 51))
        self.Ne.setObjectName("Ne")
        self.Ho = QtWidgets.QPushButton(parent=Dialog)
        self.Ho.setGeometry(QtCore.QRect(700, 450, 51, 51))
        self.Ho.setObjectName("Ho")
        self.Lu = QtWidgets.QPushButton(parent=Dialog)
        self.Lu.setGeometry(QtCore.QRect(900, 450, 51, 51))
        self.Lu.setObjectName("Lu")
        self.Pr = QtWidgets.QPushButton(parent=Dialog)
        self.Pr.setGeometry(QtCore.QRect(300, 450, 51, 51))
        self.Pr.setObjectName("Pr")
        self.Eu = QtWidgets.QPushButton(parent=Dialog)
        self.Eu.setGeometry(QtCore.QRect(500, 450, 51, 51))
        self.Eu.setObjectName("Eu")
        self.Gd = QtWidgets.QPushButton(parent=Dialog)
        self.Gd.setGeometry(QtCore.QRect(550, 450, 51, 51))
        self.Gd.setObjectName("Gd")
        self.Tb = QtWidgets.QPushButton(parent=Dialog)
        self.Tb.setGeometry(QtCore.QRect(600, 450, 51, 51))
        self.Tb.setObjectName("Tb")
        self.Ce = QtWidgets.QPushButton(parent=Dialog)
        self.Ce.setGeometry(QtCore.QRect(250, 450, 51, 51))
        self.Ce.setObjectName("Ce")
        self.Yb = QtWidgets.QPushButton(parent=Dialog)
        self.Yb.setGeometry(QtCore.QRect(850, 450, 51, 51))
        self.Yb.setObjectName("Yb")
        self.Pm = QtWidgets.QPushButton(parent=Dialog)
        self.Pm.setGeometry(QtCore.QRect(400, 450, 51, 51))
        self.Pm.setObjectName("Pm")
        self.Tm = QtWidgets.QPushButton(parent=Dialog)
        self.Tm.setGeometry(QtCore.QRect(800, 450, 51, 51))
        self.Tm.setObjectName("Tm")
        self.Er = QtWidgets.QPushButton(parent=Dialog)
        self.Er.setGeometry(QtCore.QRect(750, 450, 51, 51))
        self.Er.setObjectName("Er")
        self.La = QtWidgets.QPushButton(parent=Dialog)
        self.La.setGeometry(QtCore.QRect(200, 450, 51, 51))
        self.La.setObjectName("La")
        self.Dy = QtWidgets.QPushButton(parent=Dialog)
        self.Dy.setGeometry(QtCore.QRect(650, 450, 51, 51))
        self.Dy.setObjectName("Dy")
        self.Nd = QtWidgets.QPushButton(parent=Dialog)
        self.Nd.setGeometry(QtCore.QRect(350, 450, 51, 51))
        self.Nd.setObjectName("Nd")
        self.Sm = QtWidgets.QPushButton(parent=Dialog)
        self.Sm.setGeometry(QtCore.QRect(450, 450, 51, 51))
        self.Sm.setObjectName("Sm")
        self.Es = QtWidgets.QPushButton(parent=Dialog)
        self.Es.setGeometry(QtCore.QRect(700, 500, 51, 51))
        self.Es.setObjectName("Es")
        self.Lr = QtWidgets.QPushButton(parent=Dialog)
        self.Lr.setGeometry(QtCore.QRect(900, 500, 51, 51))
        self.Lr.setObjectName("Lr")
        self.Pa = QtWidgets.QPushButton(parent=Dialog)
        self.Pa.setGeometry(QtCore.QRect(300, 500, 51, 51))
        self.Pa.setObjectName("Pa")
        self.Am = QtWidgets.QPushButton(parent=Dialog)
        self.Am.setGeometry(QtCore.QRect(500, 500, 51, 51))
        self.Am.setObjectName("Am")
        self.Cm = QtWidgets.QPushButton(parent=Dialog)
        self.Cm.setGeometry(QtCore.QRect(550, 500, 51, 51))
        self.Cm.setObjectName("Cm")
        self.Bk = QtWidgets.QPushButton(parent=Dialog)
        self.Bk.setGeometry(QtCore.QRect(600, 500, 51, 51))
        self.Bk.setObjectName("Bk")
        self.Th = QtWidgets.QPushButton(parent=Dialog)
        self.Th.setGeometry(QtCore.QRect(250, 500, 51, 51))
        self.Th.setObjectName("Th")
        self.No = QtWidgets.QPushButton(parent=Dialog)
        self.No.setGeometry(QtCore.QRect(850, 500, 51, 51))
        self.No.setObjectName("No")
        self.Np = QtWidgets.QPushButton(parent=Dialog)
        self.Np.setGeometry(QtCore.QRect(400, 500, 51, 51))
        self.Np.setObjectName("Np")
        self.Md = QtWidgets.QPushButton(parent=Dialog)
        self.Md.setGeometry(QtCore.QRect(800, 500, 51, 51))
        self.Md.setObjectName("Md")
        self.Fm = QtWidgets.QPushButton(parent=Dialog)
        self.Fm.setGeometry(QtCore.QRect(750, 500, 51, 51))
        self.Fm.setObjectName("Fm")
        self.Ac = QtWidgets.QPushButton(parent=Dialog)
        self.Ac.setGeometry(QtCore.QRect(200, 500, 51, 51))
        self.Ac.setObjectName("Ac")
        self.Cf = QtWidgets.QPushButton(parent=Dialog)
        self.Cf.setGeometry(QtCore.QRect(650, 500, 51, 51))
        self.Cf.setObjectName("Cf")
        self.U = QtWidgets.QPushButton(parent=Dialog)
        self.U.setGeometry(QtCore.QRect(350, 500, 51, 51))
        self.U.setObjectName("U")
        self.Pu = QtWidgets.QPushButton(parent=Dialog)
        self.Pu.setGeometry(QtCore.QRect(450, 500, 51, 51))
        self.Pu.setObjectName("Pu")
        self.text = QtWidgets.QLabel(parent=Dialog)
        self.text.setGeometry(QtCore.QRect(50, 0, 51, 51))
        self.text.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text.setScaledContents(False)
        self.text.setWordWrap(False)
        self.text.setObjectName("text")
        self.text_2 = QtWidgets.QLabel(parent=Dialog)
        self.text_2.setGeometry(QtCore.QRect(100, 0, 51, 51))
        self.text_2.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_2.setScaledContents(False)
        self.text_2.setWordWrap(False)
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(parent=Dialog)
        self.text_3.setGeometry(QtCore.QRect(150, 0, 51, 51))
        self.text_3.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_3.setScaledContents(False)
        self.text_3.setWordWrap(False)
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(parent=Dialog)
        self.text_4.setGeometry(QtCore.QRect(200, 0, 51, 51))
        self.text_4.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_4.setScaledContents(False)
        self.text_4.setWordWrap(False)
        self.text_4.setObjectName("text_4")
        self.text_5 = QtWidgets.QLabel(parent=Dialog)
        self.text_5.setGeometry(QtCore.QRect(250, 0, 51, 51))
        self.text_5.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_5.setScaledContents(False)
        self.text_5.setWordWrap(False)
        self.text_5.setObjectName("text_5")
        self.text_6 = QtWidgets.QLabel(parent=Dialog)
        self.text_6.setGeometry(QtCore.QRect(300, 0, 51, 51))
        self.text_6.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_6.setScaledContents(False)
        self.text_6.setWordWrap(False)
        self.text_6.setObjectName("text_6")
        self.text_7 = QtWidgets.QLabel(parent=Dialog)
        self.text_7.setGeometry(QtCore.QRect(350, 0, 51, 51))
        self.text_7.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_7.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_7.setScaledContents(False)
        self.text_7.setWordWrap(False)
        self.text_7.setObjectName("text_7")
        self.text_8 = QtWidgets.QLabel(parent=Dialog)
        self.text_8.setGeometry(QtCore.QRect(400, 0, 51, 51))
        self.text_8.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_8.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_8.setScaledContents(False)
        self.text_8.setWordWrap(False)
        self.text_8.setObjectName("text_8")
        self.text_9 = QtWidgets.QLabel(parent=Dialog)
        self.text_9.setGeometry(QtCore.QRect(450, 0, 51, 51))
        self.text_9.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_9.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_9.setScaledContents(False)
        self.text_9.setWordWrap(False)
        self.text_9.setObjectName("text_9")
        self.text_10 = QtWidgets.QLabel(parent=Dialog)
        self.text_10.setGeometry(QtCore.QRect(500, 0, 51, 51))
        self.text_10.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_10.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_10.setScaledContents(False)
        self.text_10.setWordWrap(False)
        self.text_10.setObjectName("text_10")
        self.text_11 = QtWidgets.QLabel(parent=Dialog)
        self.text_11.setGeometry(QtCore.QRect(550, 0, 51, 51))
        self.text_11.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_11.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_11.setScaledContents(False)
        self.text_11.setWordWrap(False)
        self.text_11.setObjectName("text_11")
        self.text_12 = QtWidgets.QLabel(parent=Dialog)
        self.text_12.setGeometry(QtCore.QRect(600, 0, 51, 51))
        self.text_12.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_12.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_12.setScaledContents(False)
        self.text_12.setWordWrap(False)
        self.text_12.setObjectName("text_12")
        self.text_13 = QtWidgets.QLabel(parent=Dialog)
        self.text_13.setGeometry(QtCore.QRect(650, 0, 51, 51))
        self.text_13.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_13.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_13.setScaledContents(False)
        self.text_13.setWordWrap(False)
        self.text_13.setObjectName("text_13")
        self.text_14 = QtWidgets.QLabel(parent=Dialog)
        self.text_14.setGeometry(QtCore.QRect(700, 0, 51, 51))
        self.text_14.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_14.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_14.setScaledContents(False)
        self.text_14.setWordWrap(False)
        self.text_14.setObjectName("text_14")
        self.text_15 = QtWidgets.QLabel(parent=Dialog)
        self.text_15.setGeometry(QtCore.QRect(750, 0, 51, 51))
        self.text_15.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_15.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_15.setScaledContents(False)
        self.text_15.setWordWrap(False)
        self.text_15.setObjectName("text_15")
        self.text_16 = QtWidgets.QLabel(parent=Dialog)
        self.text_16.setGeometry(QtCore.QRect(800, 0, 51, 51))
        self.text_16.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_16.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_16.setScaledContents(False)
        self.text_16.setWordWrap(False)
        self.text_16.setObjectName("text_16")
        self.text_17 = QtWidgets.QLabel(parent=Dialog)
        self.text_17.setGeometry(QtCore.QRect(850, 0, 51, 51))
        self.text_17.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_17.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_17.setScaledContents(False)
        self.text_17.setWordWrap(False)
        self.text_17.setObjectName("text_17")
        self.text_18 = QtWidgets.QLabel(parent=Dialog)
        self.text_18.setGeometry(QtCore.QRect(900, 0, 51, 51))
        self.text_18.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_18.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_18.setScaledContents(False)
        self.text_18.setWordWrap(False)
        self.text_18.setObjectName("text_18")
        self.text_19 = QtWidgets.QLabel(parent=Dialog)
        self.text_19.setGeometry(QtCore.QRect(0, 50, 51, 51))
        self.text_19.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_19.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_19.setScaledContents(False)
        self.text_19.setWordWrap(False)
        self.text_19.setObjectName("text_19")
        self.text_20 = QtWidgets.QLabel(parent=Dialog)
        self.text_20.setGeometry(QtCore.QRect(0, 100, 51, 51))
        self.text_20.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_20.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_20.setScaledContents(False)
        self.text_20.setWordWrap(False)
        self.text_20.setObjectName("text_20")
        self.text_21 = QtWidgets.QLabel(parent=Dialog)
        self.text_21.setGeometry(QtCore.QRect(0, 150, 51, 51))
        self.text_21.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_21.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_21.setScaledContents(False)
        self.text_21.setWordWrap(False)
        self.text_21.setObjectName("text_21")
        self.text_22 = QtWidgets.QLabel(parent=Dialog)
        self.text_22.setGeometry(QtCore.QRect(0, 200, 51, 51))
        self.text_22.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_22.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_22.setScaledContents(False)
        self.text_22.setWordWrap(False)
        self.text_22.setObjectName("text_22")
        self.text_23 = QtWidgets.QLabel(parent=Dialog)
        self.text_23.setGeometry(QtCore.QRect(0, 250, 51, 51))
        self.text_23.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_23.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_23.setScaledContents(False)
        self.text_23.setWordWrap(False)
        self.text_23.setObjectName("text_23")
        self.text_24 = QtWidgets.QLabel(parent=Dialog)
        self.text_24.setGeometry(QtCore.QRect(0, 300, 51, 51))
        self.text_24.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_24.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_24.setScaledContents(False)
        self.text_24.setWordWrap(False)
        self.text_24.setObjectName("text_24")
        self.text_25 = QtWidgets.QLabel(parent=Dialog)
        self.text_25.setGeometry(QtCore.QRect(0, 350, 51, 51))
        self.text_25.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.text_25.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.text_25.setScaledContents(False)
        self.text_25.setWordWrap(False)
        self.text_25.setObjectName("text_25")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(153, 100, 490, 101))
        self.label.setObjectName("label")

        self.H.clicked.connect(self.H_def)
        self.He.clicked.connect(self.He_def)
        self.Li.clicked.connect(self.Li_def)
        self.Be.clicked.connect(self.Be_def)
        self.B.clicked.connect(self.B_def)
        self.C.clicked.connect(self.C_def)
        self.N.clicked.connect(self.N_def)
        self.O.clicked.connect(self.O_def)
        self.F.clicked.connect(self.F_def)
        self.Ne.clicked.connect(self.Ne_def)
        self.Na.clicked.connect(self.Na_def)
        self.Mg.clicked.connect(self.Mg_def)
        self.Al.clicked.connect(self.Al_def)
        self.Si.clicked.connect(self.Si_def)
        self.P.clicked.connect(self.P_def)
        self.S.clicked.connect(self.S_def)
        self.Cl.clicked.connect(self.Cl_def)
        self.Ar.clicked.connect(self.Ar_def)
        self.K.clicked.connect(self.K_def)
        self.Ca.clicked.connect(self.Ca_def)
        self.Sc.clicked.connect(self.Sc_def)
        self.Ti.clicked.connect(self.Ti_def)
        self.V.clicked.connect(self.V_def)
        self.Cr.clicked.connect(self.Cr_def)
        self.Mn.clicked.connect(self.Mn_def)
        self.Fe.clicked.connect(self.Fe_def)
        self.Co.clicked.connect(self.Co_def)
        self.Ni.clicked.connect(self.Ni_def)
        self.Cu.clicked.connect(self.Cu_def)
        self.Zn.clicked.connect(self.Zn_def)
        self.Ga.clicked.connect(self.Ga_def)
        self.Ge.clicked.connect(self.Ge_def)
        self.As.clicked.connect(self.As_def)
        self.Se.clicked.connect(self.Se_def)
        self.Br.clicked.connect(self.Br_def)
        self.Kr.clicked.connect(self.Kr_def)
        self.Rb.clicked.connect(self.Rb_def)
        self.Sr.clicked.connect(self.Sr_def)
        self.Y.clicked.connect(self.Y_def)
        self.Zr.clicked.connect(self.Zr_def)
        self.Nb.clicked.connect(self.Nb_def)
        self.Mo.clicked.connect(self.Mo_def)
        self.Tc.clicked.connect(self.Tc_def)
        self.Ru.clicked.connect(self.Ru_def)
        self.Rh.clicked.connect(self.Rh_def)
        self.Pd.clicked.connect(self.Pd_def)
        self.Ag.clicked.connect(self.Ag_def)
        self.Cd.clicked.connect(self.Cd_def)
        self.In.clicked.connect(self.In_def)
        self.Sn.clicked.connect(self.Sn_def)
        self.Sb.clicked.connect(self.Sb_def)
        self.Te.clicked.connect(self.Te_def)
        self.I.clicked.connect(self.I_def)
        self.Xe.clicked.connect(self.Xe_def)
        self.Cs.clicked.connect(self.Cs_def)
        self.Ba.clicked.connect(self.Ba_def)
        self.La.clicked.connect(self.La_def)
        self.Ce.clicked.connect(self.Ce_def)
        self.Pr.clicked.connect(self.Pr_def)
        self.Nd.clicked.connect(self.Nd_def)
        self.Pm.clicked.connect(self.Pm_def)
        self.Sm.clicked.connect(self.Sm_def)
        self.Eu.clicked.connect(self.Eu_def)
        self.Gd.clicked.connect(self.Gd_def)
        self.Tb.clicked.connect(self.Tb_def)
        self.Dy.clicked.connect(self.Dy_def)
        self.Ho.clicked.connect(self.Ho_def)
        self.Er.clicked.connect(self.Er_def)
        self.Tm.clicked.connect(self.Tm_def)
        self.Yb.clicked.connect(self.Yb_def)
        self.Lu.clicked.connect(self.Lu_def)
        self.Hf.clicked.connect(self.Hf_def)
        self.Ta.clicked.connect(self.Ta_def)
        self.W.clicked.connect(self.W_def)
        self.Re.clicked.connect(self.Re_def)
        self.Os.clicked.connect(self.Os_def)
        self.Ir.clicked.connect(self.Ir_def)
        self.Pt.clicked.connect(self.Pt_def)
        self.Au.clicked.connect(self.Au_def)
        self.Hg.clicked.connect(self.Hg_def)
        self.Tl.clicked.connect(self.Tl_def)
        self.Pb.clicked.connect(self.Pb_def)
        self.Bi.clicked.connect(self.Bi_def)
        self.Po.clicked.connect(self.Po_def)
        self.At.clicked.connect(self.At_def)
        self.Rn.clicked.connect(self.Rn_def)
        self.Fr.clicked.connect(self.Fr_def)
        self.Ra.clicked.connect(self.Ra_def)
        self.Ac.clicked.connect(self.Ac_def)
        self.Th.clicked.connect(self.Th_def)
        self.Pa.clicked.connect(self.Pa_def)
        self.U.clicked.connect(self.U_def)
        self.Np.clicked.connect(self.Np_def)
        self.Pu.clicked.connect(self.Pu_def)
        self.Am.clicked.connect(self.Am_def)
        self.Cm.clicked.connect(self.Cm_def)
        self.Bk.clicked.connect(self.Bk_def)
        self.Cf.clicked.connect(self.Cf_def)
        self.Es.clicked.connect(self.Es_def)
        self.Fm.clicked.connect(self.Fm_def)
        self.Md.clicked.connect(self.Md_def)
        self.No.clicked.connect(self.No_def)
        self.Lr.clicked.connect(self.Lr_def)
        self.Rf.clicked.connect(self.Rf_def)
        self.Db.clicked.connect(self.Db_def)
        self.Sg.clicked.connect(self.Sg_def)
        self.Bh.clicked.connect(self.Bh_def)
        self.Hs.clicked.connect(self.Hs_def)
        self.Mt.clicked.connect(self.Mt_def)
        self.Ds.clicked.connect(self.Ds_def)
        self.Rg.clicked.connect(self.Rg_def)
        self.Cn.clicked.connect(self.Cn_def)
        self.Nh.clicked.connect(self.Nh_def)
        self.Fl.clicked.connect(self.Fl_def)
        self.Mc.clicked.connect(self.Mc_def)
        self.Lv.clicked.connect(self.Lv_def)
        self.Ts.clicked.connect(self.Ts_def)
        self.Og.clicked.connect(self.Og_def)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def H_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('H', bd))
        print(self.H.text())

    def H_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('H', bd))
        print(self.H.text())

    def He_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('He', bd))
        print(self.He.text())

    def Li_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Li', bd))
        print(self.Li.text())

    def Be_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Be', bd))
        print(self.Be.text())

    def B_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('B', bd))
        print(self.B.text())

    def C_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('C', bd))
        print(self.C.text())

    def N_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('N', bd))
        print(self.N.text())

    def O_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('O', bd))
        print(self.O.text())

    def F_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('F', bd))
        print(self.F.text())

    def Ne_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ne', bd))
        print(self.Ne.text())

    def Na_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Na', bd))
        print(self.Na.text())

    def Mg_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Mg', bd))
        print(self.Mg.text())

    def Al_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Al', bd))
        print(self.Al.text())

    def Si_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Si', bd))
        print(self.Si.text())

    def P_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('P', bd))
        print(self.P.text())

    def S_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('S', bd))
        print(self.S.text())

    def Cl_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cl', bd))
        print(self.Cl.text())

    def Ar_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ar', bd))
        print(self.Ar.text())

    def K_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('K', bd))
        print(self.K.text())

    def Ca_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ca', bd))
        print(self.Ca.text())

    def Sc_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Sc', bd))
        print(self.Sc.text())

    def Ti_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ti', bd))
        print(self.Ti.text())

    def V_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('V', bd))
        print(self.V.text())

    def Cr_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cr', bd))
        print(self.Cr.text())

    def Mn_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Mn', bd))
        print(self.Mn.text())

    def Fe_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Fe', bd))
        print(self.Fe.text())

    def Co_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Co', bd))
        print(self.Co.text())

    def Ni_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ni', bd))
        print(self.Ni.text())

    def Cu_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cu', bd))
        print(self.Cu.text())

    def Zn_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Zn', bd))
        print(self.Zn.text())

    def Ga_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ga', bd))
        print(self.Ga.text())

    def Ge_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ge', bd))
        print(self.Ge.text())

    def As_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('As', bd))
        print(self.As.text())

    def Se_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Se', bd))
        print(self.Se.text())

    def Br_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Br', bd))
        print(self.Br.text())

    def Kr_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Kr', bd))
        print(self.Kr.text())

    def Rb_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Rb', bd))
        print(self.Rb.text())

    def Sr_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Sr', bd))
        print(self.Sr.text())

    def Y_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Y', bd))
        print(self.Y.text())

    def Zr_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Zr', bd))
        print(self.Zr.text())

    def Nb_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Nb', bd))
        print(self.Nb.text())

    def Mo_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Mo', bd))
        print(self.Mo.text())

    def Tc_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Tc', bd))
        print(self.Tc.text())

    def Ru_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ru', bd))
        print(self.Ru.text())

    def Rh_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Rh', bd))
        print(self.Rh.text())

    def Pd_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Pd', bd))
        print(self.Pd.text())

    def Ag_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ag', bd))
        print(self.Ag.text())

    def Cd_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cd', bd))
        print(self.Cd.text())

    def In_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('In', bd))
        print(self.In.text())

    def Sn_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Sn', bd))
        print(self.Sn.text())

    def Sb_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Sb', bd))
        print(self.Sb.text())

    def Te_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Te', bd))
        print(self.Te.text())

    def I_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('I', bd))
        print(self.I.text())

    def Xe_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Xe', bd))
        print(self.Xe.text())

    def Cs_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cs', bd))
        print(self.Cs.text())

    def Ba_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ba', bd))
        print(self.Ba.text())

    def La_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('La', bd))
        print(self.La.text())

    def Ce_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ce', bd))
        print(self.Ce.text())

    def Pr_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Pr', bd))
        print(self.Pr.text())

    def Nd_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Nd', bd))
        print(self.Nd.text())

    def Pm_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Pm', bd))
        print(self.Pm.text())

    def Sm_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Sm', bd))
        print(self.Sm.text())

    def Eu_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Eu', bd))
        print(self.Eu.text())

    def Gd_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Gd', bd))
        print(self.Gd.text())

    def Tb_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Tb', bd))
        print(self.Tb.text())

    def Dy_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Dy', bd))
        print(self.Dy.text())

    def Ho_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ho', bd))
        print(self.Ho.text())

    def Er_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Er', bd))
        print(self.Er.text())

    def Tm_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Tm', bd))
        print(self.Tm.text())

    def Yb_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Yb', bd))
        print(self.Yb.text())

    def Lu_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Lu', bd))
        print(self.Lu.text())

    def Hf_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Hf', bd))
        print(self.Hf.text())

    def Ta_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ta', bd))
        print(self.Ta.text())

    def W_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('W', bd))
        print(self.W.text())

    def Re_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Re', bd))
        print(self.Re.text())

    def Os_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Os', bd))
        print(self.Os.text())

    def Ir_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ir', bd))
        print(self.Ir.text())

    def Pt_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Pt', bd))
        print(self.Pt.text())

    def Au_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Au', bd))
        print(self.Au.text())

    def Hg_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Hg', bd))
        print(self.Hg.text())

    def Tl_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Tl', bd))
        print(self.Tl.text())

    def Pb_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Pb', bd))
        print(self.Pb.text())

    def Bi_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Bi', bd))
        print(self.Bi.text())

    def Po_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Po', bd))
        print(self.Po.text())

    def At_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('At', bd))
        print(self.At.text())

    def Rn_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Rn', bd))
        print(self.Rn.text())

    def Fr_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Fr', bd))
        print(self.Fr.text())

    def Ra_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ra', bd))
        print(self.Ra.text())

    def Ac_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ac', bd))
        print(self.Ac.text())

    def Th_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Th', bd))
        print(self.Th.text())

    def Pa_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Pa', bd))
        print(self.Pa.text())

    def U_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('U', bd))
        print(self.U.text())

    def Np_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Np', bd))
        print(self.Np.text())

    def Pu_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Pu', bd))
        print(self.Pu.text())

    def Am_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Am', bd))
        print(self.Am.text())

    def Cm_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cm', bd))
        print(self.Cm.text())

    def Bk_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Bk', bd))
        print(self.Bk.text())

    def Cf_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cf', bd))
        print(self.Cf.text())

    def Es_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Es', bd))
        print(self.Es.text())

    def Fm_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Fm', bd))
        print(self.Fm.text())

    def Md_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Md', bd))
        print(self.Md.text())

    def No_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('No', bd))
        print(self.No.text())

    def Lr_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Lr', bd))
        print(self.Lr.text())

    def Rf_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Rf', bd))
        print(self.Rf.text())

    def Db_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Db', bd))
        print(self.Db.text())

    def Sg_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Sg', bd))
        print(self.Sg.text())

    def Bh_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Bh', bd))
        print(self.Bh.text())

    def Hs_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Hs', bd))
        print(self.Hs.text())

    def Mt_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Mt', bd))
        print(self.Mt.text())

    def Ds_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ds', bd))
        print(self.Ds.text())

    def Rg_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Rg', bd))
        print(self.Rg.text())

    def Cn_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Cn', bd))
        print(self.Cn.text())

    def Nh_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Nh', bd))
        print(self.Nh.text())

    def Fl_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Fl', bd))
        print(self.Fl.text())

    def Mc_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Mc', bd))
        print(self.Mc.text())

    def Lv_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Lv', bd))
        print(self.Lv.text())

    def Ts_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Ts', bd))
        print(self.Ts.text())

    def Og_def(self):
        with open('bd.txt', 'r') as f2:
            bd = f2.read().split(',')
        self.label.setText(self.pon('Og', bd))
        print(self.Og.text())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.H.setText(_translate("Dialog", "H"))
        self.Li.setText(_translate("Dialog", "Li"))
        self.Na.setText(_translate("Dialog", "Na"))
        self.K.setText(_translate("Dialog", "K"))
        self.Rb.setText(_translate("Dialog", "Rb"))
        self.Cs.setText(_translate("Dialog", "Cs"))
        self.Fr.setText(_translate("Dialog", "Fr"))
        self.Mg.setText(_translate("Dialog", "Mg"))
        self.Sr.setText(_translate("Dialog", "Sr"))
        self.Ra.setText(_translate("Dialog", "Ra"))
        self.Ba.setText(_translate("Dialog", "Ba"))
        self.Ca.setText(_translate("Dialog", "Ca"))
        self.Be.setText(_translate("Dialog", "Be"))
        self.Sc.setText(_translate("Dialog", "Sc"))
        self.Y.setText(_translate("Dialog", "Y"))
        self.Ti.setText(_translate("Dialog", "Ti"))
        self.Hf.setText(_translate("Dialog", "Hf"))
        self.Zr.setText(_translate("Dialog", "Zr"))
        self.Rf.setText(_translate("Dialog", "Rf"))
        self.V.setText(_translate("Dialog", "V"))
        self.Ta.setText(_translate("Dialog", "Ta"))
        self.Nb.setText(_translate("Dialog", "Nb"))
        self.Db.setText(_translate("Dialog", "Db"))
        self.Cr.setText(_translate("Dialog", "Cr"))
        self.W.setText(_translate("Dialog", "W"))
        self.Mo.setText(_translate("Dialog", "Mo"))
        self.Sg.setText(_translate("Dialog", "Sg"))
        self.Mn.setText(_translate("Dialog", "Mn"))
        self.Re.setText(_translate("Dialog", "Re"))
        self.Tc.setText(_translate("Dialog", "Tc"))
        self.Bh.setText(_translate("Dialog", "Bh"))
        self.Fe.setText(_translate("Dialog", "Fe"))
        self.Os.setText(_translate("Dialog", "Os"))
        self.Ru.setText(_translate("Dialog", "Ru"))
        self.Hs.setText(_translate("Dialog", "Hs"))
        self.Co.setText(_translate("Dialog", "Co"))
        self.Ir.setText(_translate("Dialog", "Ir"))
        self.Rh.setText(_translate("Dialog", "Rh"))
        self.Mt.setText(_translate("Dialog", "Mt"))
        self.Ni.setText(_translate("Dialog", "Ni"))
        self.Pt.setText(_translate("Dialog", "Pt"))
        self.Pd.setText(_translate("Dialog", "Pd"))
        self.Ds.setText(_translate("Dialog", "Ds"))
        self.Cu.setText(_translate("Dialog", "Cu"))
        self.Au.setText(_translate("Dialog", "Au"))
        self.Ag.setText(_translate("Dialog", "Ag"))
        self.Rg.setText(_translate("Dialog", "Rg"))
        self.Zn.setText(_translate("Dialog", "Zn"))
        self.Hg.setText(_translate("Dialog", "Hg"))
        self.Cd.setText(_translate("Dialog", "Cd"))
        self.Cn.setText(_translate("Dialog", "Cn"))
        self.Ga.setText(_translate("Dialog", "Ga"))
        self.Al.setText(_translate("Dialog", "Al"))
        self.Tl.setText(_translate("Dialog", "Tl"))
        self.In.setText(_translate("Dialog", "In"))
        self.Nh.setText(_translate("Dialog", "Nh"))
        self.B.setText(_translate("Dialog", "B"))
        self.Ge.setText(_translate("Dialog", "Ge"))
        self.Si.setText(_translate("Dialog", "Si"))
        self.Pb.setText(_translate("Dialog", "Pb"))
        self.Sn.setText(_translate("Dialog", "Sn"))
        self.Fl.setText(_translate("Dialog", "Fl"))
        self.C.setText(_translate("Dialog", "C"))
        self.As.setText(_translate("Dialog", "As"))
        self.P.setText(_translate("Dialog", "P"))
        self.Bi.setText(_translate("Dialog", "Bi"))
        self.Sb.setText(_translate("Dialog", "Sb"))
        self.Mc.setText(_translate("Dialog", "Mc"))
        self.N.setText(_translate("Dialog", "N"))
        self.Se.setText(_translate("Dialog", "Se"))
        self.S.setText(_translate("Dialog", "S"))
        self.Po.setText(_translate("Dialog", "Po"))
        self.Te.setText(_translate("Dialog", "Te"))
        self.Lv.setText(_translate("Dialog", "Lv"))
        self.O.setText(_translate("Dialog", "O"))
        self.Br.setText(_translate("Dialog", "Br"))
        self.Cl.setText(_translate("Dialog", "Cl"))
        self.At.setText(_translate("Dialog", "At"))
        self.I.setText(_translate("Dialog", "I"))
        self.Ts.setText(_translate("Dialog", "Ts"))
        self.F.setText(_translate("Dialog", "F"))
        self.Kr.setText(_translate("Dialog", "Kr"))
        self.Ar.setText(_translate("Dialog", "Ar"))
        self.Rn.setText(_translate("Dialog", "Rn"))
        self.He.setText(_translate("Dialog", "He"))
        self.Xe.setText(_translate("Dialog", "Xe"))
        self.Og.setText(_translate("Dialog", "Og"))
        self.Ne.setText(_translate("Dialog", "Ne"))
        self.Ho.setText(_translate("Dialog", "Ho"))
        self.Lu.setText(_translate("Dialog", "Lu"))
        self.Pr.setText(_translate("Dialog", "Pr"))
        self.Eu.setText(_translate("Dialog", "Eu"))
        self.Gd.setText(_translate("Dialog", "Gd"))
        self.Tb.setText(_translate("Dialog", "Tb"))
        self.Ce.setText(_translate("Dialog", "Ce"))
        self.Yb.setText(_translate("Dialog", "Yb"))
        self.Pm.setText(_translate("Dialog", "Pm"))
        self.Tm.setText(_translate("Dialog", "Tm"))
        self.Er.setText(_translate("Dialog", "Er"))
        self.La.setText(_translate("Dialog", "La"))
        self.Dy.setText(_translate("Dialog", "Dy"))
        self.Nd.setText(_translate("Dialog", "Nd"))
        self.Sm.setText(_translate("Dialog", "Sm"))
        self.Es.setText(_translate("Dialog", "Es"))
        self.Lr.setText(_translate("Dialog", "Lr"))
        self.Pa.setText(_translate("Dialog", "Pa"))
        self.Am.setText(_translate("Dialog", "Am"))
        self.Cm.setText(_translate("Dialog", "Cm"))
        self.Bk.setText(_translate("Dialog", "Bk"))
        self.Th.setText(_translate("Dialog", "Th"))
        self.No.setText(_translate("Dialog", "No"))
        self.Np.setText(_translate("Dialog", "Np"))
        self.Md.setText(_translate("Dialog", "Md"))
        self.Fm.setText(_translate("Dialog", "Fm"))
        self.Ac.setText(_translate("Dialog", "Ac"))
        self.Cf.setText(_translate("Dialog", "Cf"))
        self.U.setText(_translate("Dialog", "U"))
        self.Pu.setText(_translate("Dialog", "Pu"))
        self.text.setText(_translate("Dialog", "1"))
        self.text_2.setText(_translate("Dialog", "2"))
        self.text_3.setText(_translate("Dialog", "3"))
        self.text_4.setText(_translate("Dialog", "4"))
        self.text_5.setText(_translate("Dialog", "5"))
        self.text_6.setText(_translate("Dialog", "6"))
        self.text_7.setText(_translate("Dialog", "7"))
        self.text_8.setText(_translate("Dialog", "8"))
        self.text_9.setText(_translate("Dialog", "9"))
        self.text_10.setText(_translate("Dialog", "10"))
        self.text_11.setText(_translate("Dialog", "11"))
        self.text_12.setText(_translate("Dialog", "12"))
        self.text_13.setText(_translate("Dialog", "13"))
        self.text_14.setText(_translate("Dialog", "14"))
        self.text_15.setText(_translate("Dialog", "15"))
        self.text_16.setText(_translate("Dialog", "16"))
        self.text_17.setText(_translate("Dialog", "17"))
        self.text_18.setText(_translate("Dialog", "18"))
        self.text_19.setText(_translate("Dialog", "1"))
        self.text_20.setText(_translate("Dialog", "2"))
        self.text_21.setText(_translate("Dialog", "3"))
        self.text_22.setText(_translate("Dialog", "4"))
        self.text_23.setText(_translate("Dialog", "5"))
        self.text_24.setText(_translate("Dialog", "6"))
        self.text_25.setText(_translate("Dialog", "7"))

        self.label.setText(_translate("Dialog", "Здесь будет информация"))

    def pon(self, k: str, bd: list):
        for i in range(len(bd)):
            if bd[i] == k:
                return f"{bd[i - 1]}, {bd[i]}, {bd[i + 1]}, {bd[i + 2]}, {bd[i + 3]}, {bd[i + 4]}"