import ikpy;
import numpy as np;
import matplotlib.pyplot as plt;
import pypot.creatures import PoppyErgoJr;
import random;
import time;
import math;

timeToExecute = 2.0;

flies = [1,2,3,4,5,6,7,8,9,10];

poopy = PoppyErgoJr(simulator='vrep', scene='poppy_ergo_jr_holder.ttt', camera='dummy');

chain = ikpy.chain.Chain.from_urdf_file("poppy_ergo.URDF");

ax = plt.figure().add_subplot(111,projection="3d");

for i in range(10):
    x = 0.1*random.uniform(-1,1);
    y = 0.1*random.uniform(-1,1);
    z = 0.1*random.uniform(-1,1);
    flyPos = np.asarray([x,y,z]);
    flies[i] = plyPos;
    ax.scatter(x,y,z,colors="blue");

for i in range(10):
    ik = chain.inverse_kinematics(flies[i]);
    chain.plot(ik,ax);
    poppy.m1.goto_position(ik[1]*180/math.pi, timeToExecute);
    poppy.m2.goto_position(ik[1]*180/math.pi, timeToExecute);
    poppy.m3.goto_position(ik[1]*180/math.pi, timeToExecute);
    poppy.m4.goto_position(ik[1]*180/math.pi, timeToExecute);
    poppy.m5.goto_position(ik[1]*180/math.pi, timeToExecute);
    poppy.m6.goto_position(ik[1]*180/math.pi, timeToExecute);
    time.sleep(timeToExecute);
print("Finished")


def longeur(x,y,z,ordreMouche):
    i = ordreMouche[-1]
    x0,y0,z0 = x[]