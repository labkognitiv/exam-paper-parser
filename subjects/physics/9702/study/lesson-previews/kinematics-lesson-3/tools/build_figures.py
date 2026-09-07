"""Exact motion graphs for Lesson 3. Run with Matplotlib 3.9.4.
Green displacement; blue velocity; grey axes and reading guides.
Only the context cart body has a sketch filter. All data marks stay exact.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch,Circle
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'assets/diagrams'
for style in ('Regular','Semibold','Bold'):
 font_manager.fontManager.addfont(ROOT.parent/'lesson-assets/fonts'/f'SourceSans3-{style}.ttf')
plt.rcParams.update({'font.family':'Source Sans 3','font.size':13,'svg.fonttype':'path','svg.hashsalt':'kinematics-3','axes.unicode_minus':True})
INK='#202722';GREEN='#176b55';BLUE='#285dac';GREY='#738379';GRID='#e3e8e4'
MOBILE=False
JOURNEY_T=np.array([0,2,5,7,10]);JOURNEY_S=np.array([-4,0,6,6,2])
ROBOT_T=np.array([0,3,5,7,9,12]);ROBOT_V=np.array([4,4,0,0,-3,-3])
SENSOR_T=np.array([1,3,4,6]);SENSOR_V=np.array([.8,.2,0,-.6])

def graph(kind,xlim,ylim,xticks,yticks,wide=False):
 f,a=plt.subplots(figsize=((4.7,4.0) if MOBILE else ((8,3.8) if wide else (6.2,4.3))))
 f.subplots_adjust(left=.17 if MOBILE else .14,right=.95,bottom=.18,top=.83)
 a.set(xlim=xlim,ylim=ylim,xticks=xticks,yticks=yticks)
 a.spines['top'].set_visible(False);a.spines['right'].set_visible(False)
 for name in ('left','bottom'):a.spines[name].set_color(GREY);a.spines[name].set_linewidth(1)
 a.spines['bottom'].set_position(('data',0));a.spines['left'].set_position(('data',0))
 a.tick_params(axis='both',colors=INK,labelsize=13 if MOBILE else 12,pad=7,length=4)
 # Horizontal labels stay below the complete graph; a grey zero line is the time axis.
 a.set_xlabel('Time / s',loc='right',labelpad=12,color=INK)
 a.xaxis.set_label_coords(1,-.15)
 title='Displacement / m' if kind=='s' else 'Velocity / m s⁻¹'
 a.set_title(title,loc='left',color=GREEN if kind=='s' else BLUE,fontweight='semibold',fontsize=15,pad=16)
 a.grid(True,color=GRID,lw=.8);a.set_axisbelow(True)
 return f,a

def trace(a,t,q,colour):
 line,=a.plot(t,q,color=colour,lw=2.7,solid_capstyle='round',zorder=3)
 assert line.get_sketch_params() is None
 return line

def save(f,name):
 OUT.mkdir(exist_ok=True)
 f.savefig(OUT/(name+('-mobile' if MOBILE else '')+'.svg'),bbox_inches='tight',pad_inches=.18,facecolor='white',metadata={'Date':None})
 plt.close(f)

def horizontal_s():
 f,a=graph('s',(0,8.5),(0,8),[0,2,4,6,8],[0,2,4,6,8]);trace(a,[0,8],[6,6],GREEN);save(f,'horizontal-displacement')
def horizontal_v():
 f,a=graph('v',(0,8.5),(0,6),[0,2,4,6,8],[0,2,4,6]);trace(a,[0,8],[4,4],BLUE);save(f,'horizontal-velocity')
def coordinate():
 f,a=graph('s',(0,8.5),(0,18),[0,2,4,6,8],[0,4,8,12,16]);trace(a,[0,8],[0,16],GREEN)
 a.plot([6,6,0],[0,12,12],color=GREY,ls=(0,(3,3)),lw=1.5,zorder=2);a.scatter([6],[12],s=65,c=GREEN,zorder=4)
 save(f,'reading-a-coordinate')
def reference():
 f,a=plt.subplots(figsize=(4.7,2.8) if MOBILE else (7,3.1));a.axis('off');a.set(xlim=(-6,4.8),ylim=(.05,3.2))
 a.plot([-5.5,4.5],[1,1],c=GREY,lw=1.5)
 for x in (-4,-2,0,2,4):
  a.plot([x,x],[.9,1.1],c=GREY,lw=1)
  a.text(x,.65,f'{x:+}' if x else '0',ha='center',va='top',color=GREEN)
 a.text(4.5,.08,'Displacement / m',ha='right',color=GREEN)
 body=FancyBboxPatch((-4.5,1.2),1,.45,boxstyle='round,pad=0,rounding_size=.06',ec=INK,fc='white',lw=1.5);body.set_sketch_params(.55,60,2);a.add_patch(body)
 for x in (-4.3,-3.7):a.add_patch(Circle((x,1.13),.1,ec=INK,fc='white',lw=1.3))
 a.annotate('',xy=(-1.2,2),xytext=(-4.2,2),arrowprops={'arrowstyle':'->','color':BLUE,'lw':2.4,'shrinkA':0,'shrinkB':0})
 a.text(-4.4,2.3,'v = +2 m s⁻¹',color=BLUE)
 a.plot([0,0],[1.1,1.8],color=INK,lw=2);a.text(.15,2,'Reference\npoint',color=INK,ha='left')
 a.text(4.5,2.8,'Positive →',ha='right',color=GREY)
 save(f,'side-and-direction')
def displacement():
 f,a=graph('s',(0,10.5),(-5.5,8),[0,2,5,7,10],[-4,0,2,6]);trace(a,JOURNEY_T,JOURNEY_S,GREEN);a.scatter(JOURNEY_T,JOURNEY_S,c=GREEN,s=28,zorder=4)
 save(f,'trolley-displacement')
def crossing():
 f,a=graph('v',(0,4.3),(-2.8,2.8),[0,1,2,3,4],[-2,0,2]);trace(a,[0,2,4],[2,0,-2],BLUE);a.scatter([2],[0],s=40,c=BLUE,zorder=4);save(f,'velocity-crosses-zero')
def touching():
 f,a=graph('v',(0,4.3),(-2.8,2.8),[0,1,2,3,4],[-2,0,2]);t=np.linspace(0,4,121);trace(a,t,.5*(t-2)**2,BLUE);a.scatter([2],[0],s=40,c=BLUE,zorder=4);save(f,'velocity-touches-zero')
def robot():
 f,a=graph('v',(0,12.5),(-4.5,5.5),[0,2,3,5,7,9,10,12],[-3,0,4],wide=True)
 if MOBILE:a.set_xticks([0,3,5,7,9,12])
 trace(a,ROBOT_T,ROBOT_V,BLUE);a.scatter(ROBOT_T,ROBOT_V,c=BLUE,s=28,zorder=4)
 save(f,'robot-velocity')
def sensor():
 f,a=graph('v',(0,6.5),(-.85,1),[0,1,3,4,6],[-.6,0,.2,.8]);a.scatter(SENSOR_T,SENSOR_V,c=BLUE,s=52,zorder=4)
 save(f,'sensor-readings')

DRAWINGS=(horizontal_s,horizontal_v,coordinate,reference,displacement,crossing,touching,robot,sensor)
if __name__=='__main__':
 for MOBILE in (False,True):
  plt.rcParams['font.size']=14 if MOBILE else 13
  for draw in DRAWINGS:draw()
 assert np.interp(6,[0,8],[0,16])==12
 assert np.interp(2,JOURNEY_T,JOURNEY_S)==0 and np.interp(10,JOURNEY_T,JOURNEY_S)==2
 assert JOURNEY_S[2]==JOURNEY_S[3]==6 and JOURNEY_T[3]-JOURNEY_T[2]==2
 assert np.interp(2,ROBOT_T,ROBOT_V)==4 and np.interp(10,ROBOT_T,ROBOT_V)==-3
 assert ROBOT_V[2]==ROBOT_V[3]==0 and ROBOT_T[3]-ROBOT_T[2]==2
 assert (.5*(1-2)**2)>0 and (.5*(3-2)**2)>0
 assert SENSOR_V[1]>0 and SENSOR_V[-1]<0 and SENSOR_V[2]==0
 print('18 SVGs generated; coordinates, durations, signs and reversal cases checked.')
