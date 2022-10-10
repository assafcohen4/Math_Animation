
from array import array
from manim import *
from math import *

"""
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
"""
class BooleanOperatrions(Scene):
    
    def construct(self):
        OPACITY = 0.3
        #fade in multiple objects one after another
        def _fade_in_multiple(*argv):
            for arg in argv:
                self.play(FadeIn(arg))

        #the full display of a boolean operation
       

        #a loop for multiple displays
        def _display_multiple_operations(operations: tuple[VMobject], texts: tuple[MathTex],vectors: tuple[np.array],
        rotations: tuple[float], scale: tuple[float]):
            #an inner function to display a single operation
            def _display_operation(operation, text, vector, rotation, scale):
                self.play(FadeIn(operation))
                
                operation_copy = operation.copy()
                self.play(operation_copy.animate.move_to(vector).rotate(rotation).scale(scale))

                self.play(FadeIn(text.next_to(operation_copy,RIGHT)))
                self.play(FadeOut(operation))
            for i in range(len(operations)):
                _display_operation(operations[i],texts[i],vectors[i],rotations[i],scale[i])

        #Enter a vector np.array([x,y,z]) and a rotation angle 0 - 3.60 to get the rotated unit vector
        def _rotate_vector(coords: np.array, angle):
            print(coords,angle)
            x2 = coords[0]*cos(angle) - coords[1]*sin(angle)
            y2 = coords[0]*sin(angle) + coords[1]*cos(angle)
            return np.array([x2,y2,0])

        
        intersection = MarkupText("Intersection")
        union = MarkupText("Union")
        exclusion = MarkupText("Exclusion")
        difference = MarkupText("Difference")

        c1 = Circle(radius=1.4,fill_color=GREEN,stroke_color = GREEN, fill_opacity = 0.5).shift([0,1,0])
        c2 = c1.copy().set_fill(RED).set_stroke(RED).set_opacity(0.3).shift([1,-1.8,0])
        c3 = c2.copy().set_fill(BLUE).set_stroke(BLUE).set_opacity(0.3).shift([-2,0,0])


        c1_c2_inter = Intersection(c1,c2,stroke_color=YELLOW, fill_color=YELLOW, fill_opacity=OPACITY)

        c1_c3_inter = Intersection(c1,c3,stroke_color="#00FFFF", fill_color="#00FFFF", fill_opacity=OPACITY)
        c2_c3_inter = Intersection(c2,c3,stroke_color="#FF00FF", fill_color="#FF00FF", fill_opacity=OPACITY)
        c1_c2_c3_inter = Intersection(c1,c2,c3,stroke_color=WHITE, fill_color=WHITE, fill_opacity=OPACITY)
        
        c1_c2_un = Union(c1,c2,stroke_color=YELLOW, fill_color=YELLOW, fill_opacity=OPACITY)
        c1_c3_un = Union(c1,c3,stroke_color="#00FFFF", fill_color="#00FFFF", fill_opacity=OPACITY)
        c2_c3_un = Union(c2,c3,stroke_color="#FF00FF", fill_color="#FF00FF", fill_opacity=OPACITY)
        c1_c2_c3_un = Union(c1,c2,c3,stroke_color=WHITE, fill_color=WHITE, fill_opacity=OPACITY)
        
        A = Text("A",color=WHITE,font_size=28).move_to(c1,ORIGIN)
        B = Text("B",color=WHITE,font_size=28).move_to(c2,ORIGIN)
        C = Text("C",color=WHITE,font_size=28).move_to(c3,ORIGIN)

        c1_c2_inter_txt = MathTex("A \\cap B")
        c1_c3_inter_txt = MathTex("A \\cap C")
        c2_c3_inter_txt = MathTex("B \\cap C")
        c1_c2_c3_inter_txt = MathTex("A \\cap B \\cap C")

        c1_c2_un_txt = MathTex("A \\cup B")
        c1_c3_un_txt = MathTex("A \\cup C")
        c2_c3_un_txt = MathTex("B \\cup C")
        c1_c2_c3_un_txt = MathTex("A \\cup B \\cup C")

        c1_c2_symdif = MathTex("A \\Delta B")
        c1_c2_c3_symdif = MathTex("A \\Delta (B \\cup C)")

        
        #start of scene
        self.play(FadeIn(intersection))
        self.play(FadeOut(intersection))
        
        _fade_in_multiple(c1, c2, c3, A, B, C)
        
        _display_multiple_operations((c1_c2_inter, c1_c3_inter, c2_c3_inter,c1_c2_c3_inter),
                                     (c1_c2_inter_txt, c1_c3_inter_txt, c2_c3_inter_txt, c1_c2_c3_inter_txt),
                                     (RIGHT*4.8, RIGHT*4.8 - DOWN *3, RIGHT*4.8 + DOWN *3, DOWN*3.2),
                                     (45,-45, 0, 0),(1,1,1,1))
          
        self.clear()
        self.play(FadeIn(union))
        self.play(FadeOut(union)) 
        self.add(c1,c2,c3,A,B,C)
        _display_multiple_operations((c1_c2_un, c1_c3_un, c2_c3_un,c1_c2_c3_un),
                                     (c1_c2_un_txt, c1_c3_un_txt, c2_c3_un_txt, c1_c2_c3_un_txt),
                                     (RIGHT*4.6, RIGHT*4.6 - DOWN *3, RIGHT*4.6 + DOWN *3, DOWN*3.2),
                                     (45,-45, 0, 0),
                                     (0.32,0.32,0.32,0.3))
        

        self.clear()
        self.play(FadeIn(exclusion))
        self.play(FadeOut(exclusion)) 

        self.play(FadeIn(c1_c2_symdif))
        self.add(c1,c2,c3,A,B,C)

        
"""""
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
   
"""