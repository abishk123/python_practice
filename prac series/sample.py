print(oct(12))
print(bin(12))
print(hex(12))

n=int(input('n:'))
con = input("conversion into :")
string=""
if con=="binary":
    dummy=n
    while dummy>0:
        rem=dummy%2
        string+=str(rem)
        dummy//=2
elif con=="octal":
    dummy=n
    while dummy>0:
        rem=dummy%8
        string+=str(rem)
        dummy//=8
elif con=="hexadecimal":
    l=[0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
    dummy=n
    while dummy>0:
        rem=dummy%16
        string+=l[rem]
        dummy//=16
print(string[::-1])



