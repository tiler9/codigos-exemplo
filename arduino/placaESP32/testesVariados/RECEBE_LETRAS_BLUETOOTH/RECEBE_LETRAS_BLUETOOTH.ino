void setup() {
  // put your setup code here, to run once:

  pinMode(2, OUTPUT); // Led Built in do ESP32
  Serial2.begin(9600); // deixei a Serial2 pois a Serial 0 é usada pelo esp para carregar o programa na placa
}

void loop() {
  // put your main code here, to run repeatedly:

 //funciona
  char c = Serial2.read();

  // para mandar estas letras, baixei o app de controle bluetooth
  if(c == 'A') digitalWrite(2, HIGH); 
  if(c == 'a') digitalWrite(2, LOW);
}
