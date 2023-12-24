import sympy as sym

hailstones = []

with open("day24-input.txt", "r") as f:
    for i in f.readlines():
        position, velocity = i.strip().split("@")
        position, velocity = list(map(int, position.split(","))), list(
            map(int, velocity.split(","))
        )

        hailstones.append([position, velocity])


x, y, z, vx, vy, vz = sym.symbols("x,y,z,vx,vy,vz")

equations = []
for (x1, y1, z1), (vx1, vy1, vz1) in hailstones:
    equations.append(sym.Eq((x - x1) * (vy - vy1), (y - y1) * (vx - vx1)))
    equations.append(sym.Eq((x - x1) * (vz - vz1), (z - z1) * (vx - vx1)))
result = sym.solve(equations, (x, y, z, vx, vy, vz))


open("day24-p2-output.txt", "w").write(str(sum(result[0][:3])))
