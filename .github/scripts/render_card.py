import json,math,sys,urllib.request as U
from datetime import datetime,timedelta,timezone
USER="saumil-codes";API="https://alfa-leetcode-api.onrender.com";WEEKS=62
TOT={"Easy":960,"Medium":2103,"Hard":966}
CS,GAP,HX,HY=11,3,34,266;ST=CS+GAP;GX=HX+26
LV=["#161B22","#0E4429","#006D32","#26A641","#39D353"]
def get(p):
 r=U.Request(f"{API}/{USER}/{p}",headers={"User-Agent":"card"})
 return json.load(U.urlopen(r,timeout=30))
def lvl(n):return 0 if n<=0 else 1 if n<=2 else 2 if n<=5 else 3 if n<=9 else 4
try:s,c=get("solved"),get("calendar")
except Exception as e:print("fetch failed:",e,file=sys.stderr);sys.exit(0)
K=("Easy","Medium","Hard");CT={"Easy":s["easySolved"],"Medium":s["mediumSolved"],"Hard":s["hardSolved"]}
tot=s["solvedProblem"]
sub=next(d["submissions"] for d in s["totalSubmissionNum"] if d["difficulty"]=="All")
ac=next(d["submissions"] for d in s["acSubmissionNum"] if d["difficulty"]=="All")
rate=round(100*ac/sub,1) if sub else 0
stk,act=c.get("streak",0),c.get("totalActiveDays",0)
days={datetime.fromtimestamp(int(k),timezone.utc).date():v for k,v in json.loads(c["submissionCalendar"]).items()}
today=datetime.now(timezone.utc).date()
end=today+timedelta(days=6-((today.weekday()+1)%7));d=end-timedelta(weeks=WEEKS,days=6)
cells=mon=sep="";col=0;lastm=None
while d<=end:
 for r in range(7):
  cur=d+timedelta(days=r);n=days.get(cur,0)
  if cur<=today and n:cells+=f'<rect x="{GX+col*ST}" y="{HY+r*ST}" width="{CS}" height="{CS}" rx="2.5" fill="{LV[lvl(n)]}"/>'
 m=(d+timedelta(days=6)).month
 if m!=lastm:
  if lastm is not None and col:sep+=f'<rect x="{GX+col*ST-GAP-1}" y="{HY-4}" width="1" height="{7*ST-GAP+8}" fill="#20262F"/>'
  mon+=f'<text x="{GX+col*ST}" y="{HY-11}" fill="#7D8694" font-size="10" font-weight="700" letter-spacing=".4">{(d+timedelta(days=6)).strftime("%b")}</text>'
  lastm=m
 d+=timedelta(days=7);col+=1
gw=col*ST-GAP;W=GX+gw+HX;bx=250;bw=W-bx-HX;R=58;C=2*math.pi*R
dow="".join(f'<text x="{HX+18}" y="{HY+i*ST+9}" text-anchor="end" fill="#5A6472" font-size="9" font-weight="600">{t}</text>' for i,t in ((1,"Mon"),(3,"Wed"),(5,"Fri")))
lg="".join(f'<rect x="{W-HX-92+i*15}" y="{HY+7*ST+10}" width="{CS}" height="{CS}" rx="2.5" fill="{co}"/>' for i,co in enumerate(LV))
leg=(f'<text x="{W-HX-100}" y="{HY+7*ST+20}" text-anchor="end" fill="#5A6472" font-size="10">Less</text>{lg}'
 f'<text x="{W-HX+4}" y="{HY+7*ST+20}" text-anchor="end" fill="#5A6472" font-size="10">More</text>')
H=HY+7*ST+42
arcs="";off=0
for i,k in enumerate(K):
 sg=C*CT[k]/tot if tot else 0
 arcs+=f'<circle r="{R}" fill="none" stroke="url(#g{i})" stroke-width="14" stroke-dasharray="{max(sg-3,0):.1f} {C-sg+3:.1f}" stroke-dashoffset="{-off:.1f}" stroke-linecap="round"/>';off+=sg
rows=""
for i,k in enumerate(K):
 y=104+i*44;fw=max(7,bw*CT[k]/TOT[k])
 rows+=(f'<text x="{bx}" y="{y}" fill="#AEB6C4" font-size="14" font-weight="600">{k}</text>'
 f'<text x="{W-HX}" y="{y}" text-anchor="end" font-size="14"><tspan fill="#FFF" font-weight="700">{CT[k]}</tspan><tspan fill="#59616F"> / {TOT[k]}</tspan></text>'
 f'<rect x="{bx}" y="{y+9}" width="{bw}" height="7" rx="3.5" fill="#222834"/><rect x="{bx}" y="{y+9}" width="{fw:.1f}" height="7" rx="3.5" fill="url(#g{i})"/>')
