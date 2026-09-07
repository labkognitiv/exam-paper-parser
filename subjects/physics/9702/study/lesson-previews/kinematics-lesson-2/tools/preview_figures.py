"""Render inspection sheets and detect overlapping labels without changing SVGs."""
from pathlib import Path
import io
from PIL import Image,ImageDraw
import build_figures as m
OUT=Path(__file__).resolve().parents[1]/'visual-audit-verification'
OUT.mkdir(exist_ok=True)
for mobile in (False,True):
 images=[]
 def capture(f,name):
  f.canvas.draw();renderer=f.canvas.get_renderer()
  texts=[t for ax in f.axes for t in ax.texts if t.get_text()]
  for i,t in enumerate(texts):
   for other in texts[i+1:]:
    b=t.get_window_extent(renderer);c=other.get_window_extent(renderer)
    assert not (min(b.x1,c.x1)-max(b.x0,c.x0)>1 and min(b.y1,c.y1)-max(b.y0,c.y0)>1),(name,t.get_text(),other.get_text())
  buf=io.BytesIO();f.savefig(buf,format='png',dpi=120,bbox_inches='tight',pad_inches=.12);m.plt.close(f)
  im=Image.open(buf).convert('RGB');im.thumbnail((480,440));images.append((name,im))
 m.save=capture;m.MOBILE=mobile;m.plt.rcParams['font.size']=14 if mobile else 13
 for draw in (m.snapshots,m.braking,m.robot,m.rebound,m.gates,m.times,m.lift,m.positions,m.track):draw()
 canvas=Image.new('RGB',(1500,1470),'white');d=ImageDraw.Draw(canvas)
 for i,(name,im) in enumerate(images):
  x=(i%3)*500;y=(i//3)*490;d.text((x+10,y+8),name,fill='black');canvas.paste(im,(x+10,y+30))
 canvas.save(OUT/('mobile-diagrams.png' if mobile else 'desktop-diagrams.png'))
print('18 figures checked: no overlapping text labels. Two inspection sheets saved.')
