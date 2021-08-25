import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.A=A
        self.A=A
        self.x_old=[]
        for i in range(0,len(A)):
            self.x_old.append(A[i][0])
        self.y_old=[]
        for i in range(0,len(A)):
            self.y_old.append(A[i][1])
        self.x_new=self.x_old
        self.y_new=self.y_old

 
    
    def translate(self, dx=0, dy=None):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        self.x_old=self.x_new
        self.y_old=self.y_new

        if dy==None:
            dy=dx
        
        Shape.translate(self,dx,dy)
        tm=self.T_t
        T_tt= tm.transpose()
        newcord=self.A @ T_tt
        x_new=[]
        for i in range(0,len(newcord)):
            x_new.append(round(newcord[i][0],2))
        y_new=[]
        for i in range(0,len(newcord)):
            y_new.append(round(newcord[i][1],2))
        
        for i in range(0,len(newcord)):
            self.A[i][0]=x_new[i]
        for i in range(0,len(newcord)):
            self.A[i][1]=y_new[i]
        self.x_new=x_new
        self.y_new=y_new
        
        return (x_new,y_new)
    
    def scale(self, sx=0, sy=None):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates

        '''
        self.x_old=self.x_new
        self.y_old=self.y_new

        if sy==None:
            sy=sx

        x=np.array(self.x_old)
        x_avg=np.average(x)
        y=np.array(self.y_old)
        y_avg=np.average(y)
        scaling_mat=self.A
        for i in range(0,len(self.A)):
            scaling_mat[i][0]=(self.A[i][0]-x_avg)
        for i in range(0,len(self.A)):
            scaling_mat[i][1]=(self.A[i][1]-y_avg)

        Shape.scale(self,sx,sy)
        sm=self.T_s
        T_ss= sm.transpose()
        scaling_mat=scaling_mat @ T_ss
        for i in range(0,len(scaling_mat)):
            scaling_mat[i][0]=(scaling_mat[i][0]+x_avg)
        for i in range(0,len(scaling_mat)):
            scaling_mat[i][1]=(scaling_mat[i][1]+y_avg)
        newcord=scaling_mat
        x_new=[]
        for i in range(0,len(newcord)):
            x_new.append(round(newcord[i][0],2))
        y_new=[]
        for i in range(0,len(newcord)):
            y_new.append(round(newcord[i][1],2))

        for i in range(0,len(newcord)):
            self.A[i][0]=x_new[i]
        for i in range(0,len(newcord)):
            self.A[i][1]=y_new[i]
        self.x_new=x_new
        self.y_new=y_new
        
        return (x_new,y_new)

    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        self.x_old=self.x_new
        self.y_old=self.y_new

        x=np.array(self.x_old)
        x_avg=np.average(x)
        y=np.array(self.y_old)
        y_avg=np.average(y)
        rotate_mat=self.A
        for i in range(0,len(self.A)):
            rotate_mat[i][0]=(self.A[i][0]-rx)
        for i in range(0,len(self.A)):
            rotate_mat[i][1]=(self.A[i][1]-ry)

        Shape.rotate(self,deg)
        rm=self.T_r
        T_rr= rm.transpose()
        rotate_mat=rotate_mat @ T_rr
        for i in range(0,len(rotate_mat)):
            rotate_mat[i][0]=(rotate_mat[i][0]+rx)
        for i in range(0,len(rotate_mat)):
            rotate_mat[i][1]=(rotate_mat[i][1]+ry)
        newcord=rotate_mat
        x_new=[]
        for i in range(0,len(newcord)):
            x_new.append(round(newcord[i][0],2))
        y_new=[]
        for i in range(0,len(newcord)):
            y_new.append(round(newcord[i][1],2))

        for i in range(0,len(newcord)):
            self.A[i][0]=x_new[i]
        for i in range(0,len(newcord)):
            self.A[i][1]=y_new[i]
        self.x_new=x_new
        self.y_new=y_new
        
        
        return (x_new,y_new)
    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        xold=self.x_old
        xold.append(xold[0])
        yold=self.y_old
        yold.append(yold[0])
        xnew=self.x_new
        xnew.append(xnew[0])
        ynew=self.y_new
        ynew.append(ynew[0])


        plt.plot(xold, yold, linestyle = 'dashed')
        plt.plot(xnew,ynew)

        y_lim_old=np.amax(yold)
        y_lim_new=np.amax(ynew)
        x_lim_old=np.amax(xold)
        x_lim_new=np.amax(xnew)

        x_lim=max(x_lim_new,x_lim_old)
        y_lim=max(y_lim_new,y_lim_old)

        Shape.plot(self,x_lim,y_lim)


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.cx_old=round(x,2)
        self.cy_old=round(y,2)
        self.cx_new=round(x,2)
        self.cy_new=round(y,2)
        self.r_old=round(radius,2)
        self.r_new=self.r_old



    
    def translate(self, dx=0, dy=None):
        '''
        Function to translate the circle
        
        This function takes 2 arguments: dx and dy (dy is optional).
        
        This function returns the final coordinates and the radius
        '''
        self.cx_old=self.cx_new
        self.cy_old=self.cy_new
        self.r_old= self.r_new
        
        ccordmat=np.array([self.cx_old,self.cy_old,1])
        if dy==None:
            dy=dx

        Shape.translate(self,dx,dy)
        tm=self.T_t
        T_tt= tm.transpose()
        newcord=ccordmat @ T_tt

        cx_new,cy_new,k=newcord
        cx_new=np.around(cx_new,2)
        cy_new=np.around(cy_new,2)
        radius=self.r_old


        self.cx_new=cx_new
        self.cy_new=cy_new

        
        return (cx_new,cy_new,radius)
        
    def scale(self, sx):
        
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.cx_old = self.cx_new
        self.cy_old = self.cy_new
        self.r_old=self.r_new

        r_new=(self.r_old)*(sx)
        r_new=np.around(r_new,2)

        self.r_new=r_new

        return (self.cx_old,self.cy_old,r_new)

 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.cx_old=self.cx_new
        self.cy_old=self.cy_new
        self.r_old=self.r_new

        if ry==0:
            ry=rx

        rotate_mat=np.array([self.cx_old,self.cy_old,1])

        rotate_mat[0]=(rotate_mat[0]-rx)
        rotate_mat[1]=(rotate_mat[1]-ry)

        Shape.rotate(self,deg)
        rm=self.T_r
        T_rr= rm.transpose()
        rotate_mat=rotate_mat @ T_rr

        rotate_mat[0]=(rotate_mat[0]+rx)

        rotate_mat[1]=(rotate_mat[1]+ry)

        cx_new=np.around(rotate_mat[0],2)
        cy_new=np.around(rotate_mat[1],2)
        r_new=self.r_old

        self.cx_new=round(cx_new,2)
        self.cy_new=round(cy_new,2)

        return (cx_new,cy_new,r_new)
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        circle_old=plt.Circle((self.cx_old, self.cy_old), self.r_old, fill=False,linestyle = 'dashed')
        circle_new=plt.Circle((self.cx_new, self.cy_new), self.r_new, fill=False)

        fig, ax = plt.subplots()
        ax.add_patch(circle_old)
        ax.add_patch(circle_new)

        x_lim=max(self.cx_old+self.r_old,self.cx_new+self.r_new)
        y_lim=max(self.cy_old+self.r_old,self.cy_new+self.r_new)

        Shape.plot(self,x_lim,y_lim)
        

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    verbose=int(input("verbose? 1 to plot, 0 otherwise:"))
    testcase=input("Enter the number of test cases:")
    print("0 for polygon")
    print("1 for circe")
    shapetype=int(input("Enter type of shape:"))
    if shapetype==0:
        nsides=int(input("Enter the number of sides:"))
        A=[]
        n=0
        while n<nsides:
            x,y=map(float,input("Enter(x,y):").split())
            element=[x,y,1]
            A.append(element)
            n=n+1

        figure=Polygon(A)
    elif shapetype==1:
        a,b,r=map(float,input("Enter cordinates of center and radius space seperated (eg. x y r):").split())
        figure=Circle(a,b,r)
    else:
        print("invalid input")
    querynum=int(input("Enter the number of queries:"))
    print("Awailible query are:")
    print("1)R deg (rx)(ry) for rotation\n2)T dx(dy) for translation\n3)for polygon \n  S sx(sy)\n for circle\n  S sr for scalling\n4)P for ploting")
    countquery=0
    while countquery<querynum:
         
        while True:
            responce=list(map(str, input("Enter the item codes (space-separated): ").split()))
            if len(responce)<=4:
                break
        
        if responce[0]=='R':
            deg=float(responce[1])
            if shapetype==0:
                if len(responce)>4:
                    x,y=figure.rotate(deg,float(responce[2]),float(responce[3]),float(responce[4]))
                if len(responce)>3:
                    x,y=figure.rotate(deg,float(responce[2]),float(responce[3]))
                if len(responce)>2:
                    x,y=figure.rotate(deg,float(responce[2]))
                if len(responce)>1:
                    x,y=figure.rotate(deg)
                xold=figure.x_old
                yold=figure.y_old
                for i in range(0,len(xold)):
                    print(round(xold[i],2),end='')
                    print(' ',end='')
                for i in range(0,len(yold)):
                    print(round(yold[i],2),end='')
                    print(' ',end='')
                print('')


                for i in range(0,len(x)):
                    print(round(x[i],2),end='')
                    print(' ',end='')
                for i in range(0,len(y)):
                    print(round(y[i],2),end='')
                    print(' ',end='')
                print('')
            if shapetype==1:
                if len(responce)>4:
                    xn,yn,rn=figure.rotate(deg,float(responce[2]),float(responce[3]),float(responce[4]))
                if len(responce)>3:
                    xn,yn,rn=figure.rotate(deg,float(responce[2]),float(responce[3]))
                if len(responce)>2:
                    xn,yn,rn=figure.rotate(deg,float(responce[2]))
                if len(responce)>1:
                    xn,yn,rn=figure.rotate(deg)
                
                xo=figure.cx_old
                yo=figure.cy_old
                ro=figure.r_old
                print(xo,end='')
                print(" ",end='')
                print(yo,end='')
                print(" ",end='')
                print(ro,end='')
                print(" ")


                print(xn,end='')
                print(" ",end='')
                print(yn,end='')
                print(" ",end='')
                print(rn,end='')
                print(" ")

            countquery=countquery+1
            if verbose==1:
                figure.plot()
        if responce[0]=='T':
            if shapetype==0:
                if len(responce)>2:
                    x,y=figure.translate(float(responce[1]),float(responce[2]))
                if len(responce)>1:
                    x,y=figure.translate(float(responce[1]))
                xold=figure.x_old
                yold=figure.y_old
                for i in range(0,len(xold)):
                    print(round(xold[i],2),end='')
                    print(' ',end='')
                for i in range(0,len(yold)):
                    print(round(yold[i],2),end='')
                    print(' ',end='')
                print('')

                for i in range(0,len(x)):
                    print (round(x[i],2),end='')
                    print(' ',end='')
                for i in range(0,len(y)):
                    print (round(y[i],2),end='')
                    print(' ',end='')
                print('')
            if shapetype==1:
                if len(responce)>2:
                    xn,yn,rn=figure.translate(float(responce[1]),float(responce[2]))
                if len(responce)>1:
                    xn,yn,rn=figure.translate(float(responce[1]))
                xo=figure.cx_old
                yo=figure.cy_old
                ro=figure.r_old
                print(xo,end='')
                print(" ",end='')
                print(yo,end='')
                print(" ",end='')
                print(ro,end='')
                print(" ")


                print(xn,end='')
                print(" ",end='')
                print(yn,end='')
                print(" ",end='')
                print(rn,end='')
                print(" ")

            
            countquery=countquery+1
            if verbose==1:
                figure.plot()
        if responce[0]=='S':
            if shapetype==0:
                if len(responce)>2:
                    x,y=figure.scale(float(responce[1]),float(responce[2]))
                if len(responce)>1:
                    x,y=figure.scale(float(responce[1]))
                xold=figure.x_old
                yold=figure.y_old
                for i in range(0,len(xold)):
                    print(round(xold[i],2),end='')
                    print(' ',end='')
                for i in range(0,len(yold)):
                    print(round(yold[i],2),end='')
                    print(' ',end='')
                print('')

                for i in range(0,len(x)):
                    print (round(x[i],2),end='')
                    print(' ',end='')
                for i in range(0,len(y)):
                    print (round(y[i],2),end='')
                    print(' ',end='')
                print('')
            if shapetype==1:
                if len(responce)>1:
                    xn,yn,rn=figure.scale(float(responce[1]))
                xo=figure.cx_old
                yo=figure.cy_old
                ro=figure.r_old
                print(xo,end='')
                print(" ",end='')
                print(yo,end='')
                print(" ",end='')
                print(ro,end='')
                print(" ")



                print(xn,end='')
                print(" ",end='')
                print(yn,end='')
                print(" ",end='')
                print(rn,end='')
                print(" ")

            countquery=countquery+1
            if verbose==1:
                figure.plot()
        if responce[0]=='P':
            figure.plot()
            countquery=countquery+1
            if verbose==1:
                figure.plot()
    figure.plot()

        

                


        




