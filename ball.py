from turtle import Turtle


class Ball(Turtle):
  
    INITIAL_X_MOVE = 3
    INITIAL_Y_MOVE = 3
    SPEED_INCREMENT = 0.15 
    MAX_SPEED = 15 
    
    def __init__(self, paddle_hit_func, score_sound_func):
        super().__init__()
     
        self.color("yellow")
        self.shape("circle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()

        self.x_move = self.INITIAL_X_MOVE
        self.y_move = self.INITIAL_Y_MOVE
        self.move_speed = 0.015 
        self.bounce_counter = 0

        self.play_paddle_hit = paddle_hit_func
        self.play_score_sound = score_sound_func


        self.last_hit_paddle = None

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
   
    def bounce_x(self, hitting_paddle=None):

        self.bounce_counter += 1
   
        if self.bounce_counter <= 10 and hitting_paddle is not None:

            if hitting_paddle.initial_x > 0:

                if self.x_move > 0:
                    self.x_move *= -1 

            else:
                
                if self.x_move < 0:
                    self.x_move *= -1  

    
        else:
            self.x_move *= -1


        self.play_paddle_hit()

      

    def reset_position(self):
        self.goto(0, 0)

        self.bounce_counter = 0

  
        self.x_move = self.INITIAL_X_MOVE * (self.x_move / abs(self.x_move))
        self.y_move = self.INITIAL_Y_MOVE
        self.move_speed = 0.015

        self.bounce_x()  

     

    def speed_up(self):
            """Increases the speed of the ball gradually when called (e.g., on scoring)."""
           

            current_speed = abs(self.x_move)

            if current_speed < self.MAX_SPEED:

                self.x_move += (self.x_move / current_speed) * self.SPEED_INCREMENT

                self.y_move += (self.y_move / abs(self.y_move)) * self.SPEED_INCREMENT

                if self.move_speed > 0.005:
                    self.move_speed *= 0.95

