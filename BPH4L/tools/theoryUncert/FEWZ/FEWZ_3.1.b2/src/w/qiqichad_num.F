CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC


      double precision function qiqicnum1e0(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      t5 = -s1l1*s2l2-s1l2*s2l1
      t6 = dlog(z)
      t11 = z**2
      taux1 = -8*z*(1+z)*t5*t6+4.D0/3.D0*(z-1)*(4*t11+7*z+4)*t5
      t5 = -s1l2*s2l1+s1l1*s2l2
      t6 = dlog(z)
      t11 = z**2
      taux2 = 32*z*(1+z)*t5*t6-16.D0/3.D0*(z-1)*(4*t11+7*z+4)*t5

CCC Coefficients

      tcoff1 = taux1
      tcoff2 = taux1
      tcoff3 = taux2
      tcoff4 = taux2

CCC Jet functions

      tFjet1 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff1)
      tFjet2 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff2)
      tFjet3 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff3)
      tFjet4 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff4)

CCC Sum

      qiqicnum1e0 = tFjet1*tcoff1+tFjet2*tcoff2+tFjet3*tcoff3+tFjet4*tco
     #ff4
      RETURN
      END

      double precision function qiqicnum1e1(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      t3 = dlog(z)
      t7 = z**2
      taux1 = -8*z*(1+z)*t3+4.D0/3.D0*(z-1)*(4*t7+7*z+4)
      t5 = -s1l2*s2l1+s1l1*s2l2
      t6 = dlog(z)
      t11 = z**2
      taux2 = -96*z*(1+z)*t5*t6+16*(z-1)*(4*t11+7*z+4)*t5

CCC Coefficients

      tcoff1 = taux1
      tcoff2 = taux1
      tcoff3 = taux2
      tcoff4 = taux2

CCC Jet functions

      tFjet1 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff1)
      tFjet2 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff2)
      tFjet3 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff3)
      tFjet4 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff4)

CCC Sum

      qiqicnum1e1 = tFjet1*tcoff1+tFjet2*tcoff2+tFjet3*tcoff3+tFjet4*tco
     #ff4
      RETURN
      END

      double precision function qiqicnum1e2(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      taux1 = 0
      t5 = -s1l2*s2l1+s1l1*s2l2
      t6 = dlog(z)
      t11 = z**2
      taux2 = 64*z*(1+z)*t5*t6-32.D0/3.D0*(z-1)*(4*t11+7*z+4)*t5

CCC Coefficients

      tcoff1 = taux1
      tcoff2 = taux1
      tcoff3 = taux2
      tcoff4 = taux2

CCC Jet functions

      tFjet1 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff1)
      tFjet2 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff2)
      tFjet3 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff3)
      tFjet4 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff4)

CCC Sum

      qiqicnum1e2 = tFjet1*tcoff1+tFjet2*tcoff2+tFjet3*tcoff3+tFjet4*tco
     #ff4
      RETURN
      END

      double precision function qiqicnum1e3(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      taux1 = 0
      taux2 = 0

CCC Coefficients

      tcoff1 = taux1
      tcoff2 = taux1
      tcoff3 = taux2
      tcoff4 = taux2

CCC Jet functions

      tFjet1 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff1)
      tFjet2 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff2)
      tFjet3 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff3)
      tFjet4 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff4)

CCC Sum

      qiqicnum1e3 = tFjet1*tcoff1+tFjet2*tcoff2+tFjet3*tcoff3+tFjet4*tco
     #ff4
      RETURN
      END

      double precision function qiqicnum2e0(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      t5 = -s1l1*s2l2-s1l2*s2l1
      t6 = dlog(z)
      t7 = t6**2
      t12 = z**2
      taux3 = 4*z*(1+z)*t5*t7-4.D0/3.D0*z*(15*z+8*t12+3)*t5*t6+8.D0/9.D0
     #*(z-1)*(28*t12+z+10)*t5
      t5 = -s1l2*s2l1+s1l1*s2l2
      t6 = dlog(z)
      t7 = t6**2
      t12 = z**2
      taux4 = -16*z*(1+z)*t5*t7+16.D0/3.D0*z*(15*z+8*t12+3)*t5*t6-32.D0/
     #9.D0*(z-1)*(28*t12+z+10)*t5

CCC Coefficients

      tcoff5 = taux3
      tcoff6 = taux3
      tcoff7 = taux4
      tcoff8 = taux4

CCC Jet functions

      tFjet5 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff5)
      tFjet6 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff6)
      tFjet7 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff7)
      tFjet8 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff8)

