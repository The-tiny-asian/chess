class Timer {
  // Member Variables
  int savedTime;
  int totalTime;
  
  // Constructor
  Timer(int tempTotalTime) {
    totalTime = tempTotalTime;
  }
  
  // Start Timer
  void start() {
    savedTime = millis();
  }
  
  // Detect if Milli Time Period Has Elapsed to Release Another Rock
  boolean isFinished() {
    int passedTime = millis()- savedTime;
    if (passedTime > totalTime) {
      return true;
    } else {
      return false;
    }
  }
}