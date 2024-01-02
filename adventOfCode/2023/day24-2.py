import sympy

f = open("adventOfCode\\2023\\input24.txt","r")
lignes = f.read()
f.close()
lignes = lignes.split("\n")

xc, yc, zc, vxc, vyc , vzc = sympy.symbols("xc, yc, zc, vxc, vyc , vzc")
equations = []
for i,l in enumerate(lignes):
    pos, vitesse = l.split("@")
    x,y,z = [int(i) for i in pos.split(",")]
    vx,vy,vz = [int(i) for i in vitesse.split(",")]
    equations.append((x-xc)*(vyc-vy)-(y-yc)*(vxc-vx))
    equations.append((x-xc)*(vzc-vz)-(z-zc)*(vxc-vx))


reponse = sympy.solve(equations)
reponse = reponse[0]
print(reponse[xc]+reponse[yc]+reponse[zc])