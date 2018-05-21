class Rock {
  // Member Variables
  int x;
  int speed;
  color c;
  int r;
  int y;
  int health;
  int size;
  
  // Constructor
  Rock(int Xpos, int Ypos, int Xspeed, int Xradius, color typeR, int Hp, int size) {
    this.size = size;
    r = Xradius;
    x = Xpos;
    y = Ypos;
    speed = Xspeed;
    c = typeR;
    health = Hp;
  }
  
  // Move Down the Screen
  void move() {
    y += speed;
  }
  
  // Detect if Rock Passes
  boolean reachBottom() {
    if (y > height + r*4) {
      return true;
    } else {
      return false;
    }
  }
  
  // Draw the Rock
  void display() {
    fill(c);
    noStroke();
    ellipse(x, y, r, r);
    fill(255);
  }
  
  // Determine if Rock is Hit
  void hit() {
    speed = 0;
    y = -1000;
    x = -50; 
  }
}