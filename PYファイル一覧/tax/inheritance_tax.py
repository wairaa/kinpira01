"""各相続税額"""

def inheritance_tax_indivisual(net_asset,spouse,child,direct_ancestory=0,brother=0,*args):
    houtei_list = Legal_inheritance(spouse,child,direct_ancestory,brother)
    #print(houtei_list)
    houtei_num = len(houtei_list)
    basic_deduct = 30000000+6000000*houtei_num
    taxable_price = net_asset-basic_deduct
    #print("課税価格=",taxable_price)
    #相続税合計の算定
    tax_inheritance_total =0
    for each in houtei_list:#相続人の法定相続分財産×税率　
        tax_each_houtei=inhritance_rate(each*taxable_price)
        #print(tax_each_houtei)
        #相続税総額を算定
        tax_inheritance_total += int(tax_each_houtei)
    #print("相続税合計=",tax_inheritance_total)
    print("相続税総額",tax_inheritance_total)

    indivisual_tax=[]
    for each in args:
        eachtax = int(each / net_asset * tax_inheritance_total)
        indivisual_tax.append(eachtax)
    print("軽減前相続",indivisual_tax)
    

    if spouse==1:
        #小さいほう（配偶者取得と(160Mと課税合計×配偶者法定相続分の多いほう)）
        kettei = min(args[0],max(taxable_price*houtei_list[0], 160000000))
        spouse_deduct_tax= int(tax_inheritance_total*kettei/taxable_price)
        print("配偶者軽減",spouse_deduct_tax)
        indivisual_tax[0]=max(indivisual_tax[0]-spouse_deduct_tax,0)
    return indivisual_tax


    
                      
                    

    
def inhritance_rate(taxable_price):
    inheritance_deduction = 0
    inheritance_tax_rate = 0
    if taxable_price <= 10000000:
        inheritance_tax_rate = 0.1
    elif taxable_price <= 30000000:
        inheritance_tax_rate = 0.15
        inheritance_deduction = 500000
    elif taxable_price <= 50000000:
        inheritance_tax_rate = 0.2
        inheritance_deduction = 2000000
    elif taxable_price <= 100000000:
        inheritance_tax_rate = 0.3
        inheritance_deduction = 7000000
    elif taxable_price <= 200000000:
        inheritance_tax_rate = 0.4
        inheritance_deduction = 17000000
    elif taxable_price <= 300000000:
        inheritance_tax_rate = 0.45
        inheritance_deduction = 27000000
    elif taxable_price <= 600000000:
        inheritance_tax_rate = 0.5
        inheritance_deduction = 42000000
    elif taxable_price > 600000000:
        inheritance_tax_rate = 0.55
        inheritance_deduction = 72000000
        
    inheritance_tax_amount = taxable_price*inheritance_tax_rate-inheritance_deduction
    return inheritance_tax_amount

#相続税の総額 × 各人の課税価格 ÷ 課税価格の合計額 ＝ 各相続人等の税額

#相続相続分の関数
def Legal_inheritance(spouse=1,child=0,direct_ancestory=0,brother=0):
    #子供が複数いる場合の法定相続分
    if spouse==1 and child >=1:
        inheritance = [0.5]
        child_in = 0.5* (1 / child)
        for i in range(child):
            inheritance.append(child_in)
    elif spouse==1 and child == 0 and direct_ancestory>=1:
        inheritance = [2/3]
        dir_an = 1/3 * (1 / direct_ancestory)
        for i in range(direct_ancestory):
            inheritance.append(dir_an)
    elif spouse==1 and child == 0 and direct_ancestory == 0 and brother>=1:
        inheritance = [3/4]
        brothers = 1/4 * (1 / brother)
        for i in range(brother):
            inheritance.append(brothers)
    elif spouse==1 and child == 0 and direct_ancestory == 0 and brother==0:
        inheritance = [1]
    elif spouse==0 and child >= 1 and direct_ancestory == 0 and brother==0:
        inheritance = []
        child_in = (1 / child)
        for i in range(child):
            inheritance.append(child_in)
    elif spouse==0 and child == 0 and direct_ancestory >= 1 and brother==0:
        inheritance = []
        dir_an = (1 / direct_ancestory)
        for i in range(direct_ancestory):
            inheritance.append(dir_an)
            
    elif spouse==0 and child == 0 and direct_ancestory == 0 and brother>=1:
        inheritance = []
        brothers = (1 / brother)
        for i in range(brother):
            inheritance.append(brothers)
    elif spouse ==0 and child>=1 and direct_ancestory >= 1 or brother>=1:
        inheritance = ["boo"]
    #print(inheritance)
    return inheritance



        
    

    
    
 
