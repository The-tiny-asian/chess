class Ship {
  // Member Variables
  int r;
  color col;
  int x, y;
  boolean enemy;
  PImage ship;
  
  // Constructor
  Ship(int r) {
    this.r = r;
     ship = loadImage("Hiro.png");
  }

  // Draws the Spaceship
  void display() {
    image(ship, mouseX-25, mouseY+25,50,50);
  }
  
  // Detect Collision
  boolean collide(Rock rock) {
    float distance = dist(x, y, rock.x, rock.y);
    if (distance < r + rock.r) {
      return true;
    } else {
      return false;
    }
  }
}