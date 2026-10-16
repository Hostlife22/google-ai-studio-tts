import sys, wave, numpy as np
def load(p):
    w=wave.open(p); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768; return x, w.getframerate()
def acf_stats(x, fs):
    win=int(fs*0.04); hop=int(fs*0.01); minL=fs//400; maxL=int(np.ceil(fs/65)); f0=[]
    for s in range(0, len(x)-win-maxL, hop):
        a=x[s:s+win]; e=(a*a).sum()
        if e/win<=1e-5: continue
        best=0; bl=0
        for L in range(minL, maxL+1):
            b=x[s+L:s+L+win]; r=(a*b).sum()/np.sqrt(e*(b*b).sum()+1e-12)
            if r>best: best=r; bl=L
        if best>0.6: f0.append(fs/bl)
    v=np.array(f0); med=np.median(v); st=12*np.log2(v/med)
    return round(med), [round(np.percentile(v,10)), round(np.percentile(v,90))], round(float(st.std()),2)
for p in sys.argv[1:]:
    x,fs=load(p); x=x[:fs*40]
    print(p.split('/')[-1], *acf_stats(x,fs))