CCC Sum

      qiqicnum2e0 = tFjet5*tcoff5+tFjet6*tcoff6+tFjet7*tcoff7+tFjet8*tco
     #ff8
      RETURN
      END

      double precision function qiqicnum2e1(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      t3 = dlog(z)
      t4 = t3**2
      t8 = z**2
      taux3 = 4*z*(1+z)*t4-4.D0/3.D0*z*(15*z+8*t8+3)*t3+8.D0/9.D0*(z-1)*
     #(28*t8+z+10)
      t5 = -s1l2*s2l1+s1l1*s2l2
      t6 = dlog(z)
      t7 = t6**2
      t12 = z**2
      taux4 = 48*z*(1+z)*t5*t7-16*z*(15*z+8*t12+3)*t5*t6+32.D0/3.D0*(z-1
     #)*(28*t12+z+10)*t5

CCC Coefficients

      tcoff5 = taux3
      tcoff6 = taux3
      tcoff7 = taux4
      tcoff8 = taux4

CCC Jet functions

      tFjet5 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff5)
      tFjet6 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff6)
      tFjet7 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff7)
      tFjet8 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff8)

CCC Sum

      qiqicnum2e1 = tFjet5*tcoff5+tFjet6*tcoff6+tFjet7*tcoff7+tFjet8*tco
     #ff8
      RETURN
      END

      double precision function qiqicnum2e2(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      taux3 = 0
      t5 = -s1l2*s2l1+s1l1*s2l2
      t6 = dlog(z)
      t7 = t6**2
      t12 = z**2
      taux4 = -32*z*(1+z)*t5*t7+32.D0/3.D0*z*(15*z+8*t12+3)*t5*t6-64.D0/
     #9.D0*(z-1)*(28*t12+z+10)*t5

CCC Coefficients

      tcoff5 = taux3
      tcoff6 = taux3
      tcoff7 = taux4
      tcoff8 = taux4

CCC Jet functions

      tFjet5 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff5)
      tFjet6 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff6)
      tFjet7 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff7)
      tFjet8 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff8)

