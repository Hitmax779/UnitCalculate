class UnitCalculate:
    def __init__(self,UA,C1,B,AOV,COGS,OneSCOGS,APC,CLTV,LTV,LTC,AC,RV,CM,Share,N,AvP,T,CPA,CAC,L,SP,NS,ARCl,IR):
        self.UA = UA # поток привлекаемых клиентов
        self.C1 = C1 #ставка конверсии(в %)
        self.B = B # кол-во клиентов
        self.AOV = AOV # средний чек - сумма всех платежей всех клиентов, деленная  на кол-во платежей
        self.COGS = COGS # траты на бизнес в момент сделки
        self.OneSCOGS = OneSCOGS # дополнительные траты на бизнес
        self.APC = APC # среднее число сделок на 1 клиента
        self.CLTV = CLTV # валовая прибыль на одного клиента
        self.LTV = LTV # валовая прибыль на 1 юнит
        self.LTC = LTC # стоимость маркетинговых затрат на 1 юнит
        self.AC = AC # маркетинговый бюджет на привлечение клиентов
        self.RV = RV # оборот
        self.CM = CM # маржинальная прибыль
        self.Share = Share # доля клиентов, покупающих тариф
        self.N = N # кол-во товаров в корзине
        self.AvP = AvP # средняя стоимость товара в корзине
        self.T = T #общее кол-во транзакций
        self.CPA = CPA # стоимость целевого действия(затраты)
        self.CAC = CAC # затраты на 1 клиента
        self.L = L # кол-во лидов
        self.SP = SP # цена лида
        self.NS = NS # среднее кол-во продаж 1 лида
        self.ARCl = ARCl # реализация лидов
        self.IR = IR # кол-во клиентов
    def find_UA(CLTV,C1,LTC,CM):
        return CM / (CLTV * (C1 / 100) - LTC)
    def find_C1(LTC,CLTV):
        return LTC / CLTV
    def find_C1_searchbyLTV(LTV,CLTV):
        return LTV / CLTV
    def find_C1_searchbyCM(CM,LTV):
        return CM / LTV
    def find_C1_searchbyCM_details(CM,UA,CLTV,LTC):
        return (CM / UA + LTC) / CLTV
    def find_B(UA,C1):
        return UA * (C1 / 100)
    def find_AOV_searchbyShare(N,Avp,Share):
        return N * (Avp + Share)
    def find_AOV_searchbyCLTV(CLTV,COGS,APC,OneSCOGS):
        return (CLTV + COGS * APC + (OneSCOGS - COGS * APC) / APC * APC) / APC
    def find_COGS(AOV,APC,CLTV,OneSCOGS):
        return (AOV * APC - CLTV - OneSCOGS) / APC
    def find_1sCOGS(AOV,APC,COGS,CLTV):
        return AOV * APC - COGS * APC - CLTV
    def find_APC(T,B):
        return T / B
    def find_APC_searchbyCLTV(CLTV,OneSCOGS,AOV,COGS):
        return (CLTV + OneSCOGS) / (AOV - COGS)
    def find_CLTV(AOV,COGS,APC,OneSCOGS):
        return (AOV - COGS) * APC - OneSCOGS
    def find_CLTV_searchbyCM(CM,UA,LTC,C1):
        return (CM + UA * LTC) / (UA * (C1 / 100))
    def find_LTV(CLTV,C1):
        return CLTV * (C1 / 100)
    def find_LTV_searchbyCM(CM,UA,CPA):
        return (CM + UA * CPA) / UA
    def find_CLTC(LTC,C1):
        return LTC / (C1 / 100)
    def find_CLTC_searchbyCM(B,CLTV,CM):
        return (B * CLTV - CM) / B
    def find_AC(UA,CPA):
        return UA * CPA 
    def find_AC_byCAC(B,CAC):
        return B * CAC
    def find_REV(B,AOV,APC):
        return B * AOV * APC
    def find_CM_searchbyCLTV(UA,CLTV,C1, LTC):
        return UA*(CLTV * (C1 / 100) - LTC)
    def find_CM_searchbyLTV(UA,LTV,LTC):
        return UA * (LTV - LTC)
    def find_CM_searchbyB(B,CLTV,CLTC):
        return B*(CLTV - CLTC)
    def find_N(AOV,AvP,Share):
        return AOV/(AvP * Share)
    def find_AvP(AOV,N,Share):
        return AOV/(N*Share)
    def find_Share(AOV,N,AvP):
        return AOV/(N*AvP)
    def find_AOV_mixed(NS,SP,ARCl,L,IR,B):
        return NS * SP * ARCl * L * IR / B
    def find_NS_mixed(AOV,B,SP,ARCl,L,IR):
        return AOV * B / (SP * ARCl * L * IR)
    def find_SP_mixed(AOV,B,NS,ARCl,L,IR):
        return AOV * B / (NS * ARCl * L * IR)
    def find_ARCl_mixed(AOV,B,NS,SP,L,IR):
        return AOV * B / (NS * SP * L * IR)
    def find_L_mixed(AOV,B,NS,SP,ARCl,IR):
        return AOV * B / (NS * SP * ARCl * IR)
    def find_IR_mixed(AOV,B,NS,SP,ARCl,L):
        return AOV * B / (NS * SP * ARCl * L)
    def find_B_mixed(NS,SP,ARCl,L,IR,AOV):
        return NS * SP * ARCl * L * IR / AOV
    