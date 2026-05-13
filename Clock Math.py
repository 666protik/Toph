'''
Given a time (hours as H and minutes as M), determine the smaller angle
between the two hands of a clock showing the time and print it.
        Input                 Output
        10 15               142.5000000
'''
H,M = map(int, input().split())

rm=M*6
rh= (H%12)*30 + (M*0.5)

angle=abs(rh-rm)
result=min(angle,360-angle)
ans=f"{result:.4f}"

print(ans)
