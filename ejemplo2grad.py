from manim import *
import numpy as np
config.background_color=WHITE;Text.set_default(color=BLACK)


class ec2grad(Scene):
    def construct(self):
        
       
        w1=1.6
        recta_aux=NumberLine(rotation=np.pi/2,x_range=[-5,5,2.5],length=3).set_color(BLACK).to_edge(UR,buff=0.8)        
        señalador=Vector(RIGHT).set_color(BLACK).next_to(recta_aux,LEFT,buff=0.1).scale(0.8)       
        label=MathTex("h").add_updater(lambda m: m.next_to(señalador,LEFT)).set_color(BLACK).next_to(señalador,LEFT)
        seguidor= ValueTracker(-1)
        señalador.add_updater(lambda m: m.next_to(recta_aux.n2p(seguidor.get_value()),
                                                  LEFT))                                                 
        ax= Axes(
            x_range=[-1,10,1], y_range=[-1,7,2],
            ).set_color(BLACK)
        anirect= lambda m: lambda x: (1/(m))*(x**2-8*x+12)
        grafic= VMobject()
        def update_grafic(mob):
            mob.become(
                ax.plot(
                   anirect(seguidor.get_value()),                   
                ).set_color(BLACK)
            )
        update_grafic(grafic)
        grafic.add_updater(update_grafic)
        ######Parte animaciones 
        self.add(recta_aux)
        self.add(señalador)
        self.add(label)
        self.add(ax)
        
        #region Marcas recta -5 5
        respuesta=MathTex("(x^2+bx+c)/h").to_edge(UP).set_color(BLACK)
        self.add(respuesta)
        medio=MathTex("0").next_to(señalador,RIGHT,buff=0.43).set_color(BLACK).scale(0.7)
        self.add(medio)
        alto=MathTex("5").next_to(medio,UP,buff=1.255).set_color(BLACK).scale(0.7)
        self.add(alto)
        bajo=MathTex("-5").next_to(medio,DOWN,buff=1.19).set_color(BLACK).scale(0.7)
        self.add(bajo)
        seguidor.set_value(0.1)
        self.add(grafic)
        self.play(seguidor.animate.set_value(0.45),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(5),run_time=1.5*w1,rate_func=smooth)
        self.play(seguidor.animate.set_value(0.39),run_time=1.5*w1,rate_func=linear)
        self.play(seguidor.animate.set_value(4.9),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(0.45),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(3),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(1),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(4.5),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(0.92),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(5),run_time=w1,rate_func=linear)
        self.remove(grafic)
        seguidor.set_value(-0.1)
        self.wait
        self.add(grafic)
        self.play(seguidor.animate.set_value(-0.65),run_time=0.2*w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-5),run_time=1.5*w1,rate_func=smooth)
        self.play(seguidor.animate.set_value(-0.7),run_time=1.5*w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-4.9),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-0.55),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-3),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-1),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-4.5),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-1.22),run_time=w1,rate_func=linear)
        self.play(seguidor.animate.set_value(-5),run_time=w1,rate_func=linear)
        

       