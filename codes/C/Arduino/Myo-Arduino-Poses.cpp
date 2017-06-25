#include <MyoController.h>
 
#define pinFist 4
#define pinWaveIn 5
#define pinWaveOut 6
#define pinFigersSpread 7
 
MyoController myo = MyoController();
 
void setup() {
 
// TRISD (0 até 7) como outputs:
  DDRD = 255;
  myo.initMyo();
}
 
void loop()
{
   myo.updatePose();
   switch (myo.getCurrentPose()) {
    case rest:
      digitalWrite(pinFist, LOW);
      digitalWrite(pinWaveIn, LOW);
      digitalWrite(pinWaveOut, LOW);
      digitalWrite(pinFingersSpread, LOW);
    break;
    case fist:
      digitalWrite(pinFist, HIGH);
      break;
    case waveIn:
      digitalWrite(pinWaveIn, HIGH);
      break;
    case waveOut:
      digitalWrite(pinWaveOut, HIGH);
      break;
    case fingersSpread:
      digitalWrite(pinFingersSpread, HIGH);
   }
   delay(100);
}
