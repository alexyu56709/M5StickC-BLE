#include "M5StickCPlus.h"
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

#define SERVICE_UUID        "9e89d032-5ba3-11ed-9b6a-0242ac120002"
#define CHARACTERISTIC_UUID "d098ef14-1b01-4f5c-b6c0-cbea2adb9c32"

void setup() {
  M5.begin(115200);
  M5.Lcd.setTextColor(TFT_BLUE);
  M5.Lcd.setTextSize(3);
  M5.Lcd.println("BLE Turned on");

  BLEDevice::init("AYu-Server");
  BLEServer *pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService(SERVICE_UUID);
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );

  pCharacteristic->setValue("Hello World says Alex");
  pService->start();
  // BLEAdvertising *pAdvertising = pServer->getAdvertising();  // this still is working for backward compatibility
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(true);
  pAdvertising->setMinPreferred(0x06);  // functions that help with iPhone connections issue
  pAdvertising->setMinPreferred(0x12);
  BLEDevice::startAdvertising();
  M5.Lcd.println("AYu-Server online");
}

void loop() {
  // put your main code here, to run repeatedly:
  /*int Y = M5.Lcd.getCursorY();
  if (Y > 112){  //224 Max Y
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setCursor(0, 0);
  }*/
  delay(2000);
}