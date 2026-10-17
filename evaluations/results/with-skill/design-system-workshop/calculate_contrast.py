from pathlib import Path

tokens = {'background':'#FAF7F0','surface':'#FFFFFF','foreground':'#29261F','muted':'#625E54','accent':'#805331','accent-hover':'#674025','success':'#285B3B','success-soft':'#E8F0E8','error':'#9B302B','error-soft':'#FBECE8','warning':'#674B13','warning-soft':'#FFF2CE','border':'#857C6C','focus':'#805331'}
def luminance(hex_color):
    channels=[int(hex_color[i:i+2],16)/255 for i in (1,3,5)]
    values=[c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4 for c in channels]
    return sum(v*w for v,w in zip(values,(.2126,.7152,.0722)))
def ratio(a,b):
    x,y=sorted((luminance(tokens[a]),luminance(tokens[b])))
    return (y+.05)/(x+.05)
pairs=[('foreground','background'),('foreground','surface'),('muted','background'),('muted','surface'),('surface','accent'),('surface','accent-hover'),('success','success-soft'),('error','error-soft'),('warning','warning-soft'),('border','surface'),('border','background'),('focus','surface'),('focus','background')]
rows=['| Foreground / background | Calculated ratio | Requirement |','|---|---:|---|']
for a,b in pairs:
    r=ratio(a,b)
    rows.append(f'| {a} / {b} | {r:.2f}:1 | '+('≥3:1 non-text' if a in ('border','focus') else '≥4.5:1 normal text')+' |')
Path('contrast-results.md').write_text('\n'.join(rows)+'\n')
print('\n'.join(rows))
