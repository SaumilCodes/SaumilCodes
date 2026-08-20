import json,math,sys,time,urllib.request as U
from datetime import datetime,timedelta,timezone
USER="saumil-codes";WEEKS=62
CS,GAP,HX,HY=12,3,34,262;ST=CS+GAP
LV=["#161B22","#0E4429","#006D32","#26A641","#39D353"]
GQL="""query($u:String!){
 allQuestionsCount{difficulty count}
 matchedUser(username:$u){
  submitStats{acSubmissionNum{difficulty count} totalSubmissionNum{difficulty submissions}}
  userCalendar{streak totalActiveDays submissionCalendar}}}"""
def post(url,body,hdr):
 r=U.Request(url,data=json.dumps(body).encode(),headers=hdr)
 return json.load(U.urlopen(r,timeout=30))
def fetch():
 h={"Content-Type":"application/json","Referer":f"https://leetcode.com/u/{USER}/",
    "User-Agent":"Mozilla/5.0 (compatible; profile-card/1.0)","Origin":"https://leetcode.com"}
 d=post("https://leetcode.com/graphql",{"query":GQL,"variables":{"u":USER}},h)
 m=d["data"]["matchedUser"]
 if not m: raise RuntimeError("user not found")
 tot={q["difficulty"]:q["count"] for q in d["data"]["allQuestionsCount"]}
 ac={q["difficulty"]:q["count"] for q in m["submitStats"]["acSubmissionNum"]}
 sb={q["difficulty"]:q["submissions"] for q in m["submitStats"]["totalSubmissionNum"]}
 cal=m["userCalendar"]
 return (
  {k:ac[k] for k in ("Easy","Medium","Hard")}, ac["All"],
  {k:tot[k] for k in ("Easy","Medium","Hard")}, sb["All"],
  cal["streak"] or 0, cal["totalActiveDays"] or 0, json.loads(cal["submissionCalendar"]))
err=None
for attempt in range(3):
 try:
  CT,tot,TOT,sub,stk,act,cal=fetch();err=None;break
 except Exception as e:
  err=e;print(f"attempt {attempt+1} failed: {e}",file=sys.stderr);time.sleep(5*(attempt+1))
if err: print("ERROR: could not fetch LeetCode data",file=sys.stderr);sys.exit(1)
def lvl(n):return 0 if n<=0 else 1 if n<=2 else 2 if n<=5 else 3 if n<=9 else 4
rate=round(100*tot/sub,1) if sub else 0
days={datetime.fromtimestamp(int(k),timezone.utc).date():v for k,v in cal.items()}
K=("Easy","Medium","Hard")
today=datetime.now(timezone.utc).date()
end=today+timedelta(days=6-((today.weekday()+1)%7));d=end-timedelta(weeks=WEEKS,days=6)
MGAP=8
cells=mon="";x=HX;lastm=None;mstart=HX;first=True
while d<=end:
 m=(d+timedelta(days=6)).month
 if m!=lastm:
  if not first:
   mon+=f'<text x="{(mstart+x-MGAP-CS)/2+CS/2:.0f}" y="{HY+7*ST+14}" text-anchor="middle" fill="#8B949E" font-size="11" font-weight="600">{lastn}</text>'
   x+=MGAP
  mstart=x;first=False;lastm=m;lastn=(d+timedelta(days=6)).strftime("%b")
 for r in range(7):
  cur=d+timedelta(days=r);n=days.get(cur,0)
  if cur<=today:cells+=f'<rect x="{x}" y="{HY+r*ST}" width="{CS}" height="{CS}" rx="2" fill="{LV[lvl(n)]}"/>'
 d+=timedelta(days=7);x+=ST
mon+=f'<text x="{(mstart+x-CS)/2+CS/2:.0f}" y="{HY+7*ST+14}" text-anchor="middle" fill="#8B949E" font-size="11" font-weight="600">{lastn}</text>'
gw=x-GAP-HX;W=HX+gw+HX;bx=250;bw=W-bx-HX;R=58;C=2*math.pi*R
dow=""
lg=""
leg=''
H=HY+7*ST+34
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
f'</defs>'
f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/><rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="15.25" fill="none" stroke="#222A37" stroke-width="1.5"/>'
f'<text x="{HX}" y="42" fill="#FFF" font-size="20" font-weight="700">{USER}</text>'
f'<text x="{W-HX}" y="42" text-anchor="end" fill="#FFA116" font-size="13" font-weight="700" letter-spacing="2">LEETCODE</text>'
f'<rect x="{HX}" y="58" width="{W-2*HX}" height="1.5" fill="url(#hr)"/>'
f'<g transform="translate({HX+82},152)"><circle r="{R}" fill="none" stroke="#1B222C" stroke-width="14"/>'
f'<g transform="rotate(-90)" filter="url(#gl)">{arcs}</g>'
f'<text y="6" text-anchor="middle" fill="#FFF" font-size="40" font-weight="700">{tot}</text>'
f'<text y="28" text-anchor="middle" fill="#69727F" font-size="11" font-weight="600" letter-spacing="1.6">SOLVED</text></g>{rows}'
f'<text x="{HX}" y="{HY-16}" font-size="13"><tspan fill="#FFF" font-weight="700">{sub}</tspan><tspan fill="#8B949E"> submissions in the past {WEEKS} weeks</tspan></text>'
f'<text x="{W-HX}" y="{HY-16}" text-anchor="end" font-size="13"><tspan fill="#39D353" font-weight="700">{stk}</tspan><tspan fill="#8B949E"> max streak &#183; </tspan>'
f'<tspan fill="#FFF" font-weight="700">{act}</tspan><tspan fill="#8B949E"> active days &#183; </tspan>'
f'<tspan fill="#00E5C9" font-weight="700">{rate}%</tspan><tspan fill="#8B949E"> acceptance</tspan></text>'
f'{cells}{mon}</svg>')
open("leetcode.svg","w").write(svg)
print("rendered",tot,"solved,",stk,"day streak")
