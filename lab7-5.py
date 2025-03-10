def q5():
    d_price={"rabdi":120,"basundi":20,"thandai":100}
    d_quantity={"rabdi":1,"basundi":2,"thandai":10}
    total=0
    for key in d_price.keys():
        total=total+d_price[key]*d_quantity[key]
    print(total)
q5()