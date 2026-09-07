from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Arc
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'/'diagrams'
from matplotlib import font_manager
for style in ('Regular','Semibold','Bold'):
 font_manager.fontManager.addfont(ROOT.parent/'lesson-assets/fonts'/f'SourceSans3-{style}.ttf')
plt.rcParams.update({'font.family':'Source Sans 3','font.size':13,'svg.fonttype':'path','svg.hashsalt':'kinematics-1','axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
G='#176b55';O='#b44826';B='#285dac';INK='#202722'
def base(size):
 f,a=plt.subplots(figsize=size);a.set_aspect('equal');a.axis('off');return f,a
def arrow(a,p,q,c=G,lw=2.5):a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',lw=lw,color=c,shrinkA=0,shrinkB=0))
def save(f,name):
 f.savefig(OUT/(name+'.svg'),bbox_inches='tight',pad_inches=.22,metadata={'Date':None});plt.close(f)
f,a=base((7,4.6))
pts=np.array([[0,0],[40,0],[40,30],[80,30],[80,60]])
for p,q in zip(pts[:-1],pts[1:]):arrow(a,p,q,O)
arrow(a,(0,0),(80,60));a.scatter([0,80],[0,60],s=45,color=INK,zorder=5)
for x,y,t in [(20,-7,'40 m'),(48,13,'30 m'),(60,24,'40 m'),(87,43,'30 m')]:a.text(x,y,t,color=O,ha='center')
a.text(-5,-2,'A',ha='right',weight='bold');a.text(81,65,'B',weight='bold');a.text(26,30,'100 m directly',rotation=36.87,color=G,rotation_mode='anchor');a.text(-8,70,'Delivery depot → customer',size=14,weight='bold');arrow(a,(-9,45),(-9,59),INK,1.5);a.text(-9,62,'N',ha='center',size=11);a.set_xlim(-16,103);a.set_ylim(-13,76);save(f,'delivery-route-mpl')
f,a=base((7,3.4));a.add_patch(Rectangle((0,-5),50,21,facecolor='white',edgecolor='#7e9eb0',lw=1.8))
for y in [-1,5,11]:a.plot([0,50],[y,y],color='#dbe8ed',lw=1)
arrow(a,(1,11),(49,11),O);arrow(a,(49,5),(30,5),O);arrow(a,(0,-13),(30,-13),G)
a.text(25,18,'50 m pool',ha='center',weight='bold');a.text(25,12.5,'50 m out',ha='center',color=O);a.text(40,6.5,'20 m back',ha='center',color=O);a.scatter([0,30],[-2,-2],color=INK,s=25);a.text(0,-8,'Start',ha='center');a.text(30,-8,'Finish',ha='center');a.text(15,-18,'Displacement: 30 m towards the far end',ha='center',color=G,size=12);a.set_xlim(-6,57);a.set_ylim(-22,22);save(f,'swimmer-mpl')
f,a=base((5,4.4));t=np.linspace(0,2*np.pi,300);a.plot(np.cos(t),np.sin(t),color='#81978a',lw=2)
arrow(a,(0,1),(.75,1),G);arrow(a,(1,0),(1,-.75),B);a.scatter([0,1],[1,0],color=[G,B],s=45,zorder=4);a.text(-.25,1.22,'5 m/s east',color=G);a.text(1.15,-.32,'5 m/s\nsouth',color=B,va='center');a.text(-.95,-1.3,'One complete lap: 400 m',size=12);a.text(-.65,-.1,'Same speed.\nChanging direction.',size=12,ha='left');a.set_xlim(-1.25,2.2);a.set_ylim(-1.45,1.5);save(f,'track-velocity-mpl')
f,a=base((6,5.3));arrow(a,(0,0),(90,0),O);arrow(a,(90,0),(90,120),O);arrow(a,(0,0),(90,120),G);a.add_patch(Arc((0,0),42,42,theta1=0,theta2=53.1301,color=G,lw=1.3));a.plot([84,84,90],[0,6,6],color='#8a978e',lw=1)
a.text(45,-12,'90 m east',ha='center',color=O);a.text(99,60,'120 m\nnorth',color=O,va='center');a.text(25,65,'150 m',color=G,rotation=53.13);a.text(23,12,'53.1°',color=G);a.text(-8,-3,'A');a.text(91,-10,'B');a.text(94,123,'C');a.set_xlim(-15,143);a.set_ylim(-20,140);save(f,'robot-resultant-mpl')
assert np.isclose(np.linalg.norm(pts[-1]-pts[0]),100)
assert sum(np.linalg.norm(q-p) for p,q in zip(pts[:-1],pts[1:]))==140
assert np.isclose(np.hypot(90,120),150)
print('4 SVG figures generated; route lengths and resultant checked.')
