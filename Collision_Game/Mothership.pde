class Mother {
  // Member Variables
  PImage mother;
  int r;
  color col;
  int x, y;
  boolean enemy;
  
  // Constructor
  Mother(int r) {
    this.r = r;
     mother = loadImage("MotherShip.png");
  }

  // Draws the Spaceship
  void display() {
    image(mother,160, 20);
  }
  
  // Detect Collision
  boolean collide(Ship ship) {
    float distance = dist(x, y, ship.x, ship.y);
    if (distance < r + ship.r) {
      return true;
    } else {
      return false;
    }
  }
}