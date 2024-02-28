def run(x):
    if x ==6:
        return
    

    print(x, end= '')
    run(x+1)
    print(x, end= '')
    
run(0)

