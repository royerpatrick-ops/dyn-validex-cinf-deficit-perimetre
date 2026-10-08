#!/usr/bin/env python3
"""Exact rational enclosure of the proposed perimeter constant.

No external packages. The mathematical input is the two series for J1 and Jtail;
this program certifies their numerical evaluation, not their model identification.
Tail coefficient bound and binomial alternating remainder are explicit below.
"""
from fractions import Fraction as F
from math import comb, factorial
import argparse, json, time
from pathlib import Path


def outward(q, digits, lower):
    scale=10**digits
    n=q.numerator*scale//q.denominator
    if not lower and F(n,scale)<q:n+=1
    return f'{n//scale}.{n%scale:0{digits}d}'


def atan_bounds(inv, count):
    # inv>1. count even makes the finite sum a lower bound.
    s=sum(F((-1)**k,(2*k+1)*inv**(2*k+1)) for k in range(count))
    t=F((-1)**count,(2*count+1)*inv**(2*count+1))
    return (s,s+t) if t>0 else (s+t,s)


def run(N):
    if N<2:raise ValueError('N must be at least 2')
    start=time.monotonic()
    bh=[F(1)];b3=[F(1)]
    for n in range(1,N+2):
        bh.append(bh[-1]*(F(1,2)-n+1)/n)
        b3.append(b3[-1]*(F(3,2)-n+1)/n)
    alpha=[F(0)]+[(-1)**(n+1)*bh[n] for n in range(1,N+2)]
    p=[F(0),F(1,2)]+[bh[n-1]-7*bh[n] for n in range(2,N+1)]
    J0=F(32,15)+1-F(128,63)-F(17,180)
    J1=F(16,3)*(F(1,20)+F(3,320)+F(1,24)+sum((b3[n]/(6*n+7)-8*bh[n]/(6*n+13))/((2*n+2)*(2*n+3)) for n in range(N+1)))
    n=N+1
    E1=F(16,3)*(abs(b3[n])/(6*n+7)+8*abs(bh[n])/(6*n+13))/((2*n+2)*(2*n+3))
    fac=[factorial(i) for i in range(2*N+2)]
    JT=F(4,3)*sum(alpha[m]*p[n]*F(fac[n]*fac[m],fac[n+m+1])/(3*(m+n)-5) for m in range(1,N+1) for n in range(1,N+1))
    # T_N=sum_{m>N} alpha_m = binom(2N,N)/4^N.
    # sum_{n>=1}|p_n|=5 and sum_{n>N}|p_n|=T_(N-1)+7T_N.
    # B(n+1,m+1)<=1/((m+1)(m+2)) for n>=1, and symmetrically.
    # The denominator 3(m+n)-5 >= 3m-2. Therefore either omitted
    # index>=N+1 gives the common denominator below. The two omitted
    # regions may overlap, but adding their positive bounds remains safe.
    T=F(comb(2*N,N),4**N);Tprev=F(comb(2*(N-1),N-1),4**(N-1))
    ET=F(4,3)*(Tprev+12*T)/((N+2)*(N+3)*(3*N+1))
    Jmid=J0+J1+JT;E=E1+ET;Jlo=Jmid-E;Jhi=Jmid+E
    # Machin identity pi = 16 atan(1/5) - 4 atan(1/239), with exact
    # alternating remainder intervals (30 terms each).
    aLo,aHi=atan_bounds(5,30);bLo,bHi=atan_bounds(239,30)
    piLo=16*aLo-4*bHi;piHi=16*aHi-4*bLo
    Clo=6*Jlo/piHi**2;Chi=6*Jhi/piLo**2
    assert 0<Jlo<Jhi and 0<piLo<piHi
    assert F(1437,2000)<Clo<Chi<F(1439,2000) # 0.7185 < C < 0.7195
    data={'kind':'exact_rational_series_enclosure','N':N,'atan_terms':30,
          'seconds':time.monotonic()-start,'J0':str(J0),
          'J1_mid':str(J1),'J1_error':str(E1),
          'Jtail_mid':str(JT),'Jtail_error':str(ET),
          'J_lower':str(Jlo),'J_upper':str(Jhi),
          'pi_lower':str(piLo),'pi_upper':str(piHi),
          'C_lower':str(Clo),'C_upper':str(Chi),
          'C_decimal_lower_outward':outward(Clo,18,True),
          'C_decimal_upper_outward':outward(Chi,18,False),
          'rounding_three_decimals':'0.719','rounding_three_decimals_verified':True,
          'rounding_six_decimals':'0.719233',
          'rounding_six_decimals_verified':bool(F(1438465,2000000)<Clo<Chi<F(1438467,2000000))}
    return data

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--N',type=int,default=100)
    parser.add_argument('--output',default='CERTIFICATE.json')
    args=parser.parse_args();data=run(args.N)
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:data[k] for k in ['kind','N','seconds','C_decimal_lower_outward','C_decimal_upper_outward','rounding_three_decimals','rounding_three_decimals_verified']},indent=2))
