
from array import array
from manim import *
from math import *


class BraceAnnotation(Scene):
    
    def construct(self):
        dot1_coords = [0,0,0]
        dot2_coords = (2,2,0)

        num_pl = NumberPlane()
        dot1 = Dot([0,0,0])
        dot2 = Dot([2,2,0])
        arrow = Arrow(dot1,dot2,buff=0)

        text = Text("{a},{b}".format(a=dot1_coords[0], b=dot1_coords[1]),font='american_typewriter')
        text.next_to(dot1,DOWN)
        self.add(num_pl,dot1,dot2,arrow,text)

class BooleanOperatrions(Scene):
    
    def construct(self):
        
        #fade in multiple objects one after another
        def _fade_in_multiple(*argv):
            for arg in argv:
                self.play(FadeIn(arg))

        
        def _show_intersection(intersection: Mobject, text: MathTex, vector: np.array, rotation):
            self.play(FadeIn(intersection))
            
            intersection_copy = intersection.copy()
            self.play(intersection_copy.animate.move_to(vector).rotate(rotation))

            self.play(FadeIn(text.next_to(intersection_copy,UP)))
            self.play(FadeOut(intersection))

            
        #Enter a vector np.array([x,y,z]) and a rotation angle 0 - 3.60 to get the rotated unit vector
        def _rotate_vector(coords: np.array, angle):
            print(coords,angle)
            x2 = coords[0]*cos(angle) - coords[1]*sin(angle)
            y2 = coords[0]*sin(angle) + coords[1]*cos(angle)
            return np.array([x2,y2,0])

        el1 = Circle(radius=1.5,fill_color=GREEN,stroke_color = GREEN, fill_opacity = 0.5).shift([0,1,0])
        el2 = el1.copy().set_fill(RED).set_stroke(RED).set_opacity(0.3).shift([1,-1.8,0])
        el3 = el2.copy().set_fill(BLUE).set_stroke(BLUE).set_opacity(0.3).shift([-2,0,0])

        el1_el2_inter = Intersection(el1,el2).set_stroke(YELLOW).set_fill(YELLOW).set_opacity(0.3)
        el1_el3_inter = Intersection(el1,el3).set_stroke(PURPLE).set_fill(PURPLE).set_opacity(0.3)
        el2_el3_inter = Intersection(el2,el3).set_stroke(PINK).set_fill(PINK).set_opacity(0.3)

        el1_el2_el3_inter = Intersection(el1,el2,el3).set_stroke(PINK).set_fill(PINK).set_opacity(0.3)
 
        
        A = Text("A",color=WHITE,font_size=28).move_to(el1,ORIGIN)
        B = Text("B",color=WHITE,font_size=28).move_to(el2,ORIGIN)
        C = Text("C",color=WHITE,font_size=28).move_to(el3,ORIGIN)

        el1_el2_txt = MathTex("A \\cap B")
        el1_el3_txt = MathTex("A \\cap C")
        el2_el3_txt = MathTex("B \\cap C")
        el1_el2_el3_txt = MathTex("A \\cap B \\cap C")
        
        _fade_in_multiple(el1, el2, el3, A, B, C)
        
        _show_intersection(el1_el2_inter,el1_el2_txt,RIGHT*5,45)
        
        _show_intersection(el1_el2_el3_inter,el1_el2_el3_txt,RIGHT * 5 + UP *2.8,0)

        # show el1_el2 intersection
        #self.play(FadeIn(el1_el2_inter))
        #self.play(el1_el2_inter_copy.animate.move_to(RIGHT * 5).rotate(45))

        
        #show el1_el2 text
        #el1_el2_txt.next_to(el1_el2_inter_copy,UP)
        #self.play(FadeIn(el1_el2_txt))
        #self.play(FadeOut(el1_el2_inter))


        #show el1_el2_el3 intersection
        #self.play(FadeIn(el1_el2_el3_inter))
        #self.play(el1_el2_el3_inter_copy.animate.move_to(RIGHT * 5 + UP *2.8))

        #show el1_el2_el3 intersection
        #el1_el2_el3_txt.next_to(el1_el2_el3_inter_copy,UP)
        #self.play(FadeIn(el1_el2_el3_txt))
        #self.play(FadeOut(el1_el2_el3_inter))

       

        
        

    

        


class PointMovingOnShapes(Scene):
    def construct(self):
        cir = Circle()
        dot = Dot()
        self.add(dot,cir)
        self.play(MoveAlongPath(dot,cir),run_time=3)
        self.play(Rotating(dot,about_point=[1,1,1]))

class MovingAngle(Scene):
    def construct(self):
        track = ValueTracker(0)
        l1 = Line([-1,0,0], [1,0,0])
        l2 = l1.copy()

        l1.add_updater(
            lambda x: x.rotate(
                track.get_value()*DEGREES,l1.start
            )
        )
        self.add(l1,l2,track)
        self.play(track.animate.set_value(90),run_time=10)
   
