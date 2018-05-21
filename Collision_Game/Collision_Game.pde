ArrayList<Rock> rocks;
ArrayList<Laser> lasers;
Timer timer;
Ship ship;
Mother mother;
int rockRate = 250;
int score;

void setup() {
  size(500, 500);
  ship = new Ship(50);
  rocks = new ArrayList<Rock>();
  lasers = new ArrayList<Laser>();
  timer = new Timer(rockRate);
  mother = new Mother(0);
  timer.start();
}
void draw() {
  background(11, 25, 75);
  score = millis()/10;
  fill(255);
  textSize(20);
  text(score, 10, 490);
  noCursor();
  mother.display();
  ship.display();
  if (timer.isFinished()) {
    if (random(101)>10) {
      rocks.add(new Rock(int(random(width)), -10, int(random(3, 6)), int(random(20, 70)), color(70, 45, 13), 10, 4));
    } else {
      rocks.add(new Rock(int(random(width)), -10, int(random(1, 3)), int(random(15, 30)), color(570, 45, 13), 10, 4));
    }
    timer.start();
  }
  for (int i = rocks.size()-1; i>=0; i--) {
    Rock rock = (Rock) rocks.get(i);
    rock.move();
    rock.display();
    if (rock.reachBottom()) {
      rocks.remove(rock);
    }
    for (int j = lasers.size()-1; j>=0; j--) {
      Laser l = (Laser) lasers.get(j);
      if (dist(l.x, l.y, rock.x, rock.y) < rock.r) {
        rock.health-=1;
      }
      if (rock.health<10) {
        rocks.remove(rock);
      }
    }
    //Ship Interaction
    for (int j = rocks.size()-1; j>=0; j--) {
      Rock l = (Rock) rocks.get(j);
      if (dist(l.x, l.y, ship.x, ship.y) < ship.r) {
        //ship.health-=1;
      }
      if (rock.health<10) {
        rocks.remove(rock);
      }
    }
  }
  for (int a = lasers.size()-1; a>=0; a--) {
    Laser laser = (Laser) lasers.get(a);
    laser.fire();
    laser.display();
    if (laser.reachedTop()) {
      lasers.remove(laser);
    }
  }
}

void infoPanel() {
}

void mouseReleased() {
  lasers.add(new Laser(mouseX, mouseY));
}
void keyPressed() {
  if (key == ' ') {
    lasers.add(new Laser(ship.x, ship.y));
  }
}