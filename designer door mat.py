if __name__ == "__main__":
    n, m = map(int,input().split())
    mat1 = ""
    for i in range(n//2):
        mat1 += "".join(".|."*(i*2+1)).center(m, "-")+"\n"
        
    print(mat1 + "WELCOME".center(m,"-") + mat1[::-1])