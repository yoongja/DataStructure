class Matrix:

    def initial(a,b,c,d):
        A = [[0 for col in range(2)] for row in range(2)]

        A[0][0]=a
        A[0][1]=b
        A[1][0]=c
        A[1][1]=d
        return A

    def __add__(A,B):
        answer = []

        for i in range(len(A)):
            tmp = []
            for j in range(len(A[i])):
                tmp.append(A[i][j]+B[i][j])

            answer.append(tmp)    
        return answer 

    def __sub__(A,B):
        answer = []

        for i in range(len(A)):
            tmp=[]
            for j in range(len(A[i])):
                tmp.append(A[i][j]-B[i][j])

            answer.append(tmp)    
        return answer 

    def main():
        if __name__ == "__main__":
            A = Matrix(1, 2, 3, 4)
            B = Matrix(5, 6, 7, 8)
            C = A+B
            D = A-B
            print(C)
            print(D)
  