CCC Sum

      qiqicnum2e2 = tFjet5*tcoff5+tFjet6*tcoff6+tFjet7*tcoff7+tFjet8*tco
     #ff8
      RETURN
      END

      double precision function qiqicnum2e3(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(1.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,0.0d0,
     & 1.0d0,1.0d0,l1,l2,l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,
     & s2l2,s3l2,s4l2,c3l1,-999.0d0)

CCC Auxiliary functions

      taux3 = 0
      taux4 = 0

CCC Coefficients

      tcoff5 = taux3
      tcoff6 = taux3
      tcoff7 = taux4
      tcoff8 = taux4

CCC Jet functions

      tFjet5 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,2.D0,1.D0,z,Tcoeff*
     #tcoff5)
      tFjet6 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,2.D0,1.D0,z,Tcoef
     #f*tcoff6)
      tFjet7 = Fjet(var,ndim,z,ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1.D
     #0,1.D0,s1l1,s2l1,0.D0,0.D0,s1l2,s2l2,0.D0,0.D0,9.D0,1.D0,z,Tcoeff*
     #tcoff7)
      tFjet8 = Fjet(var,ndim,z,1/ux,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,0.D0,1
     #.D0,1.D0,s2l1,s1l1,0.D0,0.D0,s2l2,s1l2,0.D0,0.D0,9.D0,1.D0,z,Tcoef
     #f*tcoff8)

CCC Sum

      qiqicnum2e3 = tFjet5*tcoff5+tFjet6*tcoff6+tFjet7*tcoff7+tFjet8*tco
     #ff8
      RETURN
      END

      double precision function qiqicnum3e0(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(zp,s13,0.0d0,s23,0.0d0,0.0d0,s1v,s2v,1.0d0,zp,l1,l2,
     & l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1,
     & qflag)

CCC Auxiliary functions

      t2 = (1-yp)**2
      t6 = zp-1
      t10 = zp*l1
      t12 = -64*l1-64*zp+64*t10
      t17 = 64-64*l1-128*zp+64*t10
      t18 = -s1l2-s2l2-zp
      t23 = -s1l1-s2l1-zp
      t28 = -64*t6
      taux5 = 2.D0/3.D0*(1+t2)/yp*((128*t6*l1*s1l2+t12*s2l2+t17*t18)*s1l
     #1+(t12*s2l1+t17*t23)*s1l2+t28*t18*s2l1+t28*t23*s2l2+128*t23*t18)
      t2 = (1-yp)**2
      t6 = zp*l1
      t7 = -l1-zp+t6
      t10 = 1-l1-2*zp+t6
      t11 = -s1l2-s2l2-zp
      t17 = -s1l1-s2l1-zp
      t22 = -zp+1
      taux6 = 2.D0/3.D0*(1+t2)/yp*((256*t7*s2l2+256*t10*t11)*s1l1+(-256*
     #t7*s2l1-256*t10*t17)*s1l2+256*t22*t11*s2l1-256*t22*t17*s2l2)

CCC Coefficients

      tcoff9 = taux5
      tcoff10 = taux5
      tcoff11 = taux6
      tcoff12 = taux6

CCC Jet functions

      tFjet9 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,zp
     #,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tcoff
     #9)
      tFjet10 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tc
     #off10)
      tFjet11 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,z
     #p,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tcof
     #f11)
      tFjet12 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tc
     #off12)

CCC Sum

      qiqicnum3e0 = tFjet9*tcoff9+tFjet10*tcoff10+tFjet11*tcoff11+tFjet1
     #2*tcoff12
      RETURN
      END

      double precision function qiqicnum3e1(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(zp,s13,0.0d0,s23,0.0d0,0.0d0,s1v,s2v,1.0d0,zp,l1,l2,
     & l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1,
     & qflag)

CCC Auxiliary functions

      t2 = (1-yp)**2
      t6 = zp*l1
      t8 = 64-64*l1+64*t6
      t25 = l1**2
      t28 = zp**2
      taux5 = 2.D0/3.D0*(1+t2)/yp*(t8*s2l2*s1l1+t8*s2l1*s1l2+(128*(zp-1)
     #*(-1+l1)*s2l2+t8*(-s1l2-s2l2-zp))*s2l1+t8*(-s1l1-s2l1-zp)*s2l2-64*
     #zp*(2*zp*t25+2*t28*l1-t28*t25-2*t28-t25-2*t6+2*zp-1))
      t2 = (1-yp)**2
      t6 = zp*l1
      t7 = 3*t6
      t8 = 3*l1
      t9 = 3*zp
      t10 = -t7+t8+t9+1
      t13 = -3+t8+6*zp-t7
      t14 = -s1l2-s2l2-zp
      t20 = -s1l1-s2l1-zp
      t25 = -3-l1+t9+t6
      taux6 = 2.D0/3.D0*(1+t2)/yp*((256*t10*s2l2+256*t13*t14)*s1l1+(-256
     #*t10*s2l1-256*t13*t20)*s1l2+256*t25*t14*s2l1-256*t25*t20*s2l2)

CCC Coefficients

      tcoff9 = taux5
      tcoff10 = taux5
      tcoff11 = taux6
      tcoff12 = taux6

CCC Jet functions

      tFjet9 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,zp
     #,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tcoff
     #9)
      tFjet10 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tc
     #off10)
      tFjet11 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,z
     #p,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tcof
     #f11)
      tFjet12 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tc
     #off12)

CCC Sum

      qiqicnum3e1 = tFjet9*tcoff9+tFjet10*tcoff10+tFjet11*tcoff11+tFjet1
     #2*tcoff12
      RETURN
      END

      double precision function qiqicnum3e2(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(zp,s13,0.0d0,s23,0.0d0,0.0d0,s1v,s2v,1.0d0,zp,l1,l2,
     & l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1,
     & qflag)

CCC Auxiliary functions

      t2 = (1-yp)**2
      t6 = zp**2
      t7 = l1**2
      taux5 = -128.D0/3.D0*(1+t2)/yp*zp*(t6*t7+2*zp*l1-2*zp*t7+1+t7-2*l1
     #)
      t2 = (1-yp)**2
      t6 = zp*l1
      t7 = 2*zp
      t8 = t6-3-l1-t7
      t11 = 1-l1-t7+t6
      t12 = -s1l2-s2l2-zp
      t19 = -s1l1-s2l1-zp
      t26 = -3*t6+1+3*l1-t7
      taux6 = 2.D0/3.D0*(1+t2)/yp*((256*t8*s2l2+512*t11*t12)*s1l1+(-256*
     #t8*s2l1-512*t11*t19)*s1l2+256*t26*t12*s2l1-256*t26*t19*s2l2)

CCC Coefficients

      tcoff9 = taux5
      tcoff10 = taux5
      tcoff11 = taux6
      tcoff12 = taux6

CCC Jet functions

      tFjet9 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,zp
     #,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tcoff
     #9)
      tFjet10 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tc
     #off10)
      tFjet11 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,z
     #p,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tcof
     #f11)
      tFjet12 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tc
     #off12)

CCC Sum

      qiqicnum3e2 = tFjet9*tcoff9+tFjet10*tcoff10+tFjet11*tcoff11+tFjet1
     #2*tcoff12
      RETURN
      END

      double precision function qiqicnum3e3(var,ndim,z,ux,l1,
     & l2,l3,l4,l5,l6,l7,l8,flag1,flag2,qflag,Tcoeff)
      IMPLICIT double precision(s,t)
      double precision Tcoeff
      INTEGER ndim
      double precision var(ndim)
      double precision lum,Pi,z3,NF,Li2
      double precision l1,l2,l3,l4,l5,l6,l7,l8,z,u,r,t,ux,Fjet
      double precision k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,s34r2
      external k1,s13f,s23f,s14f,s24f,s3vf,s4vf,f1,f2,f3,s34r2,
     & s23r2,s1vr2,s2vr2,s23rf,s34rf,s1vrf,s13rf,Fjet
      double precision s34r,s13r,s23r,s1vr,s3vr,s4vr,s2vr,
     & s134r,s234r,flag1,flag2
      double precision s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1
      double precision s13,s23,s1v,s2v,zp,yp,qflag
      external fillspin,Li2
      NF = 5.0d0
      Pi = 3.141592654d0
      z3 = 1.202056903d0
      yp = l2*(1.0d0-z)+z
      zp=z/yp
      s13 = -(1.0d0-l1)*(1.0d0-zp)
      s23 = -l1*(1.0d0-zp)
      s1v = s23
      s2v = s13
      call fillspin(zp,s13,0.0d0,s23,0.0d0,0.0d0,s1v,s2v,1.0d0,zp,l1,l2,
     & l3,l4,l5,l6,l7,l8,s1l1,s2l1,s3l1,s4l1,s1l2,s2l2,s3l2,s4l2,c3l1,
     & qflag)

CCC Auxiliary functions

      taux5 = 0
      t2 = (1-yp)**2
      t7 = zp*l1+1-l1
      taux6 = 2.D0/3.D0*(1+t2)/yp*(512*t7*s2l2*s1l1-512*t7*s2l1*s1l2+512
     #*t7*(-s1l2-s2l2-zp)*s2l1-512*t7*(-s1l1-s2l1-zp)*s2l2)

CCC Coefficients

      tcoff9 = taux5
      tcoff10 = taux5
      tcoff11 = taux6
      tcoff12 = taux6

CCC Jet functions

      tFjet9 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,zp
     #,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tcoff
     #9)
      tFjet10 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,2.D0,1.D0,yp,Tcoeff*tc
     #off10)
      tFjet11 = Fjet(var,ndim,z,ux,s13,s23,0.D0,0.D0,0.D0,s23,s13,1.D0,z
     #p,s1l1,s2l1,s3l1,0.D0,s1l2,s2l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tcof
     #f11)
      tFjet12 = Fjet(var,ndim,z,1/ux,s23,s13,0.D0,0.D0,0.D0,s13,s23,1.D0
     #,zp,s2l1,s1l1,s3l1,0.D0,s2l2,s1l2,s3l2,0.D0,9.D0,1.D0,yp,Tcoeff*tc
     #off12)

CCC Sum

      qiqicnum3e3 = tFjet9*tcoff9+tFjet10*tcoff10+tFjet11*tcoff11+tFjet1
     #2*tcoff12
      RETURN
      END

