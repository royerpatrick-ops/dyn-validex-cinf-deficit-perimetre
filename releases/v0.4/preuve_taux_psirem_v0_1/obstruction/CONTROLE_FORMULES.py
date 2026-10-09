"""Quadrature déterministe des formules de la pointe ; aucun Monte-Carlo."""
import json
import math
from pathlib import Path
from scipy.integrate import quad

def ff(x,y):
    if x == 0:
        return 1/(24*y*y)
    if y*y <= x/2:
        return 1/(2*x)-2*math.sqrt(2)*y/(3*x**1.5)+y*y/(2*x*x)
    return 1/(24*y*y)

def integrals(x,y,b=None):
    if y == 0:
        return 0., x*x/24
    rr=x*x+y*y
    lam=x/(2*y*y)
    c=x/(y*rr)
    def comp(t):
        p=1-x*y*t
        w=max(p**-3-lam*lam*p,0)
        if b is None:
            j=(1-abs(t))**3/6
        else:
            rho=(b+c-t) if t>=0 else (-b-c+t)
            rho=rho%1
            j=rho*max(1-rho-abs(t),0)
        return w*j
    jc=y**4*quad(comp,-1,1,points=[0],epsabs=1e-12,limit=500)[0]
    if x == 0:
        return jc, 0.
    def short(t):
        s=math.sqrt(1+x**3*t*t/8)
        d=1/x-y*math.sqrt(2)*x**-1.5*s+y*t/2
        if b is None:
            if d>=y:
                k=(1-t)*(d-y*t/2)
            elif d<=-y:
                k=0.
            else:
                k=(max(d+y*(1-t),0)**3-max(d,0)**3
                   -max(d-y*t,0)**3+max(d-y,0)**3)/(6*y*y)
        else:
            rho=(b-y/(x*rr)+math.sqrt(2)*x**-1.5*s-t/2)%1
            l1=max(1-rho-t,0)
            l2=1-t-l1
            k=l1*max(d+y*rho,0)+l2*max(d-y*(1-rho),0)
        return t*k
    js=x**3/4*quad(short,0,1,epsabs=1e-12,limit=500)[0]
    return jc,js

rows=[]
for x in [0.04,0.01,0.0025]:
    for rat in [0,0.5,1,2,4]:
        y=rat*math.sqrt(x/2)
        jc,js=integrals(x,y)
        f=ff(x,y)
        rows.append(dict(x=x,y=y,ratio=rat,inside_proved_domain=math.hypot(x,y)<=0.5,F=f,Jcomp_average_b=jc,
                         Jshort_average_b=js,Psi_average_b=f+y/2-jc+js))
fixed=[]
x=0.01;y=math.sqrt(x/2)
for b in [0,0.25,0.5]:
    jc,js=integrals(x,y,b)
    fixed.append(dict(x=x,y=y,b=b,Psi=ff(x,y)+y/2-jc+js))
vertical=[]
for b in [0,0.5]:
    y=0.5;jc,js=integrals(0,y,b)
    vertical.append(dict(y=y,b=b,Jcomp=jc,Psi=ff(0,y)+y/2-jc+js))
result=dict(status="DETERMINISTIC_QUADRATURE_NOT_INTERVAL_CERTIFICATE",
            rows_average_b=rows,fixed_b=fixed,vertical=vertical)
out=Path(__file__).with_name("CONTROLE_FORMULES_RESULTAT.json")
out.write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