G=lambda i,a,b:f'<linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI,Helvetica,Arial,sans-serif">'
f'<defs>{G(0,"#00E5C9","#00B8A3")}{G(1,"#FFCE4F","#FFB800")}{G(2,"#FF7A70","#EF4743")}'
f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#141922"/><stop offset="1" stop-color="#0B0E13"/></linearGradient>'
f'<linearGradient id="hr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFA116" stop-opacity="0"/><stop offset=".45" stop-color="#FFA116" stop-opacity=".85"/><stop offset="1" stop-color="#FFA116" stop-opacity="0"/></linearGradient>'
f'<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
f'<pattern id="em" x="{GX}" y="{HY}" width="{ST}" height="{ST}" patternUnits="userSpaceOnUse"><rect width="{CS}" height="{CS}" rx="2.5" fill="{LV[0]}"/></pattern></defs>'
f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/><rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="15.25" fill="none" stroke="#222A37" stroke-width="1.5"/>'
f'<text x="{HX}" y="42" fill="#FFF" font-size="20" font-weight="700">{USER}</text>'
f'<text x="{W-HX}" y="42" text-anchor="end" fill="#FFA116" font-size="13" font-weight="700" letter-spacing="2">LEETCODE</text>'
f'<rect x="{HX}" y="58" width="{W-2*HX}" height="1.5" fill="url(#hr)"/>'
f'<g transform="translate({HX+82},152)"><circle r="{R}" fill="none" stroke="#1B222C" stroke-width="14"/>'
f'<g transform="rotate(-90)" filter="url(#gl)">{arcs}</g>'
f'<text y="6" text-anchor="middle" fill="#FFF" font-size="40" font-weight="700">{tot}</text>'
f'<text y="28" text-anchor="middle" fill="#69727F" font-size="11" font-weight="600" letter-spacing="1.6">SOLVED</text></g>{rows}'
f'<text x="{HX}" y="{HY-36}" fill="#AEB6C4" font-size="13" font-weight="600">Submission activity &#183; last {WEEKS} weeks</text>'
f'<text x="{W-HX}" y="{HY-36}" text-anchor="end" font-size="13"><tspan fill="#39D353" font-weight="700">{stk}</tspan><tspan fill="#69727F"> day streak &#183; </tspan>'
f'<tspan fill="#FFF" font-weight="700">{act}</tspan><tspan fill="#69727F"> active days &#183; </tspan>'
f'<tspan fill="#00E5C9" font-weight="700">{rate}%</tspan><tspan fill="#69727F"> acceptance</tspan></text>'
f'{mon}{dow}<rect x="{GX}" y="{HY}" width="{gw}" height="{7*ST-GAP}" fill="url(#em)"/>{sep}{cells}{leg}</svg>')
open("leetcode.svg","w").write(svg)
print("rendered",tot,"solved,",stk,"day streak")
import json,math,sys,urllib.request as U
from datetime import datetime,timedelta,timezone
USER="saumil-codes";API="https://alfa-leetcode-api.onrender.com"
TOT={"Easy":960,"Medium":2103,"Hard":966}
CS,GAP,HX,HY=11,3,34,258;ST=CS+GAP
LV=["#182029","#0E4429","#006D32","#26A641","#39D353"]
def get(p):
 r=U.Request(f"{API}/{USER}/{p}",headers={"User-Agent":"card"})
 return json.load(U.urlopen(r,timeout=30))
def lvl(n):return 0 if n<=0 else 1 if n<=2 else 2 if n<=5 else 3 if n<=9 else 4
try:s,c=get("solved"),get("calendar")
except Exception as e:print("fetch failed:",e,file=sys.stderr);sys.exit(0)
K=("Easy","Medium","Hard");CT={"Easy":s["easySolved"],"Medium":s["mediumSolved"],"Hard":s["hardSolved"]}
tot=s["solvedProblem"]
sub=next(d["submissions"] for d in s["totalSubmissionNum"] if d["difficulty"]=="All")
ac=next(d["submissions"] for d in s["acSubmissionNum"] if d["difficulty"]=="All")
rate=round(100*ac/sub,1) if sub else 0
stk,act=c.get("streak",0),c.get("totalActiveDays",0)
days={datetime.fromtimestamp(int(k),timezone.utc).date():v for k,v in json.loads(c["submissionCalendar"]).items()}
today=datetime.now(timezone.utc).date()
end=today+timedelta(days=6-((today.weekday()+1)%7));d=end-timedelta(weeks=52,days=6)
cells=mon="";seen=set();col=0
while d<=end:
 for r in range(7):
  cur=d+timedelta(days=r);n=days.get(cur,0)
  if cur<=today and n:cells+=f'<rect x="{HX+col*ST}" y="{HY+r*ST}" width="{CS}" height="{CS}" rx="2.5" fill="{LV[lvl(n)]}"/>'
 if d.month not in seen and d.day<=7:
  seen.add(d.month);mon+=f'<text x="{HX+col*ST}" y="{HY-10}" fill="#5A6472" font-size="10" font-weight="600">{d.strftime("%b")}</text>'
 d+=timedelta(days=7);col+=1
