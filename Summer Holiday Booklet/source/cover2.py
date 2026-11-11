import numpy as np, sys
from PIL import Image
def hexc(h): h=h.lstrip('#'); return [int(h[i:i+2],16) for i in (0,2,4)]
def pal(stops):
    pos=[p for p,_ in stops]; cols=np.array([hexc(c) for _,c in stops],float)
    return lambda t: np.stack([np.interp(t,pos,cols[:,k]) for k in range(3)],-1)
STOPS=[(0,'#ffffff'),(0.18,'#fffbe0'),(0.34,'#E4D00A'),(0.52,'#EAA221'),(0.70,'#CC338B'),(0.86,'#43B3AE'),(1,'#1f6f6c')]
def render(out, c, cx, cy, width, W, H, maxit=500, rot=np.pi/2, ss=2, gamma=0.9, inside='#ffffff'):
    w,h=W*ss,H*ss; hh=width*H/W
    x=np.linspace(-width/2,width/2,w); y=np.linspace(hh/2,-hh/2,h)
    Z=(x[None,:]+1j*y[:,None])*np.exp(1j*rot)+(cx+1j*cy)
    N=np.zeros(Z.shape); alive=np.ones(Z.shape,bool)
    for i in range(maxit):
        Z[alive]=Z[alive]**2+c
        esc=alive&(np.abs(Z)>64)
        N[esc]=i+1-np.log2(np.log(np.abs(Z[esc])))
        alive&=~esc
        if not alive.any(): break
    t=np.where(N>0,np.log1p(N),0)
    lo,hi=np.percentile(t[N>0],2),np.percentile(t[N>0],99.7)
    t=np.clip((t-lo)/(hi-lo),0,1)**gamma
    img=pal(STOPS)(t); img[~(N>0)]=hexc(inside)
    im=Image.fromarray(img.astype(np.uint8))
    if ss>1: im=im.resize((W,H),Image.LANCZOS)
    im.save(out,quality=70,optimize=True,progressive=True)
c=-0.7269+0.1889j
if sys.argv[1]=='try':
    for k,(cx,cy,wd) in enumerate([(0,0,1.45),(0.2,0.25,1.0),(-0.15,-0.2,0.9),(0.32,0.05,0.7)]):
        render(f'try{k}.jpg',c,cx,cy,wd,300,424,400,ss=1)
else:
    cx,cy,wd=map(float,sys.argv[2:5]); render('img/cover.jpg',c,cx,cy,wd,850,1200,600)
