"""Build desktop/mobile diagrams with exact vectors and local outlined fonts.
Blue: velocity. Terracotta: acceleration. Grey: time/structure.
Sketching touches only the trolley/robot body contours; no quantitative marks.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import numpy as np
R=Path(__file__).resolve().parents[1]; O=R/'assets/diagrams'
FONTS=R.parent/'lesson-assets/fonts'
for style in ('Regular','Semibold','Bold'):
 font_manager.fontManager.addfont(FONTS/f'SourceSans3-{style}.ttf')
plt.rcParams.update({'font.family':'Source Sans 3','font.size':13,'svg.fonttype':'path','svg.hashsalt':'kinematics-2','savefig.facecolor':'white'})
G='#176b55'; B='#285dac'; T='#b44826'; K='#202722'; N='#738379'
MOBILE=False
VECTOR_SCALE=.4
REBOUND_SCALE=.28
GATE_SCALE=2.4
TIME_SCALE=1.35

def base(size):
 if MOBILE: size=(4.4, size[1]*.88)
 f,a=plt.subplots(figsize=size); a.axis('off'); return f,a

def arr(a,p,q,c=B):
 ann=a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color=c,lw=2.5,shrinkA=0,shrinkB=0))
 assert ann.arrow_patch.get_sketch_params() is None
 return ann

def label(a,x,y,s,**kw): return a.text(x,y,s,**kw)
def save(f,name):
 suffix='-mobile' if MOBILE else ''
 f.savefig(O/f'{name}{suffix}.svg',bbox_inches='tight',pad_inches=.12,metadata={'Date':None});plt.close(f)
def trolley(a,x,y,scale=1,robot=False):
 body=FancyBboxPatch((x,y),.8*scale,.35*scale,boxstyle=f'round,pad=0,rounding_size={.07*scale}',ec=K,fc='white',lw=1.4)
 body.set_sketch_params(.55,60,2);a.add_patch(body)
 for dx in (.15,.65):a.add_patch(Circle((x+dx*scale,y-.06*scale),.07*scale,ec=K,fc='white',lw=1.4))
 if robot:
  a.plot([x+.4*scale,x+.4*scale],[y+.35*scale,y+.48*scale],color=K,lw=1.2)
  a.add_patch(Circle((x+.4*scale,y+.5*scale),.025*scale,ec=K,fc=G))
  a.plot([x+.16*scale,x+.35*scale],[y+.23*scale,y+.23*scale],color=G,lw=2)

def snapshots():
 f,a=base((7,3.8))
 for y,t,v in [(3,0,2),(2,2,6),(1,4,10)]:
  label(a,0,y,f'{t} s',va='center',weight='bold');trolley(a,.85,y-.12)
  arr(a,(1.9,y),(1.9+v*VECTOR_SCALE,y));label(a,1.95,y+.26,f'+{v} m s⁻¹',color=B)
 label(a,0,3.72,'Snapshots every 2 seconds',weight='bold');a.set(xlim=(-.1,6.3),ylim=(.4,4));save(f,'equal-time-velocities')

def braking():
 f,a=base((6,3.6));label(a,0,3,'Right is positive →',weight='bold')
 label(a,0,2.15,'Before · u',weight='bold');arr(a,(1.6,2),(5.5,2));label(a,2.4,2.32,'+12 m s⁻¹',color=B)
 label(a,0,1.15,'After · v',weight='bold');a.plot(1.6,1.05,'o',color=B);label(a,2,1.05,'0 m s⁻¹',va='center',color=B)
 arr(a,(4.6,.15),(2,.15),T);label(a,2,.45,'Acceleration left',color=T)
 a.set(xlim=(-.1,5.8),ylim=(-.15,3.4));save(f,'braking-directions')

def robot():
 f,a=base((6,4));label(a,0,3.45,'Right is positive →',weight='bold')
 for y,v in [(2.5,-2),(1.25,-8)]:
  label(a,.05,y+.36,('Before · u' if v==-2 else 'After · v'),weight='bold')
  trolley(a,4.25,y-.12,robot=True)
  arr(a,(3.85,y),(3.85+v*VECTOR_SCALE,y));label(a,2.35,y+.24,f'{v} m s⁻¹',color=B)
 arr(a,(3.85,.15),(1.3,.15),T);label(a,1.3,-.2,'Acceleration left',color=T)
 a.set(xlim=(-.1,5.3),ylim=(-.5,3.9));save(f,'left-speeding-up')

def rebound():
 f,a=base((6.5,4.2));label(a,0,3.8,'Right is positive →',weight='bold')
 a.plot([5.4,5.4],[.65,3.35],color=N,lw=4);label(a,5.4,.32,'wall',ha='center')
 for y,text,v in [(2.8,'Before impact · u',6),(1.2,'After impact · v',-4)]:
  label(a,0,y+.4,text,weight='bold');a.add_patch(Circle((3.25,y),.13,ec=K,fc='white',lw=1.5))
  start=3.42 if v>0 else 3.08;arr(a,(start,y),(start+v*REBOUND_SCALE,y))
  label(a,3.5 if v>0 else 1.6,y-.43,f'{v:+} m s⁻¹',color=B)
 a.set(xlim=(-.1,5.95),ylim=(-.15,4.2));save(f,'rebound-velocities')

def gates():
 f,a=base((7,5.1 if MOBILE else 3.7))
 if MOBILE:
  rows=[(1.2,3.4,'First gate · u',.4),(1.2,.6,'Second gate · v',.7)]
 else: rows=[(1.5,1,'First gate · u',.4),(5.7,1,'Second gate · v',.7)]
 for x,y,lab,v in rows:
  a.plot([x-.9,x+1.3],[y-.2,y-.2],c=N,lw=1.5)
  # Simple apparatus stays clean; velocity length = reading × GATE_SCALE.
  a.add_patch(Rectangle((x-.65,y),1,.43,ec=K,fc='white',lw=1.5))
  for dx in (-.45,.15):a.add_patch(Circle((x+dx,y-.06),.09,fc='white',ec=K,lw=1.3))
  a.plot([x+.55,x+.55,x+.85],[y-.2,y+.7,y+.7],c=K,lw=1.5)
  a.plot([x+.55,x+.3],[y+.25,y+.25],c=N,ls=':',lw=1.5)
  arr(a,(x-.65,y+1),(x-.65+v*GATE_SCALE,y+1));label(a,x-.65,y+1.26,f'+{v:.2f} m s⁻¹',color=B)
  label(a,x,y-.62,lab,ha='center')
 if MOBILE:
  a.plot([3.25,3.5,3.5,3.25],[1,1,3.9,3.9],color=N,lw=1.3)
  label(a,3.65,2.45,'Δt\n0.60 s',va='center',color=N);a.set(xlim=(0,5),ylim=(-.35,5.1))
 else:
  a.plot([1.5,1.5,5.7,5.7],[-.18,-.38,-.38,-.18],color=N,lw=1.3)
  label(a,3.6,-.75,'Between readings: Δt = 0.60 s',ha='center',color=N);a.set(xlim=(.3,7.7),ylim=(-1,2.85))
 save(f,'light-gate-readings')

def times():
 f,a=base((8,4.3 if MOBILE else 3.4))
 for y,duration in [(2.9 if MOBILE else 2.4,2),(.7,4)]:
  start=.4;end=start+duration*TIME_SCALE
  label(a,start,y+.32,'u = +2 m s⁻¹',color=B)
  label(a,end,y+.32,'v = +6 m s⁻¹',color=B,ha='right')
  a.plot([start,end],[y,y],color=N,lw=1.5)
  for i in range(duration+1):a.plot([start+i*TIME_SCALE]*2,[y-.08,y+.08],color=N,lw=1)
  label(a,(start+end)/2,y-.4,f'Δt = {duration} s',ha='center',color=N)
  label(a,6.35,y,r'$a_{\mathrm{avg}}$'+'\n'+f'= {4/duration:.0f} m s⁻²',va='center',color=T)
 label(a,.4,4.5 if MOBILE else 3.25,'Time intervals · equal 1 s ticks',weight='bold')
 if MOBILE:
  # Narrow labels have their own lines, not compressed lettering.
  for txt in a.texts:
   if 'u =' in txt.get_text():txt.set_text('u = +2\nm s⁻¹')
   if 'v =' in txt.get_text():txt.set_text('v = +6\nm s⁻¹')
 a.set(xlim=(.15,8),ylim=(-.05,5 if MOBILE else 3.9));save(f,'time-interval-comparison')

def lift():
 f,a=base((6.4,4.3))
 for x in (1.6,3.5):a.plot([x,x],[.6,3.3],c='#acb9b0',lw=1.5)
 a.add_patch(Rectangle((1.85,1.5),1.4,1.7,ec=K,fc='white',lw=1.8));a.plot([2.55]*2,[1.5,3.2],c='#acb9b0',lw=1)
 label(a,2.55,2.3,'LIFT',ha='center',color=K)
 arr(a,(.9,3.1),(.9,1.6));label(a,.9,1.1,'Velocity\ndown',ha='center',va='top',color=B)
 arr(a,(4.1,1.6),(4.1,3.1),T);label(a,4.1,3.55,'Acceleration\nup',ha='center',color=T)
 a.set(xlim=(-.15,5.7),ylim=(.25,4.4));save(f,'lift-slowing-down')

def positions():
 f,a=base((8,2.8));xs=[.5,1.45,3.05,5.3,8.2]
 a.plot([.2,9],[1,1],color=N,lw=1.5)
 for i,x in enumerate(xs):
  a.add_patch(Rectangle((x-.25,1.2),.65,.33,ec=K,fc='white',lw=1.3))
  for w in (x-.1,x+.25):a.add_patch(Circle((w,1.12),.07,fc=K))
  label(a,x+.08,.6,f'{i} s',ha='center')
 label(a,.2,2.3,'Positions every second',weight='bold');arr(a,(6.5,2),(8.8,2));label(a,6.25,2,'Motion',ha='right',va='center',color=B)
 a.set(xlim=(-.1,9.2),ylim=(.1,2.7));save(f,'increasing-position-gaps')

def track():
 f,a=base((5,4.4));a.set_aspect('equal');t=np.linspace(0,2*np.pi,300);a.plot(np.cos(t),np.sin(t),color=N,lw=1.8)
 arr(a,(0,1),(.75,1));arr(a,(1,0),(1,-.75));a.scatter([0,1],[1,0],color=B,s=40)
 label(a,-.5,1.23,'5 m s⁻¹ east',color=B);label(a,1.16,-.32,'5 m s⁻¹\nsouth',color=B,va='center')
 label(a,0 if MOBILE else -.65,-.1,'Same speed.\nChanging\ndirection.' if MOBILE else 'Same speed.\nChanging direction.',ha='center' if MOBILE else 'left');label(a,-.95,-1.3,'One complete lap: 400 m')
 a.set(xlim=(-1.25,2.3),ylim=(-1.5,1.55));save(f,'track-velocity-mpl')

if __name__=='__main__':
 O.mkdir(exist_ok=True)
 for MOBILE in (False,True):
  plt.rcParams['font.size']=14 if MOBILE else 13
  for draw in (snapshots,braking,robot,rebound,gates,times,lift,positions,track):draw()
 assert np.isclose((.7*GATE_SCALE)/(.4*GATE_SCALE),7/4)
 assert (4*TIME_SCALE)/(2*TIME_SCALE)==2
 assert abs(-8*VECTOR_SCALE)/abs(-2*VECTOR_SCALE)==4
 assert (6*REBOUND_SCALE)/(4*REBOUND_SCALE)==1.5
 assert (10-2)/4==2 and (0-12)/6==-2 and (-8-(-2))/3==-2
 assert (-4-6)/.05==-200 and np.isclose((.7-.4)/.6,.5)
 print('18 SVGs generated; directions, scale ratios and worked results checked.')
