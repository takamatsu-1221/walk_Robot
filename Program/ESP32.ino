#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include "SSD1306.h"

//Wifi SSID,Password
const char* ssid     = "";
const char* password = "";

//WebServer begin
WebServer server(80);

//Pin
const int trig_reset = 0;
const int trig_advance = 4;
const int trig_back = 16;
const int trig_left = 17;
const int trig_right = 5;

//display
SSD1306  display(0x3c, 21, 22);


void setup() {
  display.init();
  display.setFont(ArialMT_Plain_24);
  display.drawString(0, 16, "connecting...");
  display.display();
  
  //Pin asign
  pinMode(trig_reset, OUTPUT);
  pinMode(trig_advance, OUTPUT);
  pinMode(trig_back, OUTPUT);
  pinMode(trig_left, OUTPUT);
  pinMode(trig_right, OUTPUT);
  //Initial signal
  digitalWrite(trig_reset, LOW);
  digitalWrite(trig_advance, LOW);
  digitalWrite(trig_back, LOW);
  digitalWrite(trig_left, LOW);
  digitalWrite(trig_right, LOW);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(300);
  }

  //display output
  display.init();
  display.setFont(ArialMT_Plain_24);
  display.drawString(40, 16, out_ip(WiFi.localIP()));
  display.display();

  //server started
  server.on("/", move_mainpage);
  server.onNotFound(handleNotFound);
  server.begin();
}


void loop() {
  server.handleClient();
}



//main page
void move_mainpage() {
  String html;
  //HTML
  html = "<!DOCTYPE html>";
  html += "<html lang='ja'>";
  html += "<head>";
  html += "<meta charset=\"utf-8\">";
  html += "<title>Robot move system</title>";
  html += "</head>";
  
  html += "<body>";
  
  html += "<center>";
  html += "<h1>welcome to robot control system!</h1>";
  html += "</center>";

  html += "<br>";

  html += "<center>";
  html += "<p>";
  html += "<a href=\"/?advance=on\">↑advance↑</a>";
  html += "</p>";
  html += "</center>";

  html += "<center>";
  html += "<p>";
  html += "<a href=\"/?left=on\">←left</a>";
  html += "</p>";
  html += "</center>";

  html += "<center>";
  html += "<p>";
  html += "<a href=\"/?right=on\">right→</a>";
  html += "</p>";
  html += "</center>";

  html += "<center>";
  html += "<p>";
  html += "<a href=\"/?back=on\">↓back↓</a>";
  html += "</p>";
  html += "</center>";

  html += "<br>";

  html += "<center>";
  html += "<p>";
  html += "<a href=\"/?reset=on\">reset & stop</a>";
  html += "</p>";
  html += "</center>";

  html += "</body>";
  html += "</html>";

  //click active
  if (server.hasArg("reset")){
    if (server.arg("reset").equals("on")){
      digitalWrite(trig_reset, HIGH);
      digitalWrite(trig_advance, LOW);
      digitalWrite(trig_back, LOW);
      digitalWrite(trig_left, LOW);
      digitalWrite(trig_right, LOW);
    }
  }
  
  else if (server.hasArg("advance")){
    if (server.arg("advance").equals("on")){
      digitalWrite(trig_reset, LOW);
      digitalWrite(trig_advance, HIGH);
      digitalWrite(trig_back, LOW);
      digitalWrite(trig_left, LOW);
      digitalWrite(trig_right, LOW);
    }
  }

  else if (server.hasArg("back")){
    if (server.arg("back").equals("on")){
      digitalWrite(trig_reset, LOW);
      digitalWrite(trig_advance, LOW);
      digitalWrite(trig_back, HIGH);
      digitalWrite(trig_left, LOW);
      digitalWrite(trig_right, LOW);
    }
  }

  else if (server.hasArg("left")){
    if (server.arg("left").equals("on")){
      digitalWrite(trig_reset, LOW);
      digitalWrite(trig_advance, LOW);
      digitalWrite(trig_back, LOW);
      digitalWrite(trig_left, HIGH);
      digitalWrite(trig_right, LOW);
    }
  }

  else if (server.hasArg("right")){
    if (server.arg("right").equals("on")){
      digitalWrite(trig_reset, LOW);
      digitalWrite(trig_advance, LOW);
      digitalWrite(trig_back, LOW);
      digitalWrite(trig_left, LOW);
      digitalWrite(trig_right, HIGH);
    }
  }
  
  server.send(200, "text/html", html);
}



//ip_adress to string
String out_ip(uint32_t ip){
    String result = "";
    result += String((ip & 0xFF), 10);
    result += ".";
    result += String((ip & 0xFF00) >> 8, 10);
    result = "";
    result += ".";
    result += String((ip & 0xFF0000) >> 16, 10);
    result += ".";
    result += String((ip & 0xFF000000) >> 24, 10);
    return result;
}

//Not found
void handleNotFound(void) {
  server.send(404, "text/plain", "Not Found");
}