gw=col*ST-GAP;W=gw+2*HX;H=HY+7*ST+34;bx=250;bw=W-bx-HX;R=58;C=2*math.pi*R
arcs="";off=0
for i,k in enumerate(K):
 sg=C*CT[k]/tot if tot else 0
 arcs+=f'<circle r="{R}" fill="none" stroke="url(#g{i})" stroke-width="14" stroke-dasharray="{max(sg-3,0):.1f} {C-sg+3:.1f}" stroke-dashoffset="{-off:.1f}" stroke-linecap="round"/>';off+=sg
rows=""
for i,k in enumerate(K):
 y=104+i*44;fw=max(7,bw*CT[k]/TOT[k])
 rows+=(f'<text x="{bx}" y="{y}" fill="#AEB6C4" font-size="14" font-weight="600">{k}</text>'
 f'<text x="{W-HX}" y="{y}" text-anchor="end" font-size="14"><tspan fill="#FFF" font-weight="700">{CT[k]}</tspan><tspan fill="#59616F"> / {TOT[k]}</tspan></text>'
 f'<rect x="{bx}" y="{y+9}" width="{bw}" height="7" rx="3.5" fill="#222834"/><rect x="{bx}" y="{y+9}" width="{fw:.1f}" height="7" rx="3.5" fill="url(#g{i})"/>')
G=lambda i,a,b:f'<linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI,Helvetica,Arial,sans-serif">'
f'<defs>{G(0,"#00E5C9","#00B8A3")}{G(1,"#FFCE4F","#FFB800")}{G(2,"#FF7A70","#EF4743")}'
f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#141922"/><stop offset="1" stop-color="#0B0E13"/></linearGradient>'
f'<linearGradient id="hr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFA116" stop-opacity="0"/><stop offset=".45" stop-color="#FFA116" stop-opacity=".85"/><stop offset="1" stop-color="#FFA116" stop-opacity="0"/></linearGradient>'
f'<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
f'<pattern id="em" x="{HX}" y="{HY}" width="{ST}" height="{ST}" patternUnits="userSpaceOnUse"><rect width="{CS}" height="{CS}" rx="2.5" fill="{LV[0]}"/></pattern></defs>'
f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/><rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="15.25" fill="none" stroke="#222A37" stroke-width="1.5"/>'
f'<text x="{HX}" y="42" fill="#FFF" font-size="20" font-weight="700">{USER}</text>'
f'<text x="{W-HX}" y="42" text-anchor="end" fill="#FFA116" font-size="13" font-weight="700" letter-spacing="2">LEETCODE</text>'
f'<rect x="{HX}" y="58" width="{W-2*HX}" height="1.5" fill="url(#hr)"/>'
f'<g transform="translate({HX+82},152)"><circle r="{R}" fill="none" stroke="#1B222C" stroke-width="14"/>'
f'<g transform="rotate(-90)" filter="url(#gl)">{arcs}</g>'
f'<text y="6" text-anchor="middle" fill="#FFF" font-size="40" font-weight="700">{tot}</text>'
f'<text y="28" text-anchor="middle" fill="#69727F" font-size="11" font-weight="600" letter-spacing="1.6">SOLVED</text></g>{rows}'
f'<text x="{HX}" y="{HY-30}" fill="#AEB6C4" font-size="13" font-weight="600">Last 52 weeks</text>'
f'<text x="{W-HX}" y="{HY-30}" text-anchor="end" font-size="13"><tspan fill="#39D353" font-weight="700">{stk}</tspan><tspan fill="#69727F"> day streak &#183; </tspan>'
f'<tspan fill="#FFF" font-weight="700">{act}</tspan><tspan fill="#69727F"> active days &#183; </tspan>'
f'<tspan fill="#00E5C9" font-weight="700">{rate}%</tspan><tspan fill="#69727F"> acceptance</tspan></text>'
f'{mon}<rect x="{HX}" y="{HY}" width="{gw}" height="{7*ST-GAP}" fill="url(#em)"/>{cells}</svg>')
open("leetcode.svg","w").write(svg)
print("rendered",tot,"solved,",stk,"day streak")
