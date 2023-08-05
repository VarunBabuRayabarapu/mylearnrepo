from string import ascii_lowercase

d={v:k for k,v in enumerate(ascii_lowercase)}
s1=input()
s2=input()
s3=""
s4=""
for i in range(min(len(s1),len(s2))):
    if d[s1[i]]>=d[s2[i]]:
        s3+=s2[i]
        s4+=s1[i]
    else:
        s4+=s2[i]
        s3+=s1[i]

s4=s4[::-1]

if len(s1)>len(s2):
    s4+=s2[len(s2)-len(s1):]
elif len(s1)<len(s2):
    s4+=s1[len(s1)-len(s2):]
print(s3+s4)
    
    
