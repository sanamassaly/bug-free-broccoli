from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.c = coeffs[0]
        self.b = coeffs[1]
        self.a = coeffs[2]


    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        c1 = self.c  + other.c
        b1 = self.b  + other.b
        a1 = self.a  + other.a

        if b1< 0:
            b = f'{self.b}'
        else:
            b = f'+{self.b}'
        
        if c1 <0:
            c = f'{self.c}'
        else:
            c = f'+{self.c}'
        
        
        message = f"{a1}X^2 {b}X {c}"
        return message

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        c1 = self.c  - other.c
        b1 = self.b  - other.b
        a1 = self.a  - other.a

        if b1< 0:
            b = f'{self.b}'
        else:
            b = f'+{self.b}'
        
        if c1 <0:
            c = f'{self.c}'
        else:
            c = f'+{self.c}'
        
        
        message = f"{a1}X^2 {b}X {c}"
        return message
        pass

        

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        if self.b< 0:
            b = f'{self.b}'
        else:
            b = f'+{self.b}'
        
        if self.c <0:
            c = f'{self.c}'
        else:
            c = f'+{self.c}'
        
        message = f"{self.a}X^2 {b}X {c}"
        return message

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        self.delta = self.b**2 - 4*(self.a * self.c)
        if self.delta != 0:
            self.x1 = (- self.b - sqrt(self.delta))/2*self.a
            self.x2 = (- self.b + sqrt(self.delta))/2*self.a
            return self.x1, self.x2
        else:
        
            self.x = -self.b / 2*self.a
            return self.x

           

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        self.x = x
        self.y = self.a*self.x**2 + self.b*self.x + self.c
        return self.y
    

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        
        x_points = list(range(0,20,2)) 
        y = list(self.__val(k) for k in x_points)


        axes = plt.gca()
        axes.grid(True)
        axes.set_xlabel('Abscisses') 
        axes.set_ylabel('Ordonnées') 

        plt.scatter(x_points,y,marker = "x",color = "green")
        
        plt.title(self.__str__())
        plt.show() 

        pass


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)
    print(p1)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)
    print(p2)
    print(p2.solve())

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2
    

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    print(p1)
    p1.draw()  # trace la courbe de p1, voir fichier png
