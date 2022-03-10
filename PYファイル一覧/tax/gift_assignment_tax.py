"""贈与税"""

def giht_tax(gift_asset,age=18):
    kazeikakaku = gift_asset-1100000
    if kazeikakaku <= 0:
        giht_tax_rate = 0
        deduction = 0

    elif kazeikakaku <= 2000000:
        giht_tax_rate = 0.1
        deduction = 0
    elif kazeikakaku <= 3000000:
        giht_tax_rate = 0.15
        deduction = 100000
    elif kazeikakaku <= 4000000:
        if age <18:
            giht_tax_rate = 0.2
            deduction = 250000
        else:
            giht_tax_rate = 0.15
            deduction = 100000
    elif kazeikakaku <= 6000000:
        if age <18:
            giht_tax_rate = 0.3
            deduction = 650000
        else:
            giht_tax_rate = 0.2
            deduction = 300000
            
    elif kazeikakaku <= 10000000:
        if age <18:
            giht_tax_rate = 0.4
            deduction = 1250000
        else:
            giht_tax_rate = 0.3
            deduction = 900000
            
    elif kazeikakaku <= 15000000:
        if age <18:
            giht_tax_rate = 0.45
            deduction = 1750000
        else:
            giht_tax_rate = 0.4
            deduction = 1900000
            
    elif kazeikakaku <= 30000000:
        if age <18:
            giht_tax_rate = 0.5
            deduction = 2500000
        else:
            giht_tax_rate = 0.45
            deduction = 2650000
            
    elif kazeikakaku <= 45000000:
        if age <18:
            giht_tax_rate = 0.55
            deduction = 4000000
        else:
            giht_tax_rate = 0.5
            deduction = 4150000
    elif kazeikakaku > 45000000:
        if age <18:
            giht_tax_rate = 0.55
            deduction = 4000000
        else:
            giht_tax_rate = 0.55
            deduction = 6400000
    
        
            
    # 所得税の計算
    giht_tax_ammount = int(kazeikakaku * giht_tax_rate - deduction)
    #print("贈与課税価格",kazeikakaku,"贈与税率",giht_tax_rate,"控除額=",deduction)
    
    return giht_tax_ammount

"""一般株式の譲渡"""
def general_stock(sell_price,Acquisition_cost,num_of_shares,transfer_cost=0):
    #譲渡所得　= (売却単価-取得単価)×株式数-譲渡経費
    Capital_gains = (sell_price-Acquisition_cost)*num_of_shares-transfer_cost
    Capital_gains_tax= int(Capital_gains*0.15315)
    Capital_gains_resident_tax= int(Capital_gains*0.05)
    return Capital_gains_tax, Capital_gains_resident_tax






