import json,math,sys,urllib.request as U
from datetime import datetime,timedelta,timezone,date
N="saumil-codes";A="https://alfa-leetcode-api.onrender.com";WK=62
T={"Easy":960,"Medium":2103,"Hard":966}
Z,G,P,Y=12,3,34,262;S=Z+G;M=18
L=["#2B313A","#0E4429","#006D32","#26A641","#39D353"]
def g(p):
 r=U.Request(f"{A}/{N}/{p}",headers={"User-Agent":"card"})
 return json.load(U.urlopen(r,timeout=30))
def v(n):return 0 if n<=0 else 1 if n<=2 else 2 if n<=5 else 3 if n<=9 else 4
try:s,c=g("solved"),g("calendar")
except Exception as e:print("fetch failed:",e,file=sys.stderr);sys.exit(1)
K=("Easy","Medium","Hard");C={k:s[k[0].lower()+k[1:]+"Solved"] for k in K}
tot=s["solvedProblem"]
sb=next(d["submissions"] for d in s["totalSubmissionNum"] if d["difficulty"]=="All")
ac=next(d["submissions"] for d in s["acSubmissionNum"] if d["difficulty"]=="All")
rt=round(100*ac/sb,1) if sb else 0
st,ad=c.get("streak",0),c.get("totalActiveDays",0)
D={datetime.fromtimestamp(int(k),timezone.utc).date():x for k,x in json.loads(c["submissionCalendar"]).items()}
td=datetime.now(timezone.utc).date();bg=td-timedelta(weeks=WK)
cl=mo="";x=P
y0,m0=bg.year,bg.month
while (y0,m0)<=(td.year,td.month):
 f=max(date(y0,m0,1),bg)
 ny,nm=(y0+1,1) if m0==12 else (y0,m0+1)
 e=min(date(ny,nm,1)-timedelta(days=1),td)
 col=0;d=f
 while d<=e:
  w=(d.weekday()+1)%7
  if d>f and w==0:col+=1
  cl+=f'<rect x="{x+col*S}" y="{Y+w*S}" width="{Z}" height="{Z}" rx="2" fill="{L[v(D.get(d,0))]}"/>'
  d+=timedelta(days=1)
 bw=(col+1)*S-G
 mo+=f'<text x="{x+bw/2:.0f}" y="{Y+7*S+14}" text-anchor="middle" fill="#8B949E" font-size="11" font-weight="600">{f.strftime("%b")}</text>'
 x+=bw+M;y0,m0=ny,nm
gw=x-M-P;W=P+gw+P;bx=250;b2=W-bx-P;R=58;CC=2*math.pi*R
ar="";o=0
for i,k in enumerate(K):
 sg=CC*C[k]/tot if tot else 0
 ar+=f'<circle r="{R}" fill="none" stroke="url(#g{i})" stroke-width="14" stroke-dasharray="{max(sg-3,0):.1f} {CC-sg+3:.1f}" stroke-dashoffset="{-o:.1f}" stroke-linecap="round"/>';o+=sg
rw=""
for i,k in enumerate(K):
 yy=104+i*44;fw=max(7,b2*C[k]/T[k])
 rw+=(f'<text x="{bx}" y="{yy}" fill="#AEB6C4" font-size="14" font-weight="600">{k}</text>'
 f'<text x="{W-P}" y="{yy}" text-anchor="end" font-size="14"><tspan fill="#FFF" font-weight="700">{C[k]}</tspan><tspan fill="#59616F"> / {T[k]}</tspan></text>'
 f'<rect x="{bx}" y="{yy+9}" width="{b2}" height="7" rx="3.5" fill="#222834"/><rect x="{bx}" y="{yy+9}" width="{fw:.1f}" height="7" rx="3.5" fill="url(#g{i})"/>')
q=lambda i,a,b:f'<linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
H=Y+7*S+34
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI,Helvetica,Arial,sans-serif">'
f'<defs>{q(0,"#00E5C9","#00B8A3")}{q(1,"#FFCE4F","#FFB800")}{q(2,"#FF7A70","#EF4743")}'
f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#141922"/><stop offset="1" stop-color="#0B0E13"/></linearGradient>'
f'<linearGradient id="hr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFA116" stop-opacity="0"/><stop offset=".45" stop-color="#FFA116" stop-opacity=".85"/><stop offset="1" stop-color="#FFA116" stop-opacity="0"/></linearGradient>'
f'<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/><rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="15.25" fill="none" stroke="#222A37" stroke-width="1.5"/>'
f'<text x="{P}" y="42" fill="#FFF" font-size="20" font-weight="700">{N}</text>'
f'<text x="{W-P}" y="42" text-anchor="end" fill="#FFA116" font-size="13" font-weight="700" letter-spacing="2">LEETCODE</text>'
f'<rect x="{P}" y="58" width="{W-2*P}" height="1.5" fill="url(#hr)"/>'
f'<g transform="translate({P+82},152)"><circle r="{R}" fill="none" stroke="#1B222C" stroke-width="14"/>'
f'<g transform="rotate(-90)" filter="url(#gl)">{ar}</g>'
f'<text y="6" text-anchor="middle" fill="#FFF" font-size="40" font-weight="700">{tot}</text>'
f'<text y="28" text-anchor="middle" fill="#69727F" font-size="11" font-weight="600" letter-spacing="1.6">SOLVED</text></g>{rw}'
f'<text x="{P}" y="{Y-16}" font-size="13"><tspan fill="#FFF" font-weight="700">{sb}</tspan><tspan fill="#8B949E"> submissions in the past {WK} weeks</tspan></text>'
f'<text x="{W-P}" y="{Y-16}" text-anchor="end" font-size="13"><tspan fill="#39D353" font-weight="700">{st}</tspan><tspan fill="#8B949E"> max streak &#183; </tspan>'
f'<tspan fill="#FFF" font-weight="700">{ad}</tspan><tspan fill="#8B949E"> active days &#183; </tspan>'
f'<tspan fill="#00E5C9" font-weight="700">{rt}%</tspan><tspan fill="#8B949E"> acceptance</tspan></text>'
f'{cl}{mo}</svg>')
open("leetcode.svg","w").write(svg)
print("rendered",tot,"solved,",st,"streak")

