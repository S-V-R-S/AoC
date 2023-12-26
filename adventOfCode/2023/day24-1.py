
f = open("advent code 2023\\input24.txt","r")
lignes = f.read()
f.close()
lignes = lignes.split("\n")
flocons = []


for i,l in enumerate(lignes):
    pos, vitesse = l.split("@")
    x,y,z = [int(i) for i in pos.split(",")]
    vx,vy,vz = [int(i) for i in vitesse.split(",")]
    a = vy
    b = -vx
    c = vy*x - y*vx
    flocons.append([(x,y,z), (vx,vy,vz), (a,b,c)])



nbr = 0
for i in range(len(flocons)):
    for j in range(i+1, len(flocons)):

        flocon1 = flocons[i]
        x0,y0,z0 = flocon1[0]
        vx0,vy0,vz0 = flocon1[1]
        a0,b0,c0 = flocon1[2]

        flocon2 = flocons[j]
        x1,y1,z1 = flocon2[0]
        vx1,vy1,vz1 = flocon2[1]
        a1,b1,c1 = flocon2[2]
        # si c egal ca ne se croise pas car qd on resout le coef serait egal a 0 
        if(a0*b1 != a1*b0):
            x = (b1*c0 - b0*c1) / (a0*b1 - b0*a1)
            y = (c1*a0 - c0*a1) / (a0*b1 - b0*a1)
            # si ca se croise 
            if 200000000000000<=x<=400000000000000 and 200000000000000<=y<=400000000000000:
                # dans le futur 
                if vx0*(x-x0) >= 0 and vy0*(y-y0) >= 0 and vx1*(x-x1) >= 0 and vy1*(y-y1):
                    nbr+=1

print(nbr)

