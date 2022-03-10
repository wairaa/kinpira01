
"""
令和2年における最新版
"""
class Tax():
    def __init__(self, gross_salary, Business_income,partner = 0, general_huyou = 2, college_student = 0, handicapped = 1, \
                 rebate_contribution_rate = 0, health_insurance_premium_rate = 0.1209, spouse = 0, life_deduct = 120000, \
                social_insurance=1338059, medical_exp_deduct=180000):

        self.gross_salary = gross_salary #給与収入
        self.Business_income = Business_income #事業所得
        self.partner = partner #配偶者の有無
        self.general_huyou = general_huyou #一般の扶養がいるか
        self.college_student = college_student #大学生の扶養がいるか
        self.handicapped = handicapped #障害者か
        # 免除保険料率. 2.4〜5.0％の範囲で決まる. デフォルトは4.0%
        #年齢と共に上がる傾向にあり、20~30~40~50代でだいたい3.5~4.0~4.5~5.0%くらいを推移する
        self.rebate_contribution_rate = rebate_contribution_rate
        # 健康保険料率. デフォルトは40歳大阪12.09%
        self.health_insurance_premium_rate = health_insurance_premium_rate
        self.spouse = spouse #配偶者がいれば1
        self.life_deduct = life_deduct #生命保険料控除
        self.medical_exp_deduct = medical_exp_deduct #医療費控除
        self.social_insurance=social_insurance #社会保険料=0は計算　0以外は社会保険料合計
        self.income_tax_rate = 0 #income()で代入する. ふるさと納税の計算で使い回す
        self.total_income = self.total_income() #合計所得金額
        self.total_income_amount = self.total_income_amount()
        self.Employment_income=self.Employment_income()
                

    def Employment_income(self):
        """
        給与所得控除の計算, 収入を引数として控除額を返す
        2020年以降は控除が10万減額し、所得税で10万増えたので実質変わらない
        ただし、850万以上は給与所得控除の額が減ったで実質的には増税
        """
        employment_income_deduction = 0

        if self.gross_salary < 550000:
            employment_income_deduction = self.gross_salary
            
        elif self.gross_salary <1625000:
            employment_income_deduction = 550000

        elif self.gross_salary <1800000:
            employment_income_deduction = self.gross_salary * 0.4 - 100000

        elif self.gross_salary <3600000:
            employment_income_deduction = self.gross_salary*0.3 + 80000

        elif self.gross_salary <6600000:
            employment_income_deduction = self.gross_salary*0.2 + 440000

        elif self.gross_salary <8500000:
            employment_income_deduction = self.gross_salary*0.1 + 1100000

        else:
            employment_income_deduction = 1950000

        Employment_income = self.gross_salary - employment_income_deduction
        return Employment_income
    
    def total_income(self):
        total_income = self.Employment_income() + self.Business_income
        return total_income
    

    def social_insurance_premium(self):
        """
        保険料の計算
        保険料率 ＝ 健康保険料率/2
        + (厚生年金保険料率18.3%-免除保険料率)/2
        + 雇用保険料率0.3%
        """
        if self.social_insurance == 0:
            # 保険料率
            insurance_premium_rate = (self.health_insurance_premium_rate)/2 \
             + (0.183 - self.rebate_contribution_rate)/2 + 0.003
            # 社会保険料 = 年収 x 保険料率
            social_insurance_premium = int(self.gross_salary*insurance_premium_rate)
        else:
            social_insurance_premium=self.social_insurance

        return social_insurance_premium

    def spousal_deduction(self):
        
        #配偶者控除の計算
        if self.spouse == 0:
            spousal_deduction = 0
        if self.spouse == 1:
            if self.total_income <= 9000000:
                spousal_deduction = 380000

            elif self.total_income <= 9500000:
                spousal_deduction = 260000

            elif self.total_income <= 10000000:
                spousal_deduction = 130000
        return spousal_deduction

    def total_income_amount(self):
        #総所得金額の計算
        # 所得税における扶養控除
        dependents_deduction = self.general_huyou * 480000 + self.college_student * 630000
        # 所得税における障害者控除
        handicapped_deduction = self.handicapped * 270000
        # 基礎控除2000万を超えると段階的に減る
        basic_deduction = 0
        if self.total_income <= 24000000:
            basic_deduction = 480000
        elif self.total_income <= 24500000:
            basic_deduction = 320000
        elif self.total_income <= 25000000:
            basic_deduction = 160000
            
        self.life_deduct

        # 所得税の対象となる金額、所得から控除や保険料を引いたもの
        total_income_amount = (self.total_income \
                                - self.social_insurance_premium() \
                                - self.spousal_deduction() \
                                - dependents_deduction \
                                - handicapped_deduction \
                                - basic_deduction-self.life_deduct-self.medical_exp_deduct)
        return total_income_amount
    
    def income_tax(self):
        # 年収別の所得税率と控除額⇒関数化
        if self.total_income_amount < 1950000:
            self.income_tax_rate = 0.05
            deduction = 0

        elif self.total_income_amount < 3300000:
            self.income_tax_rate = 0.1
            deduction = 97500

        elif self.total_income_amount < 6950000:
            self.income_tax_rate = 0.2
            deduction = 427500

        elif self.total_income_amount < 9000000:
            self.income_tax_rate = 0.23
            deduction = 636000

        elif self.total_income_amount < 18000000:
            self.income_tax_rate = 0.33
            deduction = 1536000

        elif self.total_income_amount < 40000000:
            self.income_tax_rate = 0.40
            deduction = 2796000

        else:
            self.income_tax_rate = 0.45
            deduction = 4796000

        # 所得税の計算
        income_tax = int(self.total_income_amount * self.income_tax_rate - deduction)
        # 所得税がマイナスにになった場合はゼロにする
        if income_tax <= 0:
            income_tax = 0
        return income_tax

    def inhabitant_tax(self):
        """
        住民税の計算, 課税所得を引数に住民税を計算する
        """

        # 住民税における扶養控除
        dependents_deduction = self.general_huyou * 330000 + self.college_student * 450000
        # 住民税における障害者控除
        handicapped_deduction = self.handicapped * 260000
        # 基礎控除、所得税と同様2020年から変更
        basic_deduction = 0
        if self.total_income <= 24000000:
            basic_deduction = 430000
        elif self.total_income <= 24500000:
            basic_deduction = 290000
        elif self.total_income <= 25000000:
            basic_deduction = 150000

        # 所得から各種控除、基礎控除（43万円）を引き、税率10%をかける
        # さらに均等割5000円を足して、調整控除2500円を引く
        inhabitant_tax = int((self.total_income
                          - self.social_insurance_premium()
                          - self.spousal_deduction()
                          - dependents_deduction
                          - handicapped_deduction 
                          - basic_deduction-self.life_deduct-self.medical_exp_deduct) * 0.1 + 5000 - 2500)

        # 計算した住民税がマイナスになった場合はゼロとする
        if inhabitant_tax <=0:
            inhabitant_tax = 0
        return inhabitant_tax

    def net_salary(self):
        """
        手取りの計算、収入から所得税、住民税、社会保険料を引く
        """
        total_tax = self.inhabitant_tax() + self.income_tax()
        net_salary = int(self.gross_salary - total_tax - self.social_insurance_premium())
        return net_salary

    def max_hurusato_donation(self):
        """
        ふるさと納税で自己負担2000円で全額控除される上限の計算
        言い換えるとreturnの金額から2000円引いたものが所得税および住民税から控除される
        """
        # 住民税所得割額(=住民税)から計算する
        # ふるさと納税控除額の上限
        hurusato_deduction = self.inhabitant_tax() * 0.2

        # (控除金額) =（寄附金額-2000）×（90％-所得税の税率×1.021）
        # (寄付金額) = (控除金額)/(90％-所得税の税率×1.021)+2000
        max_hurusato_donation = int(hurusato_deduction / (0.9 - self.income_tax_rate * 1.021) + 2000)
        return max_hurusato_donation